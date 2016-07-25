from keyfilecompression import filehold
import numpy as np
import collections
listo=[]
for i in range(0,100000):
    rando=''
    for i in range(0,255):
        rando+=str(np.random.randint(0,2)) 
    def longRunZeros(s):
        big = 0
        curr = 0
        for c in s:
            if c == '0':
                curr += 1
            else:
                if curr > big:
                    big = curr
                curr = 0
        if curr > big:
            big = curr
        return big
    def longRunOnes(s):
        big = 0
        curr = 0
        for c in s:
            if c == '1':
                curr += 1
            else:
                if curr > big:
                    big = curr
                curr = 0
        if curr > big:
            big = curr
        return big
    listo.append(longRunZeros(rando))
    listo.append(longRunOnes(rando))

print collections.Counter(listo).most_common(1)
