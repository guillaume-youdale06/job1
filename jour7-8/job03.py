def rectangle(n) :
    diag = n + 2
    rectangle = ""
    for i in range(n + 3) :
        if i == 0 or i == n + 2 :
            rectangle += "+" + (n+1)*"-" + "+"
        else :
            for y in range(n + 3) :
                if y == 0 or y == n + 2:
                    rectangle += "|"
                else :
                    if y == diag :
                        rectangle += " "
                    else :
                        rectangle += "#"
        rectangle += "\n"
        diag -= 1
    return rectangle

print(rectangle(26))