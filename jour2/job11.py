chaine_a_tester = str(input("Saisissez un chaine de caractère"))
verif = False

for i in chaine_a_tester :
    if i == 'e' or i == 'E' :
        verif = True

if verif :
    print("La lettre 'e' est présente dans la chaîne de caractère")
else :
    print("La lettre 'e' n'est pas présente dans la chaîne de caractère")