import mysql.connector as mysql

connect_params = {
'user':"root",
'password':"",
'host':"localhost",
'database': "ecole"

}

with mysql.connect(**connect_params) as db :
    with db.cursor() as cursor:
        sql ="SELECT * FROM ETUDIANT"
        cursor.execute (sql) 
        cursor.fetchall

        values ('etudiant')