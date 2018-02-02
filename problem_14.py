# -*- coding:utf-8 -*-
from tqdm import tqdm
import numpy
def collatz(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return (3 * n) + 1

def collatz_len(a):
    count = 0
    while(True):
        if a == 1:
            count += 1
            break
        else:
            a = collatz(a)
            count += 1
    return count
    
x = []
for i in tqdm(range(1,10**6)):
    x.append(collatz_len(i))
print(numpy.argmax(x)+1)
