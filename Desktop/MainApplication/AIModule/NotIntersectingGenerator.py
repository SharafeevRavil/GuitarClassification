import numpy as np
import keras
import Settings

# генератор данных для нейронной сети
class NotIntersectingGenerator(keras.utils.Sequence):
    # инициализация (загрузка id музыкальных фрагментов)
    # id в формате ['00_BN1-129-Eb_comp' id]
    def __init__(self, list_IDs):
        # сохраняем id фрагментов
        self.list_IDs = list_IDs[::Settings.con_win_size]
        # сохраняем размеры данных
        self.X_dim = (Settings.batch_size, Settings.cqt_n_bins, Settings.con_win_size, 1)
        self.y_dim = (Settings.batch_size, Settings.num_strings, Settings.num_classes)
        # перемешиваем
        self.on_epoch_end()
    
    # длина данных - {колво id} / {размер батча} (округлено вниз)
    def __len__(self):
        return int(np.floor(float(len(self.list_IDs)) / Settings.batch_size))
    
    # получение батча по индексу (от 0 до длины)
    def __getitem__(self, index):
        indexes = self.indexes[index * Settings.batch_size : (index + 1) * Settings.batch_size]
        
        list_IDs_temp = [self.list_IDs[k] for k in indexes]
        
        X, y = self.__data_generation(list_IDs_temp)
        
        return X, y
    
    # в конце эпохи - перемешиваем id
    def on_epoch_end(self):
        self.indexes = np.arange(len(self.list_IDs))
        if Settings.shuffle == True:
            np.random.shuffle(self.indexes)
    
    # возвращение данных для заданных id
    def __data_generation(self, list_IDs_temp):      
        X = np.empty(self.X_dim)
        y = np.empty(self.y_dim)

        for i, ID in enumerate(list_IDs_temp):
            
            data_dir = Settings.dataset_path + "/"
            filename = ID[0] + ".npz"
            frame_id = ID[1]
            
            loaded = np.load(data_dir + filename)
            full_x = loaded["audio_chunks"]
            # дополняем пустыми фреймами
            full_x = np.pad(full_x, [(Settings.halfwin, Settings.halfwin), (0, 0)], mode='constant') # дополняем нулями
            sample_x = full_x[frame_id : frame_id + Settings.con_win_size] # берем окно с центром нашего id
            # поворачиваем матрицу в представление для нейросети
            sample_x = np.swapaxes(sample_x, 0, 1)
            X[i,] = np.expand_dims(sample_x, -1)

            y[i,] = loaded["frets"][frame_id]

        return X, y