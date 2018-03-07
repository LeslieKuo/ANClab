
import numpy as np
import matplotlib.pylab as plt
import padasip as pa
from scipy.io import wavfile
import head as hd


orate,signal = wavfile.read('s10.wav')
orate1,noise = wavfile.read('n10.wav')  #10s dryer noise

print(noise.shape)
print(signal.shape)
#noise = noise + 0.001*signal #noise add small signal
V = signal + 0.6*noise
U = noise + 0.6*signal
# filtering
n = 20  # length of filter
U = pa.input_from_history(U, n)[:-1]


V=V[n-1:-1]
f = pa.filters.FilterRLS(mu=0.99, n=n)
y, e, w = f.run(V, U)
#V = V.astype(signal.dtype)
#e = hd.Normalization(e)
music = e.astype(signal.dtype)


wavfile.write('ex3result.wav',orate,music)