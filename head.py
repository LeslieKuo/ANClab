

import numpy as np
import matplotlib.pylab as plt
import padasip as pa
from scipy.io import wavfile


#Normalization function : amplify the array to the range of int16
def Normalization(arry):
    narry = arry*(32768/np.max(arry))
    narry = narry.astype(np.int16)
    return narry