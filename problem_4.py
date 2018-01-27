# -*- coding:utf-8 -*-
import math

arr = []

for i in range(100,1000):
    for j in range(100,1000):
        x = i * j
        x = list(str(x))
        #print(x)
        for k in range(len(x)//2):
            if x[k] != x[-1-k]:
                break
            if(k == (len(x)//2) - 1):
                arr.append(int(''.join(x)))

print(arr)
print(max(arr))
