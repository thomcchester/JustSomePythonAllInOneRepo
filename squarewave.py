from pylab import *

a1="0"
a2="1"
b1="00"
b2="01"
b3="1"
b4="0"


for i in range(0,127):
    if i%2==0:
        a1=a1+"1"
    else:
        a1=a1+"0"

for i in range(0,127):
    if i%2==0:
        a2=a2+"0"
    else:
        a2=a2+"1"
for i in range(0,int(math.floor(127/1.5))):
    if i%2==0:
        b1=b1+"1"
    else:
        b1=b1+"00"

for i in range(0,int(math.floor(127/1.5))):
    if i%2==0:
        b2=b2+"00"
    else:
        b2=b2+"1"
for i in range(0,int(math.ceil(127/1.5))):
    if i%2==0:
        b3=b3+"00"
    else:
        b3=b3+"1"
    if len(b3)==129:
        b3=b3[:-1]
