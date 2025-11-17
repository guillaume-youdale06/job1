pair = ""
impair = ""

for i in range(1, 31) :
    if i%2 == 0 :
        pair += " " + str(i)
    else :
        impair += " " + str(i)

print(pair)
print(impair)
