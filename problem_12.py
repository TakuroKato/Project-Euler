# -*- coding:utf-8 -*-
import sys
import math
from tqdm import tqdm

def mktriangle(k):
    tri = []
    sum = 0
    for i in range(1,k):
        sum += i
        tri.append(sum)
    return tri

def getNumberOfFactor(n):
    count = 0
    for i in range(1, int(math.sqrt(n) + 1e-9)+1):
        if n % i == 0:
            count += 1
            if n != i**2:
                count += 1
    return count

M = int(input())
t = mktriangle(M)

x = []
for i in tqdm(range(len(t))):
    x.append(getNumberOfFactor(t[i]))
    if(x[-1] >= 500):
        print(t[i])
print(max(x))
print(getNumberOfFactor(76576500))
