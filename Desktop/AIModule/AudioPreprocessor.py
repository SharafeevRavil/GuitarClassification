import os
import numpy as np
import jams
from scipy.io import wavfile
import sys
import librosa
from keras.utils import to_categorical
import Settings

class AudioPreprocessor:
    # загрузка аудиофайла по пути
    def load_file(self, filename):
        data, sr_original = librosa.load(filename)
        return sr_original, data

    # обработка аудиофайла (загрузка -> нормализация -> даунсемплинг -> преобразование cqt)
    def process_audiofile(self, filename):
        sr_original, data = self.load_file(filename)

        if Settings.need_to_normalize:
            data = self.normalize(data)

        if Settings.need_to_downsample:
            data = self.downsample(data, sr_original, Settings.sr_downs)

        cqt = self.cqt(data, Settings.sr_downs)
        audio_chunks = np.swapaxes(cqt, 0, 1) # поворачиваем чанки, чтобы их удобнее было итерировать

        return audio_chunks

    # внутренний метод нормализации
    def normalize(self, data):
        data = data.astype(float)            
        data = librosa.util.normalize(data)
        return data

    # внутренний метод даунсемплинга
    def downsample(self, data, sr_original, sr_downs):
        data = data.astype(float)            
        data = librosa.resample(data, orig_sr=sr_original, target_sr=sr_downs)
        return data

    # внутренний метод Constant-Q Transform
    def cqt(self, data, sr):
        data = data.astype(float)            
        data = np.abs(librosa.cqt(data,
            hop_length=Settings.hop_length, 
            sr=sr, 
            n_bins=Settings.cqt_n_bins, 
            bins_per_octave=Settings.cqt_bins_per_octave))
        return data

    