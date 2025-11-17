def arrondie(l) :
    compt = 0
    for i in l :
        if i % 5 >= 3 :
            resultat = 5 - (i % 5)
            l[compt] = i + resultat
        compt += 1
    return l


L = [8, 24, 48, 2, 16, 67, 48, 21, 90, 96, 74, 22]
print(arrondie(L))
