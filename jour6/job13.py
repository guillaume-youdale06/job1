L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

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

def ajouteValeur(e, l) :
    resultat = [e]
    l += resultat

def suppDoublons(l) :
    liste_finale = []
    for i in l :
        present = False
        for y in liste_finale :
            if i == y :
                present = True
                break
        if not present :
            ajouteValeur(i, liste_finale)
    return liste_finale

print(suppDoublons(L))
