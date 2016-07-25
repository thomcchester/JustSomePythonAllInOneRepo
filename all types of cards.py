import numpy as np
from pylab import *
import random
from collections import Counter 
#import from hard code
f=open('tcards100.txt','r')
lines=f.readlines()

#Making card list
cardlist=[]
for i in range(0,52):
    cardlist.append(i)
diamonds=[0,1,2,3,4,5,6,7,8,9,10,11,12]
hearts=[13,14,15,16,17,18,19,20,21,22,23,24,25]
clubs=[26,27,28,29,30,31,32,33,34,35,36,37,38]
spades=[39,40,41,42,43,44,45,46,47,48,49,50,51]
aces=[0,13,26,39]
kings=[1,14,27,40]
queens=[2,15,28,41]
jacks=[3,16,29,42]
tens=[4,17,30,43]
nines=[5,18,31,44]
eights=[6,19,32,45]
sevens=[7,20,33,46]
sixes=[8,21,34,47]
fives=[9,22,35,48]
fours=[10,23,36,49]
threes=[11,24,37,50]
twos=[12,25,38,51]


#now running actual cards:
wl=[[] for i in xrange(0,len(lines))]

for i in range(0,len(lines)):
    #shuffle cards:
    random.shuffle(cardlist)
    #pick which line
    cp=lines[i]#cards picked, you could insert exactly what you want here in the form, with the quotations "[first deal card, second deal card, high card, second highest, middle card, second lowest, lowest]\n" 
    cp=cp[1:-1]
    cp=cp[:-1]
    cp=cp[:-1]
    list(cp)
    cps=[]
    for j in range(0,len(cp)):
        if j!=len(cp)-1:
            if cp[j]!="," and cp[j]!=" " and cp[j+1] not in ["0","1","2","3","4","5","6","7","8","9"]:
                cps.append(int(cp[j]))
            elif cp[j]!="," and cp[j]!=" " and cp[j+1] in ["0","1","2","3","4","5","6","7","8","9"]:
                cps.append((int(cp[j])*10+int(cp[j+1])))
    cp=cps
    holdone=cp[2]
    holdtwo=cp[3]
    holdthree=cp[4]
    holdfour=cp[5]
    holdfive=cp[6]
    cardlist.remove(holdone)
    cardlist.remove(holdtwo)
    cardlist.remove(holdthree)
    cardlist.remove(holdfour)
    cardlist.remove(holdfive)
    cardlist.append(holdone)
    cardlist.append(holdtwo)
    cardlist.append(holdthree)
    cardlist.append(holdfour)
    cardlist.append(holdfive)
    
    
    