import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
w=np.linspace(-np.pi,np.pi,1000)
x=[1,1,1,1]
l=len(x)
j=cm.sqrt(-1)
n=0
X_W=0
for n in range (l):
	X_W+=(x[n]*np.exp(-j*w*n))
plt.plot(w,X_W)
plt.show()
X_magnitude=np.abs(X_W)
X_phase=np.angle(X_W)
plt.subplot(211)
plt.plot(w,X_magnitude)
plt.title('magnitude spectrum')
plt.subplot(212)
plt.plot(w,X_phase)
plt.title('phase spectrum')
plt.show()

	
