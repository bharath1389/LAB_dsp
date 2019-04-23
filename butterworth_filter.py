import math
dp=input("enter dp:")
ds=input("enter ds:")
wp=input("enter wp:")
ws=input("enter ws:")
wp=wp*2*np.pi
ws=ws*2*np.pi
s=math.log((1.0/(dp*dp)-1)/(1.0/(ds*ds)-1))
k=math.log(wp/ws)
N=math.ceil(0.5*(s/k))
wc=(wp/(1.0/(dp*dp)-1)**(0.5/N))
print N
print wc
w=np.linspace(0,2000*2*np.pi,1000)
h=1/(1+(w/wc)**(2*N))**0.5
H=-10*np.log10(1/(1+(w/wc)**(2*N))
plt.plot(w,h)
plt.show()
plt.plot(w,H)
plt.show()
