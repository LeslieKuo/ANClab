import numpy as np
import matplotlib.pylab as plt
import padasip as pa
from scipy.io import wavfile
import head as hd


orate,signal = wavfile.read('s10.wav')
orate1,noise = wavfile.read('n10.wav')  #10s dryer noise
delayPointNum = 300
print(noise.shape)
print(signal.shape)
cutHead_noise=noise[delayPointNum:]
cutTail_noise=noise[:441000-delayPointNum]
cutHead_signal=signal[delayPointNum:]
cutTail_signal = signal[:441000-delayPointNum]



U = cutHead_noise + 0.05*cutTail_signal
V = 0.1*cutHead_signal + 0.9*cutHead_noise
# filtering
n = 20  # length of filter
Udelay = pa.input_from_history(U, n)[:-1]


Vdelay=V[n-1:-1]
f = pa.filters.FilterRLS(mu=0.99, n=n)
y, e, w = f.run(Vdelay, Udelay)
music = e.astype(signal.dtype)
music =music[44100:]
mmax =np.max(music)
print(mmax)
music = music*32768//mmax
print(np.max(music))
music = music.astype(signal.dtype)
UU = U.astype(signal.dtype)
VV = V.astype(signal.dtype)

wavfile.write('ex6U.wav',orate,UU)
wavfile.write('ex6V.wav',orate,VV)
wavfile.write('ex6result.wav',orate,music)