from pylab import *
from operator import itemgetter
Aaron_McGrath=["Connectedness","Positivity", "Adaptability","Developer","Restorative"]
Brady_Peterson=["Responsablity","Achiever","Intellection","Input","Learner"]
Carl_Peaslee=["Futuristic","Ideation","Self-Assurance","Strategic","Intellection"]
Elizabeth_Cook=["Individualization","Arranger","Relator","Restorative","Responsibility"]
Evan_Kimlinger=["Command","Focus","Significance","Analytical","Activator"]
Henery_Andre=["Intellection","Empathy","Connectedness","Input","Futuristic"]
Jermey_Hjelmeland=["Adaptability","Ideation","Competition","Strategic","Activator"]
Joette_Poehler=["Input","Learner","Achiever","Positivity","Strategic"]
Kenzie_Bultema=["Strategic","Relator","Learner","Restorative","Empathy"]
Mark_Rothermal=["Context","Individualization","Stategic","Ideation","Intellection"]
Mathew_Keymer=["Empathy","Consistency","Harmony","Adaptability","Input"]
Micheal_Carlson=["Strategic","Ideation","Adaptability","Learner","Individualization"]
Mike_Elliot=["Futuristic","Competition","Activator","Focus","Achiever"]
Miles_Johnson=["Ideation","Input","Deliberative","Intellection","Analytical"]
Neil_Skupa=["Futuristic","Learner","Achiever","Analytical","Significance"]
Roman_Hiebert=["Futuristic","Analytical","Maximizer","Strategic","Achiever"]
Shelly_Wang=["Futuristic","Learner","Intellection","Input","Restorative"]
Thomas_Chester=["Learner","Consistency","Ideation","Intellection","Relator"]
Tracey_van_Haaften=["Intellection","Ideation","Restorative","Futuristic","Adaptability"]
William_Harrison=["Strategic","Futuristic","Learner","Ideation","Restorative"]

AllName=["Aaron_McGrath","Brady_Peterson","Carl_Peaslee", "Elizabeth_Cook","Evan_Kimlinger","Henery_Andre","Jermey_Hjelmeland","Joette_Poehler","Kenzie_Bultema","Mark_Rothermal","Mathew_Keymer","Micheal_Carlson","Mike_Elliot","Miles_Johnson","Neil_Skupa","Roman_Hiebert","Shelly_Wang","Thomas_Chester","Tracey_van_Haaften","William_Harrison" ]
AllNameIndex=[["Aaron_McGrath",0],["Brady_Peterson",0],["Carl_Peaslee",0],["Elizabeth_Cook",0],["Evan_Kimlinger",0],["Henery_Andre",0],["Jermey_Hjelmeland",0],["Joette_Poehler",0],["Kenzie_Bultema",0],["Mark_Rothermal",0],["Mathew_Keymer",0],["Micheal_Carlson",0],["Mike_Elliot",0],["Miles_Johnson",0],["Neil_Skupa",0],["Roman_Hiebert",0],["Shelly_Wang",0],["Thomas_Chester",0],["Tracey_van_Haaften",0],["William_Harrison",0]]
All=[Aaron_McGrath,Brady_Peterson,Carl_Peaslee,Elizabeth_Cook,Evan_Kimlinger,Henery_Andre,Jermey_Hjelmeland, Joette_Poehler, Kenzie_Bultema, Mathew_Keymer, Micheal_Carlson, Mike_Elliot, Miles_Johnson, Neil_Skupa, Roman_Hiebert, Shelly_Wang, Thomas_Chester, Tracey_van_Haaften, William_Harrison]



# running with same relation
oneRelationList=[]
for i in range(0,19):
    oneRelationList.append([])


for q in range(0,19): #defines which person is being checked
    for k in range(0,5): # defines which attribute is being checked
        for i in range(1,19): # defines which person it is being checked against
            for j in range(0,5): #defines which attribute is being checked against
               if All[q][k]==All[i][j]:
                  if k==j:
                      oneRelationList[q].append(1)
                  elif abs(k-j)==1:
                      oneRelationList[q].append(1)
                  elif abs(k-j)==2:
                      oneRelationList[q].append(1) 
                  elif abs(k-j)==3:
                      oneRelationList[q].append(1) 
                  elif abs(k-j)==5:
                      oneRelationList[q].append(1)     
                        
# running with addative  one up relation

PlusOneRelationList=[]
for i in range(0,19):
    PlusOneRelationList.append([])

for q in range(0,19): #defines which person is being checked
    for k in range(0,5): # defines which attribute is being checked
        for i in range(1,19): # defines which person it is being checked against
            for j in range(0,5): #defines which attribute is being checked against
               if All[q][k]==All[i][j]:
                  if k==j:
                      PlusOneRelationList[q].append(5)
                  elif abs(k-j)==1:
                      PlusOneRelationList[q].append(4)
                  elif abs(k-j)==2:
                      PlusOneRelationList[q].append(3) 
                  elif abs(k-j)==3:
                      PlusOneRelationList[q].append(2) 
                  elif abs(k-j)==5:
                      PlusOneRelationList[q].append(1)       

#runnning with addative 2 up relation
PlusTwoRelationList=[]
for i in range(0,19):
    PlusTwoRelationList.append([])

for q in range(0,19): #defines which person is being checked
    for k in range(0,5): # defines which attribute is being checked
        for i in range(1,19): # defines which person it is being checked against
            for j in range(0,5): #defines which attribute is being checked against
               if All[q][k]==All[i][j]:
                  if k==j:
                      PlusTwoRelationList[q].append(9)
                  elif abs(k-j)==1:
                      PlusTwoRelationList[q].append(7)
                  elif abs(k-j)==2:
                      PlusTwoRelationList[q].append(5) 
                  elif abs(k-j)==3:
                      PlusTwoRelationList[q].append(3) 
                  elif abs(k-j)==5:
                      PlusTwoRelationList[q].append(1) 

