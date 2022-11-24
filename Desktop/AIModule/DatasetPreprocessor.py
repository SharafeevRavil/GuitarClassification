import os
import numpy as np
import jams
import librosa
from keras.utils import to_categorical
import Settings
from AudioPreprocessor import AudioPreprocessor

class DatasetPreprocessor:
    # загрузка файла аннотации
    def load_jam(self, filename):
        file_anno = Settings.annotations_path + filename + ".jams"
        jam = jams.load(file_anno)
        return jam

    # обработка аудиофайла
    def process_audiofile(self, filename):
        #sr_original, data, jam = self.load_file(filename)
        jam = self.load_jam(filename)

        audioPreprocessor = AudioPreprocessor()
        file_audio = Settings.mic_path + filename + "_mic.wav"
        audio_chunks = audioPreprocessor.process_audiofile(file_audio)
        
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

        # обрезаем фреймы, которые не влезают 
        # (решили не обрезать, решили добавлять нулевые фреймы, что даст возможность размечать весь аудиофайл)
        # calc_len = len(audio_chunks) // Settings.con_win_size * Settings.con_win_size
        # audio_chunks = audio_chunks[:calc_len]
        # frets = frets[:calc_len]
        return audio_chunks, frets
    
    # то, что струна не играется обозначается -1, далее лады от 0 до 19
    # чтобы to_categorical сработал корректно, избавляемся от -1, сдвинув все обозначения направо:
    # было:
    # [  -1   ;     0    ;   1  ;   2  ; ... ;   19  ]
    # [не игр.; откр. лад; лад 1; лад 2; ... ; лад 19]
    # стало:
    # [   0   ;     1    ;   2  ;   3  ; ... ;   20  ]
    # [не игр.; откр. лад; лад 1; лад 2; ... ; лад 19]
    def correct_numbering(self, n):
        n += 1
        if n < 0:
            n = 0
        elif n > Settings.highest_fret + 1:
            n = Settings.highest_fret + 1
        return n
        
    def clean_fret(self, fret):
        fret = [self.correct_numbering(n) for n in fret]
        return to_categorical(fret, Settings.num_classes)
    
    def clean_frets(self, frets):
        return np.array([self.clean_fret(fret) for fret in frets])

    # получает все имена файлов по папке с аннотациями
    def get_all_filenames(self):
        return [file[:-5] for file in os.listdir(Settings.annotations_path) if file.endswith(".jams")]

    def process_audiofile_and_save(self, filename, folder_path = Settings.dataset_path, idsFile = Settings.ids_path):
        audio_chunks, frets = self.process_audiofile(filename)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        save_path = os.path.join(folder_path, filename + ".npz")
        np.savez(save_path, audio_chunks=audio_chunks, frets=frets)

        with open(idsFile, 'a+') as ids:
            # для обучения сохраняем все фреймы - для крайних будем дополнять пустыми фреймами до размера окна
            for i in range(len(audio_chunks)):
                ids.write(filename + ',' + str(i))
                ids.write('\n')

if __name__ == "__main__":
    dataset = DatasetPreprocessor()

    # сносим старые файлы
    try:
        os.remove(Settings.ids_path)
    except OSError:
        pass
    try:
        for file in os.listdir(Settings.dataset_path):
            if file.endswith(".npz"):
                os.remove(os.path.join(Settings.dataset_path, file))
    except OSError:
        pass

    filenames = dataset.get_all_filenames()
    for filename in filenames:
        dataset.process_audiofile_and_save(filename)
        