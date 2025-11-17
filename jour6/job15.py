L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def compte(l) :
    compt = 0
    for i in l :
        compt += 1
    return compt

def supprimeValeur(e, l) :
    for i in range(compte(l)) :
        if l[i] == e :
            del l[i]
            break

def trouveMin(l) :
    min = l[0]
    for i in l :
        if i < min :
            min = i
    return min

def ajouteValeur(e, l) :
    resultat = [e]
    l += resultat

def tri(l) :
    liste = l[:]
    liste_triee = []
    while compte(liste) > 0:
        m = trouveMin(liste)
        ajouteValeur(m, liste_triee)
        supprimeValeur(m, liste)
    return liste_triee

def arrondi(l) :
    compt = 0
    for i in l :
        l[compt] = int(i)
        compt += 1
    return l

liste_final = arrondi(L)
print(liste_final)
liste_final = tri(liste_final)
print(liste_final)


print(L)
print(tri(L))