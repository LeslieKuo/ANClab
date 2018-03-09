
from scipy.io import wavfile
import numpy as np
#z1:5-7s z2:6-8s

orate,signal = wavfile.read('s10.wav')
orate1,noise = wavfile.read('n10.wav')  #10s dryer noise
delayPointNum = 300
print(noise.shape)
print(signal.shape)
cutHead_noise=noise[delayPointNum:]
cutTail_noise=noise[:441000-delayPointNum]
cutHead_signal=signal[delayPointNum:]
cutTail_signal = signal[:441000-delayPointNum]

Uorigin = cutHead_noise + 0.6*cutTail_signal
Vorigin = cutHead_signal + 0.8*cutTail_noise
#Uorigin = cutHead_signal
#Vorigin = cutTail_signal
U = Uorigin
V = Vorigin

print(len(U), len(V))
# 需要归一化再求互相关！
U, V = U.astype(np.float64), V.astype(np.float64)
U_max = np.max(np.abs(U))
V_max = np.max(np.abs(V))
U /= U_max
V /= V_max

csame = np.correlate(U, V, "same")

# ref = np.where(csame == np.max(csame))
ref = np.argmax(csame)
print(ref)
half_len = len(U) // 2

print(len(U), half_len)
d = abs(ref - half_len)
print(d)


a, b = Uorigin, Vorigin
if ref < half_len :
    a = a[:len(a)-d]
    b = b[d:]
else:
    b = b[:len(a)-d]
    a = a[d:]

a = a.astype(signal.dtype)
b = b.astype(signal.dtype)

print(len(a),len(b))

wavfile.write("ex7t1.wav", orate, a)
wavfile.write("ex7t2.wav", orate, b)
print(a[44100],a[88200],a[100000])
print(b[44100],b[88200],b[100000])
print([44100],a[88200],a[100000])
