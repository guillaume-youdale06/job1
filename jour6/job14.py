def ajouteValeur(e, l) :
    resultat = [e]
    l += resultat

def separation(ch) :
    mot = ""
    liste = []
    for i in ch :
        if i == " " or i == "," :
            ajouteValeur(mot, liste)
            mot = ""
        else :
            mot += i
    return liste

def trouveLongueur(ch) :
    compt = 0
    for i in ch :
        compt += 1
    return compt
        
def my_long_word(x, ch) :
    ch_final = ""
    liste_mot = separation(ch)
    for i in liste_mot :
        if trouveLongueur(i) > x :
            ch_final += i + " "
    return ch_final

print(my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))