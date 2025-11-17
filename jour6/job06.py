from random import *

L = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
print(L)
tampon = L[0]
L[0] = L[len(L) - 1]
L[len(L) - 1] = tampon
print(L)
