import numpy as np
from scipy.io import wavfile

def splitChannel(srcMusicFile):
    #read
    sampleRate, musicData = wavfile.read(srcMusicFile)
    #
    left = []
    right = []
    for item in musicData:
        left.append(item[0])
        right.append(item[1])

    wavfile.write('U.wav' , sampleRate, np.array(left))
    wavfile.write('V.wav', sampleRate, np.array(right))



splitChannel('src.wav')