# -*- coding:utf-8 -*-

def dig(a):
    a = list(str(a))
    return len(a)

f1 = 1
f2 = 1
f3 = 0
for i in range(10**12):    
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    #print(f3)
    if dig(f3) == 1000:
        print(i)
        print(f3)
        break
