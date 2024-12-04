class M_pesa():
    """processus M-pesa"""
    def __init__(self):
        self.nom = input("Entrer votre nom: ")
        self.post_nom = input("Entrer votre post-nom")
        self.phone_number = input("Entrer votre numero de téléphone: ")
        self.pin = input("Entrer votre pin ")
        self.solde = 200
        self.difference = 0

    def depot(self):
        argent_envoyer = float(input("Combien voulez-vous envoyer? "))
        if self.solde >= argent_envoyer:
            beneficiaire = input("Entrer le numero du beneficiaire")
            system_question = input(f"Voulez-vous envoyer au numero suivant: {beneficiaire}").upper()
            if system_question == "YES":
                pin_code = input("Entrer votre pin pour valider l'opération")
                if pin_code == self.pin:
                    self.difference = self.solde - argent_envoyer
                    return f"Votre transaction au numéro {beneficiaire} a été effectué avec succès"
                else:
                    return f"Code pin non identique"
            else:
                return f"Votre transaction a échoué"

        if argent_envoyer > self.solde:
            return f"Désolé votre solde {self.solde} est insuffisant pour effectuer cette transaction"

    def retrait(self):
        somme = float(input("Combien voulez-vous retirer? "))
        if self.solde >= somme:
            confirmation_question = input(f"Voulez-vous retirer cette somme? {somme} ").upper()
            if confirmation_question == "YES":
                pin_code = input("Entrer votre pin pour valider l'opération")
                if pin_code == self.pin:
                    difference = self.solde - somme
                    return f"Votre opération a été effectuée avec succès"
                else:
                    return "Désolé pin non-identifié"
            else:
                return f"Votre opération a échoué"
        else:
            return f"Désolé votre balance est insuffisante pour effecrtuer cette opération"

    