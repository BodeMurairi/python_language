A = float(input("Entrer le premier nombre: "))
B = float(input("Entrer le deuxieme nombre: "))

produit = A * B

if produit > 0:
    print(f"le produit {produit} est positif")
elif produit == 0:
    print(f"le produit {produit} est nul")
else:
    print(f"le produit {produit} est négatif")