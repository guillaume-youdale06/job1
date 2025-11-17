def bouffe(type, saison) :
    type = type.lower()
    saison = saison.lower()
    if type == "fruits" and saison == "hiver" :
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été" :
        print("poire, fraise, cassis")
    elif type == "légumes" and saison == "hiver" :
        print("carotte, topinambour, endive")
    elif type == "légumes" and saison == "été" :
        print("artichaut", "aubergine", "navet")

bouffe(input("Saisissez 'fruits' ou 'légumes' : "), input("Saisissez 'été' ou 'hiver' : "))
