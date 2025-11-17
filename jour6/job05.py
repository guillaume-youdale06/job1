from random import *

L = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
print(L[1])

def somme(L) :
    L[3] = L[2] + L[4]
    print(L)

somme(L)
print(L[len(L) - 1])