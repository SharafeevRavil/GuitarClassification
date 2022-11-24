import Settings
import numpy as np

def beautify_output(output):
    res = np.copy(output)
    for i in range(Settings.num_strings):
        max = -1
        max_j = -1
        for j in range(Settings.num_classes):
            if(output[i][j] > max):
                max = output[i][j]
                max_j = j
        for j in range(Settings.num_classes):
            if j == max_j:
                res[i][j] = 1
            else:
                res[i][j] = 0
    return res

def beautify_outputs(outputs):
    res = np.copy(outputs)
    for i in range(len(outputs)):
        res[i] = beautify_output(outputs[i])
    return res