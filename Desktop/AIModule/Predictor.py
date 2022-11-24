import keras
import os
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Reshape, Activation
from keras.layers import Conv2D, MaxPooling2D, Conv1D, Lambda
from keras import backend as K
import pandas as pd
import numpy as np
import datetime
import Settings
from AudioPreprocessor import AudioPreprocessor
from PredictionGenerator import PredictionGenerator

class Predictor():

    def softmax_by_string(self, t):
        string_sm = []
        for i in range(Settings.num_strings):
            string_sm.append(K.expand_dims(K.softmax(t[:,i,:]), axis=1))
        return K.concatenate(string_sm, axis=1)

    def catcross_by_string(self, target, output):
        loss = 0
        for i in range(Settings.num_strings):
            loss += K.categorical_crossentropy(target[:,i,:], output[:,i,:])
        return loss

    def avg_acc(self, y_true, y_pred):
        return K.mean(K.equal(K.argmax(y_true, axis=-1), K.argmax(y_pred, axis=-1)))

    def load_model(self):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3),
                                activation='relu',
                                input_shape=Settings.input_shape))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))   
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(Settings.num_classes * Settings.num_strings))
        model.add(Reshape((Settings.num_strings, Settings.num_classes)))
        model.add(Activation(self.softmax_by_string))

        model.compile(loss=self.catcross_by_string,
                        optimizer=keras.optimizers.Adadelta(),
                        metrics=[self.avg_acc])

        model.load_weights(Settings.weights_path)
        return model

    def predict(self, audio, model):
        gen = PredictionGenerator(audio)
        return model.predict(gen)

p = Predictor()
a = AudioPreprocessor()

model = p.load_model()
audio = a.process_audiofile('./audio_2022-09-15_14-10-56.mp3')
result = p.predict(audio, model)
print(result)