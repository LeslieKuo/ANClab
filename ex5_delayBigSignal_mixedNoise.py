import numpy as np
import matplotlib.pylab as plt
import padasip as pa
from scipy.io import wavfile
import head as hd


orate,signal = wavfile.read('s10.wav')
orate1,noise = wavfile.read('n10.wav')  #10s dryer noise
delayPointNum=300
print(noise.shape)
print(signal.shape)
cut_noise=noise[delayPointNum:]
cut_signal=signal[delayPointNum:]
delay_signal = signal[:441000-delayPointNum]


print(delay_signal.shape)
#noise = noise + 0.001*signal #noise add small signal
U = cut_noise + 0.9*delay_signal
V = cut_signal + 0.9*cut_noise
# filtering
n = 20  # length of filter
U = pa.input_from_history(U, n)[:-1]


V=V[n-1:-1]
f = pa.filters.FilterRLS(mu=0.99, n=n)
y, e, w = f.run(V, U)
#V = V.astype(signal.dtype)
#e = hd.Normalization(e)

#music = signal *32768/signal[300000]
#music = signal * 3000
music = e.astype(signal.dtype)
wavfile.write('ex5result.wav',orate,music)