from . import Settings
import numpy as np

def beautify_output(output, cat):
    res = np.copy(output)
    if not cat:
        res_int = np.empty(Settings.num_strings)
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
        if not cat:
            res_int[i] = categorial_to_int(res[i])
    if cat:
        return res
    else:
        return res_int

def categorial_to_int(cat):
    return(np.where(cat == 1.)[0][0]-1)

def beautify_outputs(outputs, cat=True):
    if cat:
        res = np.copy(outputs)
    else:
        res = np.empty((len(outputs), Settings.num_strings))
    for i in range(len(outputs)):
        res[i] = beautify_output(outputs[i], cat)
    return res