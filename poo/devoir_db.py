import mysql.connector as mysql

def connexion_bdd():
    """
    Fonction pour se connecter à la base de données
    """

        # Remplacer les valeurs par les informations de votre base de données
    connexion = mysql.connect(
                host="localhost",
            user="root",
            password="",
            database="ecole",
        )
    return connexion

def insertion(code_permanent, nom, prenom, date_naissance, specialite):
    """
    Fonction pour insérer un étudiant dans la base de données
    """
    
    connexion = connexion_bdd()
    curseur = connexion.cursor()
    
     
    sql = "INSERT INTO etudiant (code_permanent, nom, prenom, date_naissance, specialite) VALUES (%s, %s, %s, %s, %s)"
    valeurs = (code_permanent, nom, prenom, date_naissance, specialite)
    curseur.execute(sql, valeurs)
    connexion.commit()

    
def afficher(connexion):
    """
    Fonction pour afficher tous les étudiants de la base de données
    """
    curseur = connexion.cursor()

        # Remplacer "nom_de_la_table" par le nom de votre table
    sql = "SELECT * FROM etudiant"
    curseur.execute(sql)
    resultats = curseur.fetchall()
    for resultat in resultats:
            print(f"ID : {resultat[0]}")
            print(f"Nom : {resultat[1]}")
            print(f"Prénom : {resultat[2]}")
            print(f"Age : {resultat[3]}")
            print("-----")

connex= connexion_bdd()
insertion("BC0023556","Bijou","Claris","2002-05-15","Expert Comptable")
afficher(connex)
 