import os

def getPathInRoot(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)

def getPathInFolder(folder, path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), folder, path)