from pylab import *
import numpy
from operator import itemgetter
import collections
import math
import heapq
np=5 #number of players

#making cards
cardlist=[]
for i in range(0,52):
    cardlist.append(i)
for j in range (0,51):
        q1=numpy.random.randint(0,len(cardlist))
        q2=numpy.random.randint(0,len(cardlist))
        b=cardlist[q1]
        del cardlist[q1]
        cardlist.insert(q2,b)
for j in range (0,51):
        q1=numpy.random.randint(0,len(cardlist))
        q2=numpy.random.randint(0,len(cardlist))
        b=cardlist[q1]
        del cardlist[q1]
        cardlist.insert(q2,b)
for j in range (0,51):
        q1=numpy.random.randint(0,len(cardlist))
        q2=numpy.random.randint(0,len(cardlist))
        b=cardlist[q1]
        del cardlist[q1]
        cardlist.insert(q2,b)
for j in range (0,51):
        q1=numpy.random.randint(0,len(cardlist))
        q2=numpy.random.randint(0,len(cardlist))
        b=cardlist[q1]
        del cardlist[q1]
        cardlist.insert(q2,b)
for j in range (0,51):
        q1=numpy.random.randint(0,len(cardlist))
        q2=numpy.random.randint(0,len(cardlist))
        b=cardlist[q1]
        del cardlist[q1]
        cardlist.insert(q2,b)
#assign value
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
#asign suit
diamonds=[]
for i in range(0,13):
    diamonds.append(i)

hearts=[]
for i in range(13,26):
    hearts.append(i)

clubs=[]
for i in range(26,39):
    clubs.append(i)

spades=[]
for i in range(39,52):
    spades.append(i)
#shuffling
for j in range (0,51):
    q1=numpy.random.randint(0,len(cardlist))
    q2=numpy.random.randint(0,len(cardlist))
    b=cardlist[q1]
    del cardlist[q1]
    cardlist.insert(q2,b)
for j in range (0,51):
    q1=numpy.random.randint(0,len(cardlist))
    q2=numpy.random.randint(0,len(cardlist))
    b=cardlist[q1]
    del cardlist[q1]
    cardlist.insert(q2,b)
for j in range (0,51):
    q1=numpy.random.randint(0,len(cardlist))
    q2=numpy.random.randint(0,len(cardlist))
    b=cardlist[q1]
    del cardlist[q1]
    cardlist.insert(q2,b)
for j in range (0,51):
    q1=numpy.random.randint(0,len(cardlist))
    q2=numpy.random.randint(0,len(cardlist))
    b=cardlist[q1]
    del cardlist[q1]
    cardlist.insert(q2,b)
for j in range (0,51):
    q1=numpy.random.randint(0,len(cardlist))
    q2=numpy.random.randint(0,len(cardlist))
    b=cardlist[q1]
    del cardlist[q1]
    cardlist.insert(q2,b)
for j in range (0,51):
    q1=numpy.random.randint(0,len(cardlist))
    q2=numpy.random.randint(0,len(cardlist))
    b=cardlist[q1]
    del cardlist[q1]
    cardlist.insert(q2,b)
for j in range (0,51):
    q1=numpy.random.randint(0,len(cardlist))
    q2=numpy.random.randint(0,len(cardlist))
    b=cardlist[q1]
    del cardlist[q1]
    cardlist.insert(q2,b)

#make card things
nplist=np
nplists=[[] for i in xrange(nplist)]
suitlistrank=[[] for i in xrange(nplist)]

#first Card
for i in range(0,np):
    nplists[i].append(cardlist[0])
    del cardlist[0]
#second card
for i in range(0,np):
    nplists[i].append(cardlist[0])
    del cardlist[0]

