alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_a_l_envers = ""

for i in range(len(alphabet) -1) :
    alphabet_a_l_envers = alphabet_a_l_envers + alphabet[len(alphabet) - 1 - i]

print(alphabet_a_l_envers)