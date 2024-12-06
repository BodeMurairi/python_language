class Mpesa:
    def __init__(self):
        self.nom = input("Entrer votre nom: ")
        self.prenom = input("Entrer votre prenom: ")
        self.telephone = input("Entrer votre telephone: ")
        self.solde = float(input("Entrer votre solde en USD: "))
        self.pincode = input("Entrer votre pincode: ")
        self.currency = None

    def verifier_pin(self):
        print(self.pincode)

    def depot(self):
        self.currency = input("CF ou USD: ").upper()
        if self.currency == "CF":
            self.solde = self.solde * 2950
            montant = float(input("Entrer le montant à envoyer en CF: "))
        montant = float(input("Entrer le montant à envoyer en USD: "))
        phone_number = input("Entrer le numerdo de téléphone du destinateur: ")
        # Vérifier si le montant est positif et la devise est valide
        if montant > self.solde :
            print("Montant invalide car supérieur au solde.")
        else:
            user_answer= input(f"Souhaitez-vous envoyer le {montant}{self.currency} au numero suivant {phone_number} ?").upper()
            if user_answer == "OUI":
                self.solde = self.solde - montant
                print (f"Montant envoyé : {montant}{self.currency} au numero suivant {phone_number}.\nVotre nouveau solde : {self.solde}{self.currency}.")

    def retrait(self):
        self.currency = input("CF ou USD: ").upper()
        if self.currency == "CF":
            self.solde = self.solde * 2950
            montant = float(input("Entrer le montant à envoyer en CF: "))
        montant = float(input("Entrer le montant à envoyer en USD: "))
        # Vérifier si le solde est suffisant et la devise est valide
        if montant > self.solde:
            print("Solde insuffisant")
        else:
            user_answer = input(f"Souhaitez-vous retirer ce montant {montant}{self.currency} ?").upper()
            if user_answer == "YES":
                self.solde = self.solde - montant
                print(f"Montant retiré : {montant}\n Votre nouveau solde : {self.solde}{currency}")

    def account_solde(self):
        self.currency = input("CF ou USD: ").upper()
        if self.currency == "CF":
            self.solde = self.solde * 2950
            print(f"{self.solde}{self.currency}")
        print(f"{self.solde}{self.currency}")

def menu_principal():
    print("1. Verifier pin\n 2. Dépôt\n 3. Retrait\n 4. Solde")
    # ... (menu interactif avec des options claires et la gestion des devises)

# Création d'un compte utilisateur
utilisateur = Mpesa()

# Boucle principale
menu_principal()
choix = input("Votre choix : ")
if choix == "1":
    utilisateur.verifier_pin()
elif choix == "2":
    utilisateur.depot()
elif choix == "3":
    utilisateur.retrait()
elif choix == "4":
    utilisateur.account_solde()

