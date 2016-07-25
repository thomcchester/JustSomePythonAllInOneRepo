
icards=[]
for i in range(0,12):
    for j in range(i+1,26):
        for k in range((j-39)%13,39):
            for l in range((k-39)%13,52):
                for h in range((l-39)%13,52):
                    if ((k-39)%13>=(j-39)%13) and j!=k:
                        if ((l-39)%13>=(k-39)%13) and l!=k:
                            if ((h-39)%13>=(l-39)%13) and h!=l:
                                icards.append([i,j,k,l,h])
                        
tcards=[]
for j in range(0,4):
    for k in range(j+1,5):
        for i in range(0,len(icards)):
            tcards.append([j,k,icards[i][0],icards[i][1],icards[i][2],icards[i][3],icards[i][4]])
for j in range(0,len(tcards)):
    f=open('tcards100.txt','a')
    g=tcards[j]
    k=str(g)
    f.write(k)
    f.write("\n")
    f.close()
