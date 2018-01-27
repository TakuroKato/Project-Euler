# -*- coding:utf-8 -*-

x = 1
for i in range(1,101):
    x *= i
print(x)

x = list(str(x))
x = map(int,x)

print(sum(x))
