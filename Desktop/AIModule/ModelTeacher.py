import pandas as pd
import numpy as np
import Settings
from DataGenerator import DataGenerator
from sklearn.model_selection import train_test_split
import CnnModel as cnnModel

class ModelTeacher():
    def load_IDs(self):
        csv_file = Settings.ids_path
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

    def teach_model(self, model, gen_train, callbacks = [], workers = 6):
        history = model.fit(x = gen_train
                    ,validation_data=None
                    ,epochs=Settings.epochs
                    ,verbose=1
                    #,use_multiprocessing=True # не работает и намертво лочит комп - возможно генератор плохо написан
                    ,workers=workers
                    ,callbacks = callbacks
                    )
        return history

    def save_weights(self, model):
        model.save_weights(Settings.weights_path)

    def test_model(self, model, gen_test, workers = 6):
        predictions = model.predict(x = gen_test
                    ,verbose=1
                    #,use_multiprocessing=True
                    ,workers=workers
                    )
        return predictions



if __name__ == "__main__":
    mt = ModelTeacher()

    ids = mt.load_IDs()
    ids_train, ids_test = train_test_split(ids, test_size= (1 - Settings.train_split), random_state=42)
    gen_train = DataGenerator(ids_train)
    gen_test = DataGenerator(ids_test)

    model = cnnModel.create_model()
    mt.teach_model(model, gen_train)
    mt.save_weights(model)
    mt.test_model(model, gen_test)