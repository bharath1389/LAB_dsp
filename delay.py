import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
[fs,y]=wav.read("/home/rgukt/Desktop/voice.wav")
fs=8000.00
wav.write("/home/rgukt/Desktop/v1.wav",2*fs,y)
plt.plot(y)
plt.show()
