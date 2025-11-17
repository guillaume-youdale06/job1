def rectangle(width, height) :
    rectangle = ""
    for i in range(height) :
        rectangle += "|"
        for y in range(width - 2) :
            if i == 0 or i == height - 1 :
                rectangle += "-"
            else :
                rectangle += " "
        rectangle += "|\n"

    return rectangle

print(rectangle(15,5))