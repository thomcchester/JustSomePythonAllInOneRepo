from pylab import *


tlist=[]
xlist=[]
vlist=[]
t=0.0
dt=.000001
x=.30
v=0.0
l=1.0
uk=.4
g=9.8
tf=10.0
k=g/l
tlist.append(t)
xlist.append(x)
vlist.append(v)

while x<l:
    a=k*x-uk*(l-x)*g
    v=v+a*dt
    x=x+v*dt
    t= t + dt
    tlist.append(t)
    xlist.append(x)
    vlist.append(v)
print (t)
print "joe sucks"
