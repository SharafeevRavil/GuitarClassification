import guitarpro
from AIModule.Predictor import Predictor
import AIModule.Settings as Settings

def create(filename):
    p = Predictor()
    beats = p.predict(filename, './AIModule')

    template = guitarpro.parse('blank.gp5')
    template.tracks[0].name='Guitar'
    beat_list = template.tracks[0].measures[0].voices[0].beats
    beat_list.clear()
    prev = [-1,-1,-1,-1,-1,-1]

    for beat in beats:
        new_beat = guitarpro.Beat(template.tracks[0].measures[0].voices[0], duration=guitarpro.Duration(value=8))
        new_beat.status=guitarpro.BeatStatus.normal
        for i in range(Settings.num_strings):
            if beat[i] != -1 and beat[i] != prev[i]:
                new_beat.notes.append(guitarpro.Note(new_beat, value=beat[i], string=i+1, type=guitarpro.NoteType.normal))
            prev[i] = beat[i]
        if new_beat.notes:
            beat_list.append(new_beat)

    guitarpro.write(template, 'tabs.gp5')