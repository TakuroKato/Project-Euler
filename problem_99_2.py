# -*- coding:utf-8 -*-
import math

def pow(x,n):
    if (n == 0):
        return 1
    if (n % 2 == 0):
        return pow(x * x, n / 2)
    else:
        return x * pow(x, n - 1)

x = 0
y = 0
m_max = 1
n_max = 1
l = 0
for i in range(1000):
    x,y = map(int,input().split(','))
    if y*math.log(x,10) > n_max*math.log(m_max,10):
        m_max = x
        n_max = y
        l = i+1
print(m_max,n_max,l)
