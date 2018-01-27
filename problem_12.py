# -*- coding:utf-8 -*-
import sys

def mktriangle(k):
    tri = [0]
    sum = 0
    for i in range(k):
        sum += i
        tri.append(sum)
    return tri


def mkdiv(M):
    arr = [0]*M
    for i in range(1,M):
        for j in range(1,M):
            if j % i == 0:
                arr[j] += 1
    return arr


M = 100000
a = mkdiv(M)
t = mktriangle(100)

for i in range(len(a)):
    if a[i] >= 500:
        print(i)
