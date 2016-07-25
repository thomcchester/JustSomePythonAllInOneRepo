import numpy as np 
from pylab import *


x=[]
for j in range(1,256):
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="0"
        else:
            b+="1"
    x.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="1"
        else:
            b+="0"
    x.append(b)
y=[]   
for j in range(1,256):
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="00"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="11"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="0000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="1111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="00000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="11111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="0000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="1111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="00000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="11111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="000000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="111111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="0000000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="1111111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="00000000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="11111111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="000000000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="111111111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="0000000000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="1111111111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="00000000000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="11111111111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="000000000000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="111111111111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="0000000000000000"
        else:
            b+="1"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)
    b=""
    for i in range(1,256):
        if i%j==0:
            b+="1111111111111111"
        else:
            b+="0"
    hold=b
    b=""
    for i in range(0,255):
        b+=hold[i]
    y.append(b)


filehold=y+x