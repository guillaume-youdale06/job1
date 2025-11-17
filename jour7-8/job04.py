def crypte(ch, decal) :
    abc = "abcdefghijklmnopqrstuvwxyz"
    resultat = ""
    for i in ch :
        if i in abc :
            indice = abc.index(i)
            nvl_indice = (indice + decal) % 26
            nouveau_ch = abc[nvl_indice]
            resultat += nouveau_ch

        else :
            resultat += i
    return resultat









"""for y in range(len(abc)) :
    if i == abc[y] :
        if y + decal <= 25 :
            resultat += abc[y + decal]
        else :
            nv_indice = (y + decal) - 25
            resultat += abc[nv_indice]            
decal *= -1
for y in range(len(abc_lenver)) :
    if i == abc_lenver[y] :
        if y + decal <= 25 :
            resultat += abc_lenver[y + decal]
        else :
            nv_indice = (y + decal) - 25
            resultat += abc_lenver[nv_indice]

else :
return ch
return resultat"""
    
print(crypte("bonjour", 3))