montant_initial = 2000
taux_rendement = 3
gain = (montant_initial + montant_initial * (taux_rendement/100)) - montant_initial
print(f"Le gain annuel sera de : {gain}")

montant_2 = montant_initial + 5000
taux_rendement += 2
gain = (montant_2 + montant_2 * (taux_rendement/100)) - montant_2
print(f"Le gain annuel sera de : {gain}")

montant_final = (montant_2 - montant_2 * (10/100))
taux_rendement -= 1
gain = (montant_final + montant_final * (taux_rendement/100)) - montant_final
print(f"Le gain annuel sera de : {gain}")