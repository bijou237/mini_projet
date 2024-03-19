class SalleCinema:
    def __init__(self, capacite):
        self._capacite = capacite
        self._reservations = {}
    
    def reserver_place(self, nom, place):
        if len(self._reservations) < self._capacite:
            self._reservations[nom] = place
            print("Place réservée pour", nom)
        else:
            print("La salle est pleine, aucune place disponible.")
    
    def afficher_places_reservées(self):
        for nom, place in self._reservations.items():
            print(f"{nom}: Place {place}")
    
    def nombre_places_disponibles(self):
        return self._capacite - len(self._reservations)
    
    def filtrer_reservations_par_personne(self, nom):
        if nom in self._reservations:
            print(f"Réservations pour {nom}: Place {self._reservations[nom]}")
        else:
            print(f"Aucune réservation pour {nom}.")
    
    def annuler_reservation(self, nom):
        if nom in self._reservations:
            del self._reservations[nom]
            print(f"Réservation annulée pour {nom}.")
        else:
            print(f"Aucune réservation trouvée pour {nom}.")
    
    def reserver_place_speciale(self, nom):
        if len(self._reservations) < self._capacite:
            place = "spéciale"
            self._reservations[nom] = place
            print(f"Place spéciale réservée pour {nom}")
        else:
            print("La salle est pleine, aucune place spéciale disponible.")
