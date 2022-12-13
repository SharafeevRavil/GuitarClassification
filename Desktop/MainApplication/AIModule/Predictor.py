from . import AudioPreprocessor as ap
from . import PredictionGenerator as pg
from . import Settings
from . import OutputBeautifier 
from . import CnnModel as cnnModel
import os

class Predictor():
    def load_model(self, ai_module_path = '.'):
        model = cnnModel.create_model()
        model.load_weights(os.path.join(ai_module_path, Settings.weights_path))
        return model

    def predict_audio(self, audio, model):
        gen = pg.PredictionGenerator(audio)
        return model.predict(gen)

    def predict(self, filepath, ai_module_path = '.'):
        a = ap.AudioPreprocessor()

        model = self.load_model(ai_module_path)
        audio = a.process_audiofile(filepath)
        result = self.predict_audio(audio, model)
        return OutputBeautifier.beautify_outputs(result, cat=False)

"""
if __name__ == "__main__":
    p = Predictor()
    a = AudioPreprocessor()

    model = p.load_model()
    audio = a.process_audiofile('./audio_2022-09-15_14-10-56.mp3')
    result = p.predict_audio(audio, model)
    print(OutputBeautifier.beautify_outputs(result, cat=False))
"""