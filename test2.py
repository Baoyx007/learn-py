from collections import Iterable
import os

__author__ = 'haven'

L = []
for x in range(100):
    if x % 2 != 0:
        L.append(x)

# print(L)

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print(L[0:3])
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# print(L[4:])

# print( isinstance(L,Iterable))
# l = [d for d in os.listdir('.')]

# print(l)
def tri():
    l = [1]
    while True :
        yield(l)
        last_item =1
        new_line = [1]
        for item in l[1:]:
            new_line.append(item + last_item)
            last_item = item
        if last_item==1 :
            new_line.append(1)
        l = new_line

def tri2():
    l = [1,1]
    while True :
        l =[1]+  [l[i]+l[i-1] for i in range(1,len(l))]+[1]
        yield (l)

n=0
for t in tri2():
    print(t)
    n = n + 1
    if n == 10:
        break
# tri2()
