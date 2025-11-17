def my_sort(l) :
    compt = 0                           #Initialisation d'un compteur
    for i in range(len(l) - 1) :        #On parcourt les éléments grace à l'indice
        for y in range(i + 1, len(l)):  #On parcourt les éléments grace à l'indice
            if l[i] > l[y] :            #On vérifie si l'élément suivant est supérieur
                l[i], l[y] = l[y], l[i] #On inverse les éléments si le suivant est supérieur
                compt += 1              #On incrémente le compteur à chaque déplacement
    print(f"Nombre total de coups nécessaires pour trier la liste : {compt}\nListe triée : {l}") #On print le résultat

L = [8, 24, 48, 2, 16, 67, 48, 21, 90, 96, 74, 22]
my_sort(L)