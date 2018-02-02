# -*- coding:utf-8 -*-
import math

def pow(x,n):
    if (n == 0):
        return 1
    if (n % 2 == 0):
        return pow(x * x, n / 2)
    else:
        return x * pow(x, n - 1)

m = []
n = []
m_m = 0
n_m = 0
x = 0
y = 0
m_max = 0
n_max = 0
n_max_l = 0
for i in range(1000):
    x,y = map(int,input().split(','))
    if x > m_m and y > n_m:
        m_m = x
        n_m = y
    if x > m_max:
        m_max = x
    if y > n_max:
        n_max = y
        n_max_l = i+1
for i in range(1000):
    x,y = map(int,input().split(','))
    if x > m_m:
        m.append(x)
        n.append(y)
    elif y > n_m:
        m.append(x)
        n.append(y)

print(m,n,len(m),len(n),m_m,n_m,m_max,n_max,n_max_l)