#runnning with addative 10 up relation
PlusTenRelationList=[]
for i in range(0,19):
    PlusTenRelationList.append([])

for q in range(0,19): #defines which person is being checked
    for k in range(0,5): # defines which attribute is being checked
        for i in range(1,19): # defines which person it is being checked against
            for j in range(0,5): #defines which attribute is being checked against
               if All[q][k]==All[i][j]:
                  if k==j:
                      PlusTenRelationList[q].append(41)
                  elif abs(k-j)==1:
                      PlusTenRelationList[q].append(31)
                  elif abs(k-j)==2:
                      PlusTenRelationList[q].append(21) 
                  elif abs(k-j)==3:
                      PlusTenRelationList[q].append(11) 
                  elif abs(k-j)==5:
                      PlusTenRelationList[q].append(1)           

#x2 up relation
X2RelationList=[]
for i in range(0,19):
    X2RelationList.append([])

for q in range(0,19): #defines which person is being checked
    for k in range(0,5): # defines which attribute is being checked
        for i in range(1,19): # defines which person it is being checked against
            for j in range(0,5): #defines which attribute is being checked against
               if All[q][k]==All[i][j]:
                  if k==j:
                      X2RelationList[q].append(16)
                  elif abs(k-j)==1:
                      X2RelationList[q].append(8)
                  elif abs(k-j)==2:
                      X2RelationList[q].append(4) 
                  elif abs(k-j)==3:
                      X2RelationList[q].append(2) 
                  elif abs(k-j)==5:
                      X2RelationList[q].append(1)     
#x5 up relation
X5RelationList=[]
for i in range(0,19):
    X5RelationList.append([])

for q in range(0,19): #defines which person is being checked
    for k in range(0,5): # defines which attribute is being checked
        for i in range(1,19): # defines which person it is being checked against
            for j in range(0,5): #defines which attribute is being checked against
               if All[q][k]==All[i][j]:
                  if k==j:
                      X5RelationList[q].append(625)
                  elif abs(k-j)==1:
                      X5RelationList[q].append(125)
                  elif abs(k-j)==2:
                      X5RelationList[q].append(25) 
                  elif abs(k-j)==3:
                      X5RelationList[q].append(5) 
                  elif abs(k-j)==5:
                      X5RelationList[q].append(1)           
#x10 up relation
X10RelationList=[]
for i in range(0,19):
    X10RelationList.append([])

for q in range(0,19): #defines which person is being checked
    for k in range(0,5): # defines which attribute is being checked
        for i in range(1,19): # defines which person it is being checked against
            for j in range(0,5): #defines which attribute is being checked against
               if All[q][k]==All[i][j]:
                  if k==j:
                      X10RelationList[q].append(10000)
                  elif abs(k-j)==1:
                      X10RelationList[q].append(1000)
                  elif abs(k-j)==2:
                      X10RelationList[q].append(100) 
                  elif abs(k-j)==3:
                      X10RelationList[q].append(10) 
                  elif abs(k-j)==5:
                      X10RelationList[q].append(1)           

                                                        
newOneRelationList=[]                          
for i in range(0,len(oneRelationList)):
    x=sum(oneRelationList[i])
    x1=[i,x]
    newOneRelationList.append(x1) 

newPlusOneRelationList=[]                          
for i in range(0,len(PlusOneRelationList)):
    x=sum(PlusOneRelationList[i])
    x1=[i,x]
    newPlusOneRelationList.append(x1) 
     
newPlusTwoRelationList=[]                          
for i in range(0,len(PlusTwoRelationList)):
    x=sum(PlusTwoRelationList[i])
    x1=[i,x]
    newPlusTwoRelationList.append(x1) 

newPlusTenRelationList=[]                          
for i in range(0,len(PlusTenRelationList)):
    x=sum(PlusTenRelationList[i])
    x1=[i,x]
    newPlusTenRelationList.append(x1) 
                                                                        
newX2RelationList=[]                          
for i in range(0,len(X2RelationList)):
    x=sum(X2RelationList[i])
    x1=[i,x]
    newX2RelationList.append(x1) 

newX5RelationList=[]                          
for i in range(0,len(X5RelationList)):
    x=sum(X5RelationList[i])
    x1=[i,x]
    newX5RelationList.append(x1)    
newX10RelationList=[]                          
for i in range(0,len(X10RelationList)):
    x=sum(X10RelationList[i])
    x1=[i,x]
    newX10RelationList.append(x1) 

newNewX10RelationList=[]
for i in range(0,len(newX10RelationList)) :
    newNewX10RelationList.append(newX10RelationList)


newOneRelationList=sorted(newOneRelationList, key=itemgetter(1))
newX10RelationList=sorted(newX10RelationList, key=itemgetter(1))
newPlusTwoRelationList=sorted(newPlusTwoRelationList, key=itemgetter(1))
newPlusTenRelationList=sorted(newPlusTenRelationList, key=itemgetter(1))
newX2RelationList=sorted(newX2RelationList, key=itemgetter(1))
newNewX10RelationList=sorted(newNewX10RelationList, key=itemgetter(1))


print AllNameIndex

#for i in range(0,len(newX10RelationList)):
#   print AllName[newOneRelationList[i][0]], "      ",  AllName[newPlusOneRelationList[i][0]], "      ", 

