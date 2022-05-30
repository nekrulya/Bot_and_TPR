import numpy as np
import random

a = [[0]*4 for i in range(4)]

lowerBound = 1
upperBound = 100
for i in range(4):
    for j in range(4):
        a[i][j] = random.randint(lowerBound, upperBound)
    print(a[i])
max = 0
max_mass = []

for j in range (len(a[i])):
    max = a[i][0]
    for i in range (len(a)):
        if a[i][j] > max:
            max = a[i][j]
    print(max)
    max_mass.append(max)
print(max_mass)
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = max_mass[j] - a[i][j]
#print(max)
print(a)