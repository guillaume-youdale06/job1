nom = "pain"
prix_unitaire = 1.50
stock = 670

print("===Information du produit===")
print(f"Nom du produit : {nom}")
print(f"Prix unitaire du produit : {prix_unitaire}")
print(f"Stock disponible : {stock}")

achat = int(input("Saisissez le nombre de baguette à acheter :"))
stock -= achat
prix_unitaire = (prix_unitaire + prix_unitaire * (1/10))

print("===Information du produit===")
print(f"Nom du produit : {nom}")
print(f"Prix unitaire du produit : {prix_unitaire}")
print(f"Stock disponible : {stock}")
