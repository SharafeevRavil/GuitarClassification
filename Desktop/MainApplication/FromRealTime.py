from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QUrl, QRunnable, Slot, QThreadPool, QTimer, QObject, Signal
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWebEngineCore import QWebEngineSettings
from Ui.ui_FromRealTime import Ui_FromRealTime
import GPCreator
import settings
import os
import sys
import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import FileHelper as fh

class WorkerSignals(QObject):
    finished = Signal()

class RecordWorker(QRunnable):
    def __init__(self, isFirstRun):
        super(RecordWorker, self).__init__()
        self.isFirstRun = isFirstRun
        self.signals = WorkerSignals()

    @Slot()
    def run(self,):
        recording = sd.rec(int(settings.record_duration * settings.record_frequency), 
                   samplerate=settings.record_frequency, channels=settings.record_channels)
        sd.wait()
        folder = fh.getPathInRoot(settings.real_time_folder)
        now = datetime.utcnow().strftime("%Y.%m.%d_%H.%M.%S")
        self.filename = fh.getPathInFolder(folder, now+"_recording.wav")
        os.makedirs(folder, exist_ok=True)
        write(self.filename, settings.record_frequency, recording)
        self.signals.finished.emit()

class FromRealTime(QtWidgets.QWidget):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_FromRealTime()
        self.ui.setupUi(self)

        self.ui.button_play.clicked.connect(self.start_recording)
        self.ui.button_stop.clicked.connect(self.stop_recording)
        #self.ui.button_submit.clicked.connect(self.generate) is in MainWindow.py
        self.ui.button_return.clicked.connect(self.return_button)
        self.main_window.ui.stackedWidget.currentChanged.connect(self.stop_recording)

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.timer = QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.record_chunk)

    def clear(self):
        self.isFirstRun = True
        self.ui.webEngineView.load('')
        self.ui.button_play.setEnabled(True)
        self.ui.button_stop.setEnabled(False)   

    def return_button(self):
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.ui.page_welcome)
    
    def start_recording(self):
        self.isFirstRun = True
        self.ui.button_play.setEnabled(False)
        self.ui.button_stop.setEnabled(True)
        self.timer.start()

    def stop_recording(self):
        self.ui.button_play.setEnabled(True)
        self.ui.button_stop.setEnabled(False)
        self.timer.stop() 

    def record_chunk(self):
        worker = RecordWorker(self.isFirstRun)
        worker.signals.finished.connect(lambda : self.load_tab(worker.filename, self.isFirstRun))
        self.threadpool.start(worker)
        self.isFirstRun = False
            
    def load_tab(self, filename, isFirstRun):
        GPCreator.create(filename, not isFirstRun)
        url = QUrl.fromLocalFile(fh.getPathInRoot('.\\tab.html'))
        self.ui.webEngineView.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.ui.webEngineView.load(url)
        