import sqlite3

connexion=sqlite3.connect("Moov.db")

cursor=connexion.cursor()

Table_1="""
    CREATE TABLE IF NOT EXISTS utilisateurs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    age INTEGER NOT NULL ,
    lieux TEXT NOT NULL
    )

"""

Table_2= """
    CREATE TABLE IF NOT EXISTS  commandes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mounting INTEGER NOT null,
    TEL INTEGER NOT NULL,
    id_utilisateurs INTEGER,
     FOREIGN KEY (id_utilisateurs)
     REFERENCES utilisateurs(id)
    )

"""

cursor.execute(Table_1)
cursor.execute(Table_2 )

utilisateurs_a_mettre_a_jour = [
     {"lieux":"Abobo" , "non":"Zebi"},
     {"lieux":"Adjamé", "non":"Sarah"},     
     {"lieux":"Anyama", "non":"Aliman"},
     {"lieux":"Attécoubé","non":"Roxame"},
     {"lieux":"Cocody", "non":"Luise"},
     {"lieux":"Cocody", "non":"jullitte"},
     {"lieux":"Marcory", "non":"mack"}
]

# cursor.execute("ALTER TABLE utilisateurs ADD COLUMN lieux TEXT ")
# cursor.execute("ALTER TABLE commands  ADD COLUMN TEL INTEGER")
# cursor.executemany("insert INTO commands ()VALUES () ")

cursor.executemany("UPDATE utilisateurs SET lieux = :lieux WHERE nom = :nom", utilisateurs_a_mettre_a_jour)



connexion.commit()
connexion.close()
print("effectué ")