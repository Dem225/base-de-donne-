import sqlite3

connexion=sqlite3.connect("utlisateurs.db")

cursor=connexion.cursor()

Table_1="""id_utlisateurs
    CREATE TABLE IF NOT EXISTS utlisateurs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    age INTEGER NOT NULL 
    )

"""

Table_2= """
    CREATE TABLE IF NOT EXISTS  commandes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    montant INTEGER NOT NULL,
    id_utlisateur INTEGER,
     FOREIGN KEY (id_utlisateur)
     REFERENCES utlisateurs(id)
    )

"""

cursor.execute(Table_1)
cursor.execute(Table_2 )

connexion.commit()
connexion.close()

    

print("effectué ")