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
        currency = input("CF ou USD: ").upper()
        if currency not in ["CF", "USD"]:
            print("Devise invalide. Veuillez choisir CF ou USD.")
            return

        montant = float(input(f"Entrer le montant à envoyer en {currency}: "))
        if montant <= 0:
            print("Montant invalide. Veuillez entrer un montant positif.")
            return

        phone_number = input("Entrer le numéro de téléphone du destinataire: ")
        # Add validation for phone number format if needed

        user_answer = input(f"Souhaitez-vous envoyer {montant} {currency} au numéro {phone_number} ? (Oui/Non)").upper()
        if user_answer == "OUI":
            if currency == "CF":
                montant_usd = montant / 2950
                if montant_usd > self.solde:
                    print("Solde insuffisant.")
                    return
                self.solde -= montant_usd
            else:
                if montant > self.solde:
                    print("Solde insuffisant.")
                    return
                self.solde -= montant
            print(f"Montant envoyé: {montant} {currency} au numéro {phone_number}.")
            print(f"Nouveau solde: {self.solde} USD.")

    def retrait(self):
        currency = input("CF ou USD: ").upper()
        if currency not in ["CF", "USD"]:
            print("Devise invalide. Veuillez choisir CF ou USD.")
            return

        montant = float(input(f"Entrer le montant à retirer en {currency}: "))
        if montant <= 0:
            print("Montant invalide. Veuillez entrer un montant positif.")
            return

        user_answer = input(f"Souhaitez-vous retirer {montant} {currency} ? (Oui/Non)").upper()
        if user_answer == "OUI":
            if currency == "CF":
                montant_usd = montant / 2950
                if montant_usd > self.solde:
                    print("Solde insuffisant.")
                    return
                self.solde -= montant_usd
            else:
                if montant > self.solde:
                    print("Solde insuffisant.")
                    return
                self.solde -= montant
            print(f"Montant retiré: {montant} {currency}.")
            print(f"Nouveau solde: {self.solde} USD.")

    def account_solde(self):
        currency = input("CF ou USD: ").upper()
        if currency not in ["CF", "USD"]:
            print("Devise invalide. Veuillez choisir CF ou USD.")
            return

        if currency == "CF":
            print(f"Votre solde en CF: {self.solde * 2950}")
        else:
            print(f"Votre solde en USD: {self.solde}")

def menu_principal():
    while True:
        print("1. Vérifier PIN")
        print("2. Dépôt")
        print("3. Retrait")
        print("4. Solde")
        print("5. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            utilisateur.verifier_pin()
        elif choix == "2":
            utilisateur.depot()
        elif choix == "3":
            utilisateur.retrait()
        elif choix == "4":
            utilisateur.account_solde()
        elif choix == "5":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Création d'un compte utilisateur
utilisateur = Mpesa()

# Boucle principale
menu_principal()