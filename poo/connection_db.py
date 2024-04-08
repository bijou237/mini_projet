import mysql.connector as mysql
#initialisation de la connexion à la base de données

connect_db = mysql.connect(
    host = "localhost",
    user = "root",
    password ="",
    database = "ecole"
)
cursor = connect_db.cursor()
def insertion():
    sql ="INSERT INTO etudiant(code_permanent, nom, prenom, date_naissance, specialite) values('AD2526', 'Abdou', 'Diallo', '2000-05-15', 'Expert_Developpeur')"
    cursor.execute(sql)

    connect_db.commit()
def afficher():
    sql ="SELECT * FROM etudiant"
    cursor.execute(sql)
    # Recuperation des donnés

    etudiants = cursor.fetchall()
    for etudiant in etudiants:
        print(etudiant)
#insertion()
afficher()


