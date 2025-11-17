def nbrMetre(marche, hauteur) :
    resultat_cm = (((marche*hauteur)*2)*5)*7
    resultat_m = resultat_cm / 100
    print(f"Pour {marche} marches de {hauteur} cm, le gardien parcourt {resultat_m} m par semaine.")

nbrMetre(567, 5)