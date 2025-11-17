def triangle(hauteur) :
    triangle = ""
    for i in range(hauteur - 1) :
        if i != hauteur - 2 :
            triangle += ((hauteur - 1) - i)*" " + "/" + (i+i)*" " + "\\"
        else :
            triangle += ((hauteur - 1) - i)*" " + "/" + (i+i)*"_" + "\\"
        triangle += "\n"

    return triangle

print(triangle(10))