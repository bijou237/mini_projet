class FileAttente:
    def __init__(self):
        self._attente = []
    
    def ajouter_personne_en_attente(self, nom):
        self._attente.append(nom)
    
    def supprimer_personne_de_attente(self):
        if self._attente:
            nom = self._attente.pop(0)
            print("Personne supprimée de la file d'attente:", nom)
        else:
            print("File d'attente vide.")

