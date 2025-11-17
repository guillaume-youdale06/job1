def calcule(num1, operator, num2) :
    liste_operateur = ["+", "-", "*", "/", "%"]
    for i in range (5) :
        if operator == liste_operateur[i] :
            if i == 0 :
                resultat = num1 + num2
            elif i == 1 :
                resultat = num1 - num2
            elif i == 2 :
                resultat = num1 * num2
            elif i == 3 :
                resultat = num1 / num2
            else :
                resultat = num1 % num2
    return resultat

print(calcule(1, "*", 2))