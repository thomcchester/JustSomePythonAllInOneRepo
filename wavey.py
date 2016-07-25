from wavecompressionone import a1
import time
start_time=time.time()
hold=[]
for i in range(0,4294967296):
    holder=bin(i)
    hold.append(holder)
    start_time=time.time()
elapsed_time=time.time()-start_time
print len(hold)
print elapsed_time
