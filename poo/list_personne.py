from personne import Personne

class ListePersonnes:
    def __init__(self):
        self._personnes = []
    
    def ajouter_personne(self, nom, age):
        personne = Personne(nom, age)
        self._personnes.append(personne)
    
    def afficher_personnes(self):
        for personne in self._personnes:
            personne.afficher_details()
    
    def rechercher_personne(self, nom):
        for personne in self._personnes:
            if personne.nom == nom:
                personne.afficher_details()
                return
        print("Personne non trouvée.")

    def filtrer_personnes_par_age(self, min_age, max_age):
        for personne in self._personnes:
            if min_age <= personne.age <= max_age:
                personne.afficher_details()



