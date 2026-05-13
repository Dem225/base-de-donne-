import sqlite3

bd=sqlite3.connect("Statistics.db")


cusor=bd.cursor()


cusor.execute("""
     CREATE TABLE IF NOT  EXISTS Statistics (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
               Titre TEXTE NOT NULL,
               Prix INTEGER  NOT NULL,
               Ville TEXTE NOT NULL ,
               Available INTEGER NOT NULL
               )

""")

# 1présentation de la base de données 

base_données=[
    ('Penthouse',1200000 , 'Abidjan' ,1 ),
    ('Studio Zone',4200000 , 'Abidjan' ,1 ),
    ('Résidence Bassam',600000 , 'Grand-Bassam' ,1 ),
    ('Bureau Plateau',450000 , 'Abidjan' ,0 ),
    ('Loft Almadies',950000 , 'Dakar' ,1 )
]



# cusor.executemany("INSERT  INTO Statistics (Titre, Prix, Ville,Available) VALUES (? , ? , ? , ?)",base_données)

#Mission A (Le Tri) : Afficher toutes les Statistics disponibles, classées du plus cher au moins cher.

# cusor.execute("SELECT * FROM Statistics  WHERE ville=? ORDER BY prix desc",('Abidjan' ,))

# Where I demand the moyenne (AVG) of the prix column

cusor.execute("SELECT AVG(Prix) FROM Statistics WHERE ville = ?", ('Abidjan' ,))

resultat = cusor.fetchone()

moyenne = resultat[0]

print(f"Le prix moyen des logements à Abidjan est de : {moyenne} FCFA")
donnees=cusor.fetchall()
for i in donnees:
    
    print(i)
bd.commit()
bd.close()

