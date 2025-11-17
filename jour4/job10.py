def pair(a) :
    if type(a) == int and a >= 0 :
        if a % 2 == 0 :
            print("Le nombre est pair")
        else :
            print("Le nombre est impair")
    else :
        print("La valeure rentré n'est pas valide")

pair(0)
pair(1)
pair(4)
pair(-7)
pair(1863)
pair("test")
pair(3.67)