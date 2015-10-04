from collections import Iterable
import os
__author__ = 'haven'

L=[]
for x in range(100):
   if  x%2!=0:
      L.append(x)

# print(L)

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print(L[0:3])
L=[1,2,3,4,5,6,7,8,9]
# print(L[4:])

# print( isinstance(L,Iterable))
l = [d for d in os.listdir('.')]

print(l)