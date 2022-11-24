import numpy as np
import keras
import Settings

class PredictionGenerator(keras.utils.Sequence):
    
    def __init__(self, audio_chunks):
        
        self.list_IDs = range(len(audio_chunks))
        self.audio_chunks = audio_chunks
        
        self.X_dim = (Settings.batch_size, Settings.cqt_n_bins, Settings.con_win_size, 1)
        self.y_dim = (Settings.batch_size, Settings.num_strings, Settings.num_classes)
                    
        self.on_epoch_end()
        
    def __len__(self):
        return int(np.floor(float(len(self.list_IDs)) / Settings.batch_size))
    
    def __getitem__(self, index):
        indexes = self.indexes[index*Settings.batch_size:(index+1)*Settings.batch_size]
        
        list_IDs_temp = [self.list_IDs[k] for k in indexes]
        
        X = self.__data_generation(list_IDs_temp)
        
        return X
    
    def on_epoch_end(self):
        self.indexes = np.arange(len(self.list_IDs))
        if Settings.shuffle == True:
            np.random.shuffle(self.indexes)
            
    def __data_generation(self, list_IDs_temp):      
        X = np.empty(self.X_dim)

        for i, ID in enumerate(list_IDs_temp):
            
            full_x = np.pad(self.audio_chunks, [(Settings.halfwin,Settings.halfwin), (0,0)], mode='constant')
            sample_x = full_x[ID : ID + Settings.con_win_size]
            X[i,] = np.expand_dims(np.swapaxes(sample_x, 0, 1), -1)

        return X