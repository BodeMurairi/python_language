nombreDePhotocopie = int(input("Combien de photocopies allez-vous faire?"))
if nombreDePhotocopie <= 10:
    prix = 0.25 * nombreDePhotocopie
    print(f"La facture est de {prix} DH")
elif (nombreDePhotocopie > 10) and (nombreDePhotocopie <= 20):
    prix = 0.20 * nombreDePhotocopie
    print(f"la facture est de {prix} DH")
else:
    prix = 0.1 * nombreDePhotocopie
    print(f"la facture est de {prix} DH")