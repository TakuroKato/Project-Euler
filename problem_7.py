# -*- coding:utf-8 -*-

arr = [2,3]

for i in range(arr[-1],10000000):
    flag = 0
    for j in range(len(arr)):
        if i % arr[j] == 0:
            flag = 1
            break
    if flag == 0:
        arr.append(i)
        print(i, end = ' ')
    if len(arr) == 10001:
        break
print('')
