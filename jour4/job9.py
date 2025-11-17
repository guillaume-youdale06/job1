def moyenne(a, b, c) :
    return (float(a) + float(b) + float(c))/3

def statutEleve(moyenne) :
    if moyenne >= 15 :
        print("Très bon élève")
    elif 14 >= moyenne >= 11 :
        print("Bon élève")
    elif 10 >= moyenne >= 8 :
        print("Elève moyen")
    else :
        print("Elève devant faire des efforts")


note1 = input("Saisissez une note : ")
note2 = input("Saisissez une note : ")
note3 = input("Saisissez une note : ")

moyenne_etudiant = moyenne(note1, note2, note3)
statutEleve(moyenne_etudiant)
