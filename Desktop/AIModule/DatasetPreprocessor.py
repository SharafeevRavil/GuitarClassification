import os
import numpy as np
import jams
from scipy.io import wavfile
import sys
import librosa
from keras.utils import to_categorical
import Settings

class DatasetPreprocessor:

    def load_file(self, filename):
        file_audio = Settings.mic_path + filename + "_mic.wav"
        file_anno = Settings.annotations_path + filename + ".jams"
        jam = jams.load(file_anno)
        sr_original, data = wavfile.read(file_audio)
        return sr_original, data, jam

    def process_audiofile(self, filename):
        sr_original, data, jam = self.load_file(filename)

        if Settings.need_to_normalize:
            data = self.normalize(data)
        if Settings.need_to_downsample:
            data = self.downsample(data, sr_original, Settings.sr_downs)
        audio_chunks = np.swapaxes(self.cqt(data, Settings.sr_downs),0,1)
        
        chunk_indices = range(len(audio_chunks))
        times = librosa.frames_to_time(chunk_indices, sr = Settings.sr_downs, hop_length=Settings.hop_length)
        
        frets = []
        for string_num in range(6):
            anno = jam.annotations["note_midi"][string_num]
            string_note_samples = anno.to_samples(times)
            string_fret_samples = []
            for i in chunk_indices:
                if string_note_samples[i] == []:
                    string_fret_samples.append(-1)
                else:
                    #номер лада = миди номер из файла - миди номер ноты открытой струны
                    #каждый лад отличается друг от друга на полутон
                    #миди ноты тоже отличаются друг от друга на полутон
                    string_fret_samples.append(int(round(string_note_samples[i][0]) - Settings.string_midi_pitches[string_num]))
            frets.append([string_fret_samples])
            
        frets = np.array(frets)
        frets = np.squeeze(frets)
        frets = np.swapaxes(frets,0,1)
        
        frets = self.clean_frets(frets)

        return audio_chunks, frets
    
    def correct_numbering(self, n):
        n += 1
        if n < 0:
            n = 0
        elif n > Settings.highest_fret + 1:
            n = Settings.highest_fret + 1
        return n
    
    def categorical(self, fret):
        return to_categorical(fret, Settings.num_classes)
    
    def clean_fret(self, fret):
        fret = [self.correct_numbering(n) for n in fret]
        return self.categorical(fret)
    
    def clean_frets(self, frets):
        return np.array([self.clean_fret(fret) for fret in frets])

    def normalize(self, data):
        data = data.astype(float)            
        data = librosa.util.normalize(data)
        return data

    def downsample(self, data, sr_original, sr_downs):
        data = data.astype(float)            
        data = librosa.resample(data, sr_original, sr_downs)
        return data

    def cqt(self, data, sr):
        data = data.astype(float)            
        data = np.abs(librosa.cqt(data,
            hop_length=Settings.hop_length, 
            sr=sr, 
            n_bins=Settings.cqt_n_bins, 
            bins_per_octave=Settings.cqt_bins_per_octave))
        return data

    def get_all_filenames(self):
        return [file[:-5] for file in os.listdir(Settings.annotations_path) if file.endswith(".jams")]

    def save_audiofile(self, audio_chunks, frets, filename):
        if not os.path.exists(Settings.dataset_path):
            os.makedirs(Settings.dataset_path)
        audiofile = {}
        audiofile['repr'] = audio_chunks
        audiofile['labels'] = frets
        np.savez(Settings.dataset_path + filename, **audiofile)
        with open(Settings.ids_path, 'a+') as ids:
            for i in range(len(audio_chunks)):
                ids.write(filename + '_' + str(i))
                ids.write('\n')


dataset = DatasetPreprocessor()

filenames = dataset.get_all_filenames()
for filename in filenames:
    audio_chunks, frets = dataset.process_audiofile(filename)
    try:
        os.remove(Settings.ids_path)
    except OSError:
        pass
    dataset.save_audiofile(audio_chunks, frets, filename)
    