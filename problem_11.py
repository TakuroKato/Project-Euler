# -*- coding:utf-8 -*-
import sys

arr = [[0] * 20]* 20
for i in range(20):
    arr[i] = list(map(int,input().split()))

m = 0

sum = 0
sums = [0]
count = 0
for i in range(20):
    for j in range(20):
        try:
            if (i + 3 < 20 and j + 3 < 20):
                sum = arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3]
                sums.append(sum)
            else:
                pass
        except:
            pass
        count += 1
for i in range(20):
    for j in range(20):
        try:
            if (i + 3 < 20 and j + 3 < 20):
                sum = arr[i][j] * arr[i+1][j] * arr[i+2][j] * arr[i+3][j]
                sums.append(sum)
            else:
                pass
        except:
            pass
        count += 1
for i in range(20):
    for j in range(20):
        try:
            if (i + 3 < 20 and j + 3 < 20):
                sum = arr[i][j] * arr[i+1][j+1] * arr[i+2][j+2] * arr[i+3][j+3]
                sums.append(sum)
            else:
                pass
        except:
            pass
        count += 1

for i in range(20):
    for j in range(20):
        try:
            if (i + 3 < 20 and j + 3 < 20):
                sum = arr[i][j] * arr[i+1][j-1] * arr[i+2][j-2] * arr[i+3][j-3]
                sums.append(sum)
            else:
                pass
        except:
            pass
        count += 1
        
print(arr)
print(max(sums))
print(count)
