import pandas as pd
import numpy as np
import Settings
import os
import json
import keras
import random
from DataGenerator import DataGenerator
from NotIntersectingGenerator import NotIntersectingGenerator as NIGenerator
from sklearn.model_selection import train_test_split
import CnnModel as cnnModel
import matplotlib
#matplotlib.use('tkagg')
#from matplotlib import pyplot

class ModelTeacher():
    def load_IDs(self):
        csv_file = os.path.realpath(os.path.join(os.path.dirname(__file__), Settings.ids_path))
        ids = np.array(pd.read_csv(csv_file, header=None))
        return ids

    def split_IDs(self, ids):
        train_ids = []
        test_ids = []
        for i in ids:
            result = np.random.choice(2, p=[Settings.train_split, 1 - Settings.train_split])
            if result == 1:
                test_ids.append(i)
            else:
                train_ids.append(i)
        return train_ids, test_ids

    def teach_model(self, model, gen_train, callbacks = [], workers = 6, gen_test = None, epochs=Settings.epochs):
        history = model.fit(x = gen_train
                    ,validation_data=gen_test
                    ,epochs=epochs
                    ,verbose=1
                    #,use_multiprocessing=True # не работает и намертво лочит комп - возможно генератор плохо написан
                    ,workers=workers
                    ,callbacks = callbacks
                    )
        return history

    def save_weights(self, model):
        model.save_weights(Settings.weights_path)

    def test_model(self, model, gen_test, workers = 6):
        predictions = model.evaluate(x = gen_test
                    ,verbose=1
                    #,use_multiprocessing=True
                    ,workers=workers
                    )
        return predictions

    def group_by_song(self, ids):
        new_ids = []
        for id in ids:
            flag = False
            for new_id in new_ids:
                if new_id[0][0] == id[0]:
                    flag = True
                    new_id.append(id)
                    break
            if not flag:
                new_ids.append([id])
        return new_ids

    def remove_excess_ids(self, songs):
        new_songs = []
        for song in songs:
            new_songs.append(song[::Settings.con_win_size])
        return new_songs

    def split_songs(self, songs, random_state):
        train = []
        test = []
        random.Random(random_state).shuffle(songs)
        for song in songs:
            if len(train) == 0 or len(train) / (len(test) + len(train)) < Settings.train_split:
                for id in song:
                    train.append(id)
            else:
                for id in song:
                    test.append(id)
        return train, test

class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.loss = []
        self.avg_acc = []
        self.val_loss = []
        self.val_avg_acc = []

    def on_batch_end(self, batch, logs={}):
        self.loss.append(logs.get('loss'))
        self.avg_acc.append(logs.get('avg_acc'))
        self.val_loss.append(logs.get('val_loss'))
        self.val_avg_acc.append(logs.get('val_avg_acc'))

    def get_data(self):
        return {
            "loss": self.loss,
            "avg_acc": self.avg_acc,
            "val_loss": self.val_loss,
            "val_avg_acc": self.val_avg_acc
        }


if __name__ == "__main__":
    mt = ModelTeacher()

    ids = mt.load_IDs()
    songs = mt.group_by_song(ids)
    songs = mt.remove_excess_ids(songs)
    ids_train, ids_test = mt.split_songs(songs, 42)
    gen_train = DataGenerator(ids_train)
    gen_test = DataGenerator(ids_test)

    model = cnnModel.create_model()
    
    lossHistory = LossHistory()
    history = mt.teach_model(model, gen_train, [lossHistory])

    mt.save_weights(model)
    
    #pyplot.title('Loss')
    #pyplot.plot(history.history['loss'], label='train')
    #pyplot.legend()
    #pyplot.show()
    
    #pyplot.title('Loss by batches')
    #pyplot.plot(lossHistory.loss, label='loss')
    #pyplot.plot(lossHistory.avg_acc, label='avg_acc')
    #pyplot.legend()
    #pyplot.show()

    historyFile = os.path.realpath(os.path.join(os.path.dirname(__file__), "history.json"))
    json.dump(history.history, open(historyFile, 'w'))
    lossHistoryFile = os.path.realpath(os.path.join(os.path.dirname(__file__), "lossHistory.json"))
    json.dump(lossHistory.get_data(), open(lossHistoryFile, 'w'))
    
    results = mt.test_model(model, gen_test)
    print("test loss, test acc:", results)