import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,1,100)
n=np.linspace(-10,10,20)
f=input("enter a low frequency[Hz]:")
f=f*1.0
fs=input("enter a high frequency[HZ]:")
fs=fs*1.0
x=np.sin(2*np.pi*(f/fs)*n)
plt.subplot(224)
plt.stem(n,x)
plt.show()
p=input("enter current sample value:")
s=0
i=0
for i in range(p):
	s=s+x[i]
	print("sum of first %d samples is :%f"%(i,s))
print("final accumulator output is:%f"%(s))
