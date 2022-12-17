import guitarpro
from AIModule.Predictor import Predictor
import AIModule.Settings as AISettings
import settings

def create(filename, toConcat = False):
    p = Predictor()
    beats = p.predict(filename, './AIModule')

    if toConcat:
        template = guitarpro.parse(settings.tab_file)
        beat_list = template.tracks[0].measures[0].voices[0].beats
        prev = [-1,-1,-1,-1,-1,-1]
    else:
        template = guitarpro.parse(settings.blank_file)
        template.tracks[0].name='Guitar'
        beat_list = template.tracks[0].measures[0].voices[0].beats
        beat_list.clear()
        prev = [-1,-1,-1,-1,-1,-1]

    for beat in beats:
        new_beat = guitarpro.Beat(template.tracks[0].measures[0].voices[0], duration=guitarpro.Duration(value=8))
        new_beat.status=guitarpro.BeatStatus.normal
        for i in range(AISettings.num_strings):
            if beat[i] != -1 and beat[i] != prev[i]:
                new_beat.notes.append(guitarpro.Note(new_beat, value=beat[i], string=i+1, type=guitarpro.NoteType.normal))
            prev[i] = beat[i]
        if new_beat.notes:
            beat_list.append(new_beat)

    guitarpro.write(template, settings.tab_file)