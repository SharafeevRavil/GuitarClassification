#preprocessor settings
string_midi_pitches = [40,45,50,55,59,64]
highest_fret = 19
num_classes = highest_fret + 2 # открытая/не играется

need_to_downsample = True
need_to_normalize = True
sr_downs = 22050

cqt_n_bins = 192
cqt_bins_per_octave = 24
hop_length = 512 #длина фрейма в герцах
#длина фрейма в секундах - hop_length / sr

#model settings
con_win_size = 9
halfwin = con_win_size // 2
num_classes = 21
num_strings = 6
input_shape = (cqt_n_bins, con_win_size, 1)
train_split = .65
epochs = 8

batch_size = 128
shuffle = True

#data paths
dataset_path = './data/repr/'
ids_path = './data/ids.csv'
mic_path = './GuitarSet/audio/mic/'
annotations_path = './GuitarSet/annotation/'
weights_path = './data/output/weights.h5'