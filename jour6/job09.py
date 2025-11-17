L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def trouveMax() :
    max = L[0]
    for i in L :
        if i > max :
            max = i
    return max

def trouveMin() :
    min = L[0]
    for i in L :
        if i < min :
            min = i
    return min

le_max = trouveMax()
le_min = trouveMin()
print(f"La valeur max est : {le_max}")
print(f"La valeur min est : {le_min}")