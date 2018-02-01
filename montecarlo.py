# -*- coding:utf-8 -*-
import random,math,sys
from tqdm import tqdm

print(" *** pi-calculator ***\n"+"input the number of iteration : ",end = '')
n = int(input())
n *= 2

print("\ncalculating...")
count = 0
for i in tqdm(range(n)):
    if math.sqrt(random.random()**2 + random.random()**2) <= 1:
        count += 1
res = (4*count)/n
        
print("\n"+"calculation finished.")
print("result :", res)
print("accuracy : ",100-(abs(math.pi - res)/math.pi)*100,"%",sep='')
