import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=input("enter a signal:")
l=len(x)
N=input("enter N:")
n=np.linspace(0,N-1,N)
if (l<N):
	for i in range(N-l):
		x.append(0)
j=cm.sqrt(-1)
k=np.linspace(-2*N,2*N-1,4*N)
X_W=[]
for m in range(-2*N,2*N,1):
	s=0
	for t in range(N):
		s=s+(x[t]*np.exp(-j*2*np.pi*m*t/N))
	X_W.append(s)
plt.subplot(221)
plt.stem(n,x)
plt.subplot(222)
plt.stem(k,np.abs(X_W))
plt.subplot(223)
plt.stem(k,np.angle(X_W))
plt.subplot(224)
plt.stem(k,X_W)
plt.show()

