import numpy as np
import keras
import Settings

class DataGenerator(keras.utils.Sequence):
    
    def __init__(self, list_IDs):
        
        self.list_IDs = list_IDs
        
        self.X_dim = (Settings.batch_size, Settings.cqt_n_bins, Settings.con_win_size, 1)
        self.y_dim = (Settings.batch_size, Settings.num_strings, Settings.num_classes)
                    
        self.on_epoch_end()
        
    def __len__(self):
        return int(np.floor(float(len(self.list_IDs)) / Settings.batch_size))
    
    def __getitem__(self, index):
        indexes = self.indexes[index*Settings.batch_size:(index+1)*Settings.batch_size]
        
        list_IDs_temp = [self.list_IDs[k] for k in indexes]
        
        X, y = self.__data_generation(list_IDs_temp)
        
        return X, y
    
    def on_epoch_end(self):
        self.indexes = np.arange(len(self.list_IDs))
        if Settings.shuffle == True:
            np.random.shuffle(self.indexes)
            
    def __data_generation(self, list_IDs_temp):      
        X = np.empty(self.X_dim)
        y = np.empty(self.y_dim)

        for i, ID in enumerate(list_IDs_temp):
            
            data_dir = Settings.dataset_path + "/"
            filename = "_".join(ID.split("_")[:-1]) + ".npz"
            frame_idx = int(ID.split("_")[-1])
            
            loaded = np.load(data_dir + filename)
            full_x = np.pad(loaded["repr"], [(Settings.halfwin,Settings.halfwin), (0,0)], mode='constant')
            sample_x = full_x[frame_idx : frame_idx + Settings.con_win_size]
            X[i,] = np.expand_dims(np.swapaxes(sample_x, 0, 1), -1)

            y[i,] = loaded["labels"][frame_idx]

        return X, y