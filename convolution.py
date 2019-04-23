import numpy as np
import matplotlib.pyplot as plt
x=input("enter the first signal:")
h=input("enter the second signal:")
m=len(x)
n=len(h)
y=np.zeros(m+n-1)
for j in range(m):
	for i in range(n):
		y[j+i]=y[j+i]+x[j]*h[i]
for i in range(m-1):
	h.append(0)
for j in range(n-1):
	x.append(0)
plt.subplot(311)
plt.stem(x)
plt.subplot(312)
plt.stem(h)
plt.subplot(313)
plt.stem(y)
plt.show()
		
