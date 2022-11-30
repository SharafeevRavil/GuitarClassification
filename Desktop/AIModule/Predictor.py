import Settings
from AudioPreprocessor import AudioPreprocessor
from PredictionGenerator import PredictionGenerator
import CnnModel as cnnModel

class Predictor():
    def load_model(self):
        model = cnnModel.create_model()
        model.load_weights(Settings.weights_path)
        return model

    def predict(self, audio, model):
        gen = PredictionGenerator(audio)
        return model.predict(gen)

if __name__ == "__main__":
    p = Predictor()
    a = AudioPreprocessor()

    model = p.load_model()
    audio = a.process_audiofile('./audio_2022-09-15_14-10-56.mp3')
    result = p.predict(audio, model)
    print(result)