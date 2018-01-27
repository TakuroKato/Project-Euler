# -*- coding:utf-8 -*-

k = 1
for i in range(1000):
    k *= 2

print(k)

k = list(str(k))
k = map(int,k)
print(sum(k))
