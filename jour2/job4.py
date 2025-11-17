n = int(input("Saisissez un entier : "))

for i in range(1, n+1) :
    print(f"Table de multiplication de {i} : ")
    for y in range(1, 11) :
        print(f"{i} x {y} = {i*y}")
    print("")
