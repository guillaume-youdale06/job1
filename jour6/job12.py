L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

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

print(L)
print(tri(L))