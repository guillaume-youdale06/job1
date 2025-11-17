def index() :
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.append("mangue")
    deux = fruits[2]
    dernier = fruits[len(fruits) - 1]
    fruits[2] = dernier
    fruits[len(fruits) - 1] = deux
    print(fruits)

index()