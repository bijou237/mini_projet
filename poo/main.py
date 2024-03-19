from list_personne import ListePersonnes
from file_attentes import FileAttente
from salle_cinema import SalleCinema

# Test du code
if __name__ == "__main__":
    # Test de ListePersonnes
    liste_personnes = ListePersonnes()
    liste_personnes.ajouter_personne("Alice", 30)
    liste_personnes.ajouter_personne("Bob", 25)
    liste_personnes.ajouter_personne("Charlie", 40)
    liste_personnes.afficher_personnes()
    liste_personnes.rechercher_personne("Alice")
    liste_personnes.filtrer_personnes_par_age(25, 35)

    # Test de FileAttente
    file_attente = FileAttente()
    file_attente.ajouter_personne_en_attente("David")
    file_attente.ajouter_personne_en_attente("Emma")
    file_attente.supprimer_personne_de_attente()

    # Test de SalleCinema
    salle_cinema = SalleCinema(50)
    salle_cinema.reserver_place("Alice", 10)
    salle_cinema.reserver_place("Bob", 20)
    salle_cinema.reserver_place("Charlie", 30)
    salle_cinema.afficher_places_reservées()
    print("Places disponibles:", salle_cinema.nombre_places_disponibles())
    salle_cinema.filtrer_reservations_par_personne("Alice")
    salle_cinema.annuler_reservation("Bob")
    salle_cinema.reserver_place_speciale("David")
