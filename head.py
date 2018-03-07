

import numpy as np
import matplotlib.pylab as plt
import padasip as pa
from scipy.io import wavfile


def Normalization(arry):
    m = (arry - np.min(arry))/(np.max(arry)-np.min(arry))
