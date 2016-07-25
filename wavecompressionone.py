from pylab import *

value=""
for i in range(0,256):
    holder=random()
    if holder<.5:
        value+=str(0)
    else:
        value+=str(1)

a1=""
for i in range(0,256):
    if i%2==0:
        a1+=str(0)
    else:
        a1+=str(1)
        
a2=""
for i in range(0,256):
    if i%2==0:
        a2+=str(1)
    else:
        a2+=str(0)

b1=""
for i in range(0,265/3):
    b1+="001"
for i in range(0,8):
    b1=b1[:-1]


b2="01"
for i in range(0,265/3):
    b2+="001"
for i in range(0,10):
    b2=b2[:-1]
   

b3="1"
for i in range(0,265/3):
    b3+="001"
for i in range(0,10):
    b3=b3[:-1]
    

b4=""
for i in range(0,265/3):
    b4+="011"
for i in range(0,8):
    b4=b4[:-1]


b6="11"
for i in range(0,265/3):
    b6+="011"
for i in range(0,10):
    b6=b6[:-1]
    print len(b6)
    
    
b5="1"
for i in range(0,265/3):
    b5+="011"
for i in range(0,9):
    b5=b5[:-1]
    print len(b5)
    
c1=""
for i in range(0,256/4):
    c1+="0011"
c2="011"
for i in range(0,256/4):
    c2+="0011"
for i in range(0,3):
    c2=c2[:-1]


c3="11"
for i in range(0,256/4):
    c3+="0011"
for i in range(0,2):
    c3=c3[:-1]


c4="1"
for i in range(0,256/4):
    c4+="0011"
for i in range(0,1):
    c4=c4[:-1]
   
    
d1=""
for i in range(0,256/4):
    d1+="0001"
    

d2="001"
for i in range(0,256/4):
    d2+="0001"
for i in range(0,3):
    d2=d2[:-1]
    print len(d2)
    
d3="01"
for i in range(0,256/4):
    d3+="0001"
for i in range(0,2):
    d3=d3[:-1]


d4="1"
for i in range(0,256/4):
    d4+="0001"
for i in range(0,1):
    d4=d4[:-1]
    print len(d4)
    
d5=""
for i in range(0,256/4):
    d5+="0111"
#for i in range(0,1):
#    d4=d4[:-1]
    print len(d5)

d6="111"
for i in range(0,256/4):
    d6+="0111"
for i in range(0,3):
    d6=d6[:-1]
    print len(d6)
    
d7="11"
for i in range(0,256/4):
    d7+="0111"
for i in range(0,2):
    d7=d7[:-1]
    print len(d7)

d8="1"
for i in range(0,256/4):
    d8+="0111"
for i in range(0,1):
    d8=d8[:-1]
    print len(d8)
    
e1=""
for i in range(0,256/4):
    e1+="1110"

    
e2="110"
for i in range(0,256/4):
    e2+="1110"

for i in range(0,3):
    e2=e2[:-1]

e3="10"
for i in range(0,256/4):
    e3+="1110"
for i in range(0,3):
    e3=e3[:-1]

f1=""
for i in range(0,256/5+1):
    f1+="00011"
for i in range(0,4):
    f1=f1[:-1]
    
f2="011"
for i in range(0,256/5):
    f2+="00011"
for i in range(0,2):
    f2=f2[:-1]
f3="11"
for i in range(0,256/5):
    f3+="00011"
for i in range(0,1):
    f3=f3[:-1]
f4="1"
for i in range(0,256/5):
    f4+="00011"
f6=""
for i in range(0,256/5):
    f6+="00111"  
f6+="0"

f7="0111"
for i in range(0,256/5):
    f7+="00111" 
for i in range(0,3):
    f7=f7[:-1]
    

print len(f7)
print f7