#sklansky-malmuth method: for this lower is better
smrank=[[] for i in xrange(nplist)]
for i in range(0,np):
    #if they are suited
    if ((nplists[i][0] in hearts) and(nplists[i][1] in hearts)) or ((nplists[i][0] in diamonds) and(nplists[i][1] in diamonds)) or ((nplists[i][0] in clubs) and(nplists[i][1] in clubs)) or ((nplists[i][0] in spades) and(nplists[i][1] in spades)):
        if (nplists[i][0] in aces) or (nplists[i][1] in aces):
            if (nplists[i][0] in kings) or (nplists[i][1] in kings):
                smrank[i]=1
            elif (nplists[i][0] in queens) or (nplists[i][1] in queens) or (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                smrank[i]=2
            elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                smrank[i]=3
            else:
                smrank[i]=5
        elif (nplists[i][0] in kings) or (nplists[i][1] in kings):
            if (nplists[i][0] in queens) or (nplists[i][1] in queens):
                smrank[i]=2
            elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                smrank[i]=3
            elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                smrank[i]=4
            elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                smrank[i]=6
            else:
                smrank[i]=7
        elif (nplists[i][0] in queens) or (nplists[i][1] in queens):
            if (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                smrank[i]=3
            elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                smrank[i]=4
            elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                smrank[i]=5
            elif (nplists[i][0] in eights) or (nplists[i][1] in eights):
                smrank[i]=7
            else:
                smrank[i]=9
        elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
            if (nplists[i][0] in tens) or (nplists[i][1] in tens):
                smrank[i]=3
            elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                smrank[i]=4
            elif (nplists[i][0] in eights) or (nplists[i][1] in eights):
                smrank[i]=6
            elif (nplists[i][0] in sevens) or (nplists[i][1] in sevens):
                smrank[i]=8
            else:
                smrank[i]=9
        elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
            if (nplists[i][0] in nines) or (nplists[i][1] in nines):
                smrank[i]=4
            elif (nplists[i][0] in eights) or (nplists[i][1] in eights):
                smrank[i]=5
            elif (nplists[i][0] in sevens) or (nplists[i][1] in sevens):
                smrank[i]=7
            else:
                smrank[i]=9
        elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
            if (nplists[i][0] in eights) or (nplists[i][1] in eights):
                smrank[i]=4
            elif (nplists[i][0] in sevens) or (nplists[i][1] in sevens):
                smrank[i]=5
            elif (nplists[i][0] in sixes) or (nplists[i][1] in sixes):
                smrank[i]=8
            else:
                smrank[i]=9
        elif (nplists[i][0] in eights) or (nplists[i][1] in eights):
            if (nplists[i][0] in sevens) or (nplists[i][1] in sevens):
                smrank[i]=5
            elif (nplists[i][0] in sixes) or (nplists[i][1] in sixes):
                smrank[i]=6
            elif (nplists[i][0] in fives) or (nplists[i][1] in fives):
                smrank[i]=8
            else:
                smrank[i]=9
        elif (nplists[i][0] in sevens) or (nplists[i][1] in sevens):
            if (nplists[i][0] in sixes) or (nplists[i][1] in sixes):
                smrank[i]=5
            elif (nplists[i][0] in fives) or (nplists[i][1] in fives):
                smrank[i]=6
            elif (nplists[i][0] in fours) or (nplists[i][1] in fours): 
                smrank[i]=8
            else:
                smrank[i]=9
        elif (nplists[i][0] in sixes) or (nplists[i][1] in sixes):
            if (nplists[i][0] in fives) or (nplists[i][1] in fives) or ((nplists[i][0] or nplist[i][1]) in fours):
                smrank[i]=7
            else:
                smrank[i]=9
        elif ((nplists[i][0] or nplists[i][1]) in fives):
            if ((nplists[i][0] or nplist[i][1]) in fours):
                smrank[i]=6
            elif ((nplists[i][0] or nplist[i][1]) in threes):
                smrank[i]=7
            else:
                smrank[i]=8
    #if they are not suited
    else:
        #if they are the same value:
        if ((nplists[i][0]-39) % 13)==((nplists[i][1]-39) % 13):
            if (nplists[i][0] in aces) or (nplists[i][0] in kings) or (nplists[i][0] in queens) or (nplists[i][0] in jacks):
                smrank[i]=1
            elif (nplists[i][0] in tens):
                smrank[i]=2 
            elif (nplists[i][0] in nines):
                smrank[i]=3
            elif (nplists[i][0] in eights):
                smrank[i]=4
            elif (nplists[i][0] in sevens):
                smrank[i]=5
            elif (nplists[i][0] in sixes) or (nplists[i][0] in fives):
                smrank[i]=6
            else:
                smrank[i]=7
        #if they are not the value:
        else: 
            if (nplists[i][0] in aces) or (nplists[i][1] in aces):
                if (nplists[i][0] in kings) or (nplists[i][1] in kings):
                    smrank[i]=2
                elif (nplists[i][0] in queens) or (nplists[i][1] in queens):
                    smrank[i]=3
                elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                    smrank[i]=4
                elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                    smrank[i]=6
                elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                    smrank[i]=8
                else:
                    smrank[i]=9
            elif (nplists[i][0] in kings) or (nplists[i][1] in kings):
                if (nplists[i][0] in queens) or (nplists[i][1] in queens):
                    smrank[i]=4
                elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                    smrank[i]=5
                elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                    smrank[i]=6
                elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                    smrank[i]=8
                else:
                    smrank[i]=9
            elif (nplists[i][0] in queens) or (nplists[i][1] in queens):
                if (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                    smrank[i]=5
                elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                    smrank[i]=6
                elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                    smrank[i]=8
                else:
                    smrank[i]=9
            elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                if (nplists[i][0] in tens) or (nplists[i][1] in tens):
                    smrank[i]=5
                elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                    smrank[i]=7
                elif (nplists[i][0] in eights) or (nplists[i][1] in eights):
                    smrank[i]=8
                else:
                    smrank[i]=9
            elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                if (nplists[i][0] in nines) or (nplists[i][1] in nines):
                    smrank[i]=7
                elif (nplists[i][0] in eights) or (nplists[i][1] in eights):
                    smrank[i]=8
                else:
                    smrank[i]=9
            elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                if (nplists[i][0] in eights) or (nplists[i][1] in eights):
                    smrank[i]=8
                else:
                    smrank[i]=7
            elif (nplists[i][0] in eights) or (nplists[i][1] in eights):
                if (nplists[i][0] in sevens) or (nplists[i][1] in sevens):
                    smrank[i]=8
                else:
                    smrank[i]=9
            elif (nplists[i][0] in sevens) or (nplists[i][1] in sevens):
                if (nplists[i][0] in sixes) or (nplists[i][1] in sixes):
                    smrank[i]=8
                else:
                    smrank[i]=9
            elif (nplists[i][0] in fives) or (nplists[i][1] in fives):
                if (nplists[i][0] in fours) or (nplists[i][1] in fours):
                    smrank[i]=8
                else:
                    smrank[i]=9
            else:
                smrank[i]=9
                    
                
#Chen Formula: for this higher is better 
chenrank=[[] for i in xrange(nplist)]

for i in range(0,np):
    #scoring highest card:
    if (nplists[i][0] in aces) or (nplists[i][1] in aces):
        chenrank[i]=10
    elif (nplists[i][0] in kings) or (nplists[i][1] in kings):
        chenrank[i]=8
    elif (nplists[i][0] in queens) or (nplists[i][1] in queens):
        chenrank[i]=7
    elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
        chenrank[i]=6
    elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
        chenrank[i]=5
    elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
        chenrank[i]=4.5
    elif (nplists[i][0] in eights) or (nplists[i][1] in eights):
        chenrank[i]=4
    elif (nplists[i][0] in sevens) or (nplists[i][1] in sevens):
        chenrank[i]=3.5
    elif (nplists[i][0] in sixes) or (nplists[i][1] in sixes):
        chenrank[i]=3
    elif (nplists[i][0] in fives) or (nplists[i][1] in fives):
        chenrank[i]=2.5
    elif (nplists[i][0] in fours) or (nplists[i][1] in fours):
        chenrank[i]=2
    elif (nplists[i][0] in threes) or (nplists[i][1] in threes):
        chenrank[i]=1.5
    else:
        chenrank[i]=1
                    
   
    if (nplists[i][0]-39) %13==(nplists[i][1]-39)%13:
        if (nplists[i][0] in twos):
            chenrank[i]=5
        else:
            chenrank[i]=chenrank[i]*2
    
    if ((nplists[i][0] and nplists[i][1]) in hearts) or ((nplists[i][0] and nplists[i][1]) in diamonds) or ((nplists[i][0] and nplists[i][1]) in clubs) or ((nplists[i][0] and nplists[i][1]) in spades):
        chenrank[i]=chenrank[i]+2
    
    if abs(((nplists[i][0]-39) %13)-((nplists[i][1]-39) %13))>4:
        chenrank[i]=chenrank[i]-5
    elif abs(((nplists[i][0]-39) %13)-((nplists[i][1]-39) %13))>3:
        chenrank[i]=chenrank[i]-4
    elif abs(((nplists[i][0]-39) %13)-((nplists[i][1]-39) %13))>2:
        chenrank[i]=chenrank[i]-2
    elif abs(((nplists[i][0]-39) %13)-((nplists[i][1]-39) %13))>1:
        chenrank[i]=chenrank[i]-1
  
    if ((nplists[i][0] and nplists[i][1]) not in aces) and ((nplists[i][0] and nplists[i][1]) not in kings) and ((nplists[i][0] and nplists[i][1]) not in queens):
        if abs(((nplists[i][0]-39) %13)-((nplists[i][1]-39) %13))==0 or abs(((nplists[i][0]-39) %13)-((nplists[i][1]-39) %13))==1:
            chenrank[i]=chenrank[i]+1
  
    chenrank[i]=math.ceil(chenrank[i])

    
         
    
#stats online play:
#higher number equals better
statsrank=[[] for i in xrange(nplist)]
for i in range(0,np):
    if ((nplists[i][0]-39) % 13)==((nplists[i][0]-39) % 13):
        if  ((nplists[i][0]-39) % 13) in aces:
            statsrank[i]=2.32
        elif ((nplists[i][0]-39) % 13) in kings:
            statsrank[i]=1.67
        elif  ((nplists[i][0]-39) % 13) in queens:
            statsrank[i]=1.22
        elif  ((nplists[i][0]-39) % 13) in jacks:
            statsrank[i]=.86
        elif  ((nplists[i][0]-39) % 13) in tens:
            statsrank[i]=.58
        elif  ((nplists[i][0]-39) % 13) in nines:
            statsrank[i]=.38
        elif  ((nplists[i][0]-39) % 13) in eights:
            statsrank[i]=.25
        elif  ((nplists[i][0]-39) % 13) in sevens:
            statsrank[i]=.16
        elif  ((nplists[i][0]-39) % 13) in sixes:
            statsrank[i]=.07
        elif  ((nplists[i][0]-39) % 13) in fives:
            statsrank[i]=.02
        else:
            statsrank[i]=0
    if ((nplists[i][0] in hearts) and (nplists[i][1] in hearts)) or ((nplists[i][0] in diamonds) and (nplists[i][1] in diamonds)) or ((nplists[i][0] in clubs) and (nplists[i][1] in clubs)) or ((nplists[i][0] in spades) and (nplists[i][1] in spades)):
        if (nplists[i][0] in aces) or (nplists[i][1] in aces):
            if (nplists[i][0] in kings) or (nplists[i][1] in kings):
                statsrank[i]=.77
            elif (nplists[i][0] in queens) or (nplists[i][1] in queens):
                statsrank[i]=.59
            elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                statsrank[i]=.43
            elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                statsrank[i]=.33
            elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                statsrank[i]=.18
            elif (nplists[i][0] in eights) or (nplists[i][1] in eights):
                statsrank[i]=.1
            elif (nplists[i][0] in sevens) or (nplists[i][1] in sevens):
                statsrank[i]=.08
            elif (nplists[i][0] in sixes) or (nplists[i][1] in sixes):
                statsrank[i]=.03
            elif (nplists[i][0] in fives) or (nplists[i][1] in fives):
                statsrank[i]=.08
            elif (nplists[i][0] in fours) or (nplists[i][1] in fours):
                statsrank[i]=.06
            elif (nplists[i][0] in threes) or (nplists[i][1] in threes):
                statsrank[i]=.02
            else:
                statsrank[i]=0
        elif (nplists[i][0] in kings) or (nplists[i][1] in kings):
            if (nplists[i][0] in queens) or (nplists[i][1] in queens):
                statsrank[i]=.39
            elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                statsrank[i]=.29
            elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                statsrank[i]=.2
            elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                statsrank[i]=.09
            elif (nplists[i][0] in eights) or (nplists[i][0] in eights):
                statsrank[i]=.01
            else:
                statsrank[i]=0
        elif (nplists[i][0] in queens) or (nplists[i][1] in queens):
            if (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                statsrank[i]=.23
            elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                statsrank[i]=.17
            elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                statsrank[i]=.06
            else:
                statsrank[i]=0
        elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
            if (nplists[i][0] in tens) or (nplists[i][1] in tens):
                statsrank[i]=.15
            elif (nplists[i][0] in nines) or (nplists[i][1] in nines):
                statsrank[i]=.04
            else:
                statsrank[i]=0
        elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
            if (nplists[i][0] in nines) or (nplists[i][1] in nines):
                statsrank[i]=.05
            else:
                statsrank[i]=0
    else:
        if (nplists[i][0] in aces) or (nplists[i][1] in aces):
            if (nplists[i][0] in kings) or (nplists[i][1] in kings):
                statsrank[i]=.51
            elif (nplists[i][0] in queens) or (nplists[i][1] in queens):
                statsrank[i]=.31
            elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                statsrank[i]=.19
            elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                statsrank[i]=.08
            else:
                statsrank[i]=0
        elif (nplists[i][0] in kings) or (nplists[i][1] in kings):
            if (nplists[i][0] in queens) or (nplists[i][1] in queens):
                statsrank[i]=.16
            elif (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                statsrank[i]=.07
            elif (nplists[i][0] in tens) or (nplists[i][1] in tens):
                statsrank[i]=.01
            else:
                statsrank[i]=0
        elif (nplists[i][0] in queens) or (nplists[i][1] in queens):
            if (nplists[i][0] in jacks) or (nplists[i][1] in jacks):
                statsrank[i]=.03
            else:
                statsrank[i]=0
        else:
            statsrank[i]=0
del cardlist[0]
#the flop
floplist=[[] for i in xrange(3)]
for i in range(0,3):
    floplist[i].append(cardlist[0])
    del cardlist[0]

#adding flop to cards
for i in range(0,np):
    nplists[i].append(floplist[0][0])
    nplists[i].append(floplist[1][0])
    nplists[i].append(floplist[2][0])


#converted nplists for rank:
cnplists=[[0,0,0,0,0,0] for i in xrange(nplist)]
for i in range(0,np):
    for j in range(0,6):
        cnplists[i][j]=(nplists[i][j]-39)%13
#sort cnplists
for i in range(0,np):
    cnplists[i].sort()

#converted nplists for suit
crnplists=[[0,0,0,0,0] for i in xrange(nplist)]
for i in range(0,np):
    for j in range(0,5):
        if nplists[i][j] in diamonds:
            crnplists[i][j]=0
        elif nplists[i][j] in hearts:
            crnplists[i][j]=1
        elif nplists[i][j] in clubs:
            crnplists[i][j]=2
        else:
            crnplists[i][j]=3
    
#ranking cards after flop:
ranklist=[[0,0,0,0,0,0,0,0,0,0,0,0,0] for i in xrange(nplist)]

for i in range(0,np):
    a=crnplists[i]
    counter=collections.Counter(a)
    #flush or not
    if max(counter.values())==5:
        ranklist[i][0]=1
    else:
        ranklist[i][1]=0
    a=cnplists[i]
    counter=collections.Counter(a)
    #4 of  a kind or not
    if max(counter.values())==4:
        ranklist[i][1]=1
    else:
        ranklist[i][1]=0
    
    #straight or not
    if cnplists[i][0]==0 or cnplists[i][1]==0 or cnplists[i][2]==0 or cnplists[i][3]==0 or cnplists[i][4]==0:
        if cnplists[i][0]==12 or cnplists[i][1]==12 or cnplists[i][2]==12 or cnplists[i][3]==12 or cnplists[i][4]==12:
            if cnplists[i][0]==11 or cnplists[i][1]==11 or cnplists[i][2]==11 or cnplists[i][3]==11 or cnplists[i][4]==11:
                if cnplists[i][0]==10 or cnplists[i][1]==10 or cnplists[i][2]==10 or cnplists[i][3]==10 or cnplists[i][4]==10:
                    if cnplists[i][0]==9 or cnplists[i][1]==9 or cnplists[i][2]==9 or cnplists[i][3]==9 or cnplists[i][4]==9:
                        ranklist[i][2]=1
        else:
            if max(counter.values())==1:
                if max(cnplists[i])==min(cnplists[i])+4:
                    ranklist[i][2]=1
    else:
        if max(counter.values())==1:
            if max(cnplists[i])==min(cnplists[i])+4:
                ranklist[i][2]=1
            else:
                ranklist[i][2]=0
        else:
            ranklist[i][2]=0
    #full house or not
    if counter.values()==[3,2]:
        ranklist[i][3]=1
    else:
        ranklist[i][3]=0
    # 3 of  kind
    if (counter.values()==[3,1,1]):
        ranklist[i][4]=1
    else:
        ranklist[i][4]=0
    # 2 pair
    if counter.values()==[2,2,1]:
        ranklist[i][5]=1
    else:
        ranklist[i][5]=0
    # pair:
    if counter.values()==[2,1,1,1]:
        ranklist[i][6]=1
    else:
        ranklist[i][6]=0
    #high card
    ranklist[i][7]=min(cnplists[i])
    #second highest card
    ranklist[i][8]=cnplists[i][1]
    #middle card
    ranklist[i][9]=cnplists[i][2]
    #second to last
    ranklist[i][10]=cnplists[i][3]
    #lowest card
    ranklist[i][11]=cnplists[i][4]
    a=cnplists[i]
    def most_common(a):
        return max(set(a), key=a.count)
    if counter.values()==[1,1,1,1,1]:
        ranklist[i][12]=-1
    else:
        ranklist[i][12]=most_common(a)

# creating the actual rank for each player
# higher is better
frank=[0 for i in xrange(nplist)]
flushadd=6
fourkind=8
straight=6
fullhouse=5
threekind=4
twopair=3
pair=2
topthirdh=1.5 #multiplication factor, face card
topthirdhadd=2
middlethirdh=1#multiplication factor, 6-10
middlethirdhadd=0
bottomthirdh=.5#2-6
bottomthirdhadd=-1
threeofsuit=1
fourofsuit=3



for i in range(0,np):
    a=crnplists[i]
    if ranklist[i][0]==1:
        frank[i]=frank[i]+flushadd
    if ranklist[i][1]==1:
        frank[i]=frank[i]+fourkind
    if ranklist[i][2]==1:
        frank[i]=frank[i]+straight
    if ranklist[i][3]==1:
        frank[i]=frank[i]+fullhouse
    if ranklist[i][4]==1:
        frank[i]=frank[i]+threekind
    if ranklist[i][5]==1:
        frank[i]=frank[i]+twopair
    if ranklist[i][6]==1:
        frank[i]=frank[i]+pair
    if ranklist[i][7]<4:
        frank[i]=frank[i]*topthirdh+topthirdhadd
    elif ranklist[i][7]<5:
        frank[i]=frank[i]*middlethirdh+middlethirdhadd
    else:
        frank[i]=frank[i]*bottomthirdh+bottomthirdhadd
    counter=collections.Counter(a)
    if counter.values()==[3,1,1]:
        frank[i]=frank[i]+threeofsuit
    elif counter.values()==[4,1]:
        frank[i]=frank[i]+fourofsuit
    
#turn
for i in range(0,1):
    floplist[i].append(cardlist[0])
    del cardlist[0]
    
#adding turn cards
for i in range(0,np):
    nplists[i].append(floplist[0][0])
    

#converted nplists for rank:
cnplists=[[0,0,0,0,0,0] for i in xrange(nplist)]
for i in range(0,np):
    for j in range(0,5):
        cnplists[i][j]=(nplists[i][j]-39)%13
#sort cnplists
for i in range(0,np):
    cnplists[i].sort()

#converted nplists for suit
crnplists=[[0,0,0,0,0,0] for i in xrange(6)]
for i in range(0,np):
    for j in range(0,6):
        if nplists[i][j] in diamonds:
            crnplists[i][j]=0
        elif nplists[i][j] in hearts:
            crnplists[i][j]=1
        elif nplists[i][j] in clubs:
            crnplists[i][j]=2
        else:
            crnplists[i][j]=3
        
        

ranklist=[[0,0,0,0,0,0,0,0,0,0,0,0,0] for i in xrange(nplist)]      
trank=[0,0,0,0,0]      
for i in range(0,np):
    for j in range(0,6):
        t_trank=0
        holdsuit=crnplists[i][j]
        holdrank=cnplists[i][j]
        holdlist=nplists[i][j] 
        del crnplists[i][j]
        del cnplists[i][j]
        del nplists[i][j]
        #find flush
        a=crnplists[i]
        counter=collections.Counter(a)
        if counter.values()==5:
            ranklist[i][0]=1
        else:
            ranklist[i][0]=0
        #4 of a  kind
        a=cnplists[i]
        counter=collections.Counter(a)
        if counter.values()==[4,1]:
            ranklist[i][1]=1
        else:
            ranklist[i][1]=0
        #straight
        if counter.values()==[1,1,1,1,1]:
            ranklist[i][3]=0
            ranklist[i][4]=0
            ranklist[i][5]=0
            ranklist[i][6]=0
            if cnplists[i][0]==0 and cnplists[i][1]==9 and cnplists[i][2]==10 and cnplists[i][3]==11 and cnplists[i][4]==12:
                ranklist[i][2]=1
            else:
                if abs(cnplists[i][0]-cnplists[i][4])==4:
                    ranklist[i][2]=1
                else:
                    ranklist[i][2]=0
        else:
            ranklist[i][2]=0
        if counter.values()==[3,2]:
            ranklist[i][3]=1
        else:
            ranklist[i][3]=0
        if counter.values()==[3,1,1]:
            ranklist[i][4]=1
        else:
            ranklist[i][4]=0
        if counter.values()==[2,2,1]:
            ranklist[i][5]=1
        else:
            ranklist[i][5]=0
        if counter.values()==[2,1,1,1]:
            ranklist[i][6]=1
        else:
            ranklist[i][6]=0
        ranklist[i][7]=cnplists[i][0]
        ranklist[i][8]=cnplists[i][1]
        ranklist[i][9]=cnplists[i][2]
        ranklist[i][10]=cnplists[i][3]
        ranklist[i][11]=cnplists[i][4]
        def most_common(a):
            return max(set(a), key=a.count)
        if counter.values()==[1,1,1,1,1]:
            ranklist[i][12]=-1
        else:
            ranklist[i][12]=most_common(a)
        
        #temp  rank:
        if ranklist[i][0]==1:
            t_trank=t_trank+flushadd
        if ranklist[i][1]==1:
            t_trank=t_trank+fourkind
        if ranklist[2]==1:
            t_trank=t_trank+straight
        if ranklist[i][3]==1:
            t_trank=t_trank+fullhouse
        if ranklist[i][4]==1:
            t_trank=t_trank+threeking
        if ranklist[i][5]==1:
            t_trank=t_trank+twopair
        if ranklist[i][6]==1:
            t_trank=t_trank+pair
        if ranklist[i][7] in [0,1,2,3]:
            t_trank=t_trank*topthirdh
            t_trank=t_trank+topthirdhadd
        elif ranklist[i][7] in [4,5,6,7,8]:
            t_trank=t_trank*middlethirdh
            t_trank=t_trank+middlethirdhadd
        else:
            t_trank=t_trank*bottomthirdh
            t_trank=t_trank+bottomthirdhadd
        a=crnplists[i]
        counter=collections.Counter(a)
        if counter.values()==[3,1,1]:
            t_trank=t_trank+threeofsuit
        elif counter.values()==[4,1]:
            t_trank==t_trank+fourofsuit
            
        
        #set actual rank:
        if t_trank>trank[i]:
            trank[i]=t_trank
        
            
        crnplists[i].insert(j,holdsuit)
        cnplists[i].insert(j,holdrank)
        nplists[i].insert(j,holdlist)
#river
for i in range(0,1):
    floplist[i].append(cardlist[0])
    del cardlist[0]
    
#adding river cards
for i in range(0,np):
    nplists[i].append(floplist[0][0])


#converted nplists for rank:
cnplists=[[0,0,0,0,0,0] for i in xrange(nplist)]
for i in range(0,np):
    for j in range(0,7):
        cnplists[i][j]=(nplists[i][j]-39)%13
#sort cnplists
for i in range(0,np):
    cnplists[i].sort()

#converted nplists for suit
crnplists=[[0,0,0,0,0,0,0] for i in xrange(6)]
for i in range(0,np):
    for j in range(0,7):
        if nplists[i][j] in diamonds:
            crnplists[i][j]=0
        elif nplists[i][j] in hearts:
            crnplists[i][j]=1
        elif nplists[i][j] in clubs:
            crnplists[i][j]=2
        else:
            crnplists[i][j]=3
