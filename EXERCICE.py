import sqlite3

bd=sqlite3.connect("annonces.db")

cusor=bd.cursor()

cusor.execute("""
    CREATE TABLE IF NOT EXISTS annonces (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              titre TEXTE NOT NULL,
              prix INTEGER  NOT NULL,
              ville TEXTE NOT NULL,
              disponible  INTEGER NOT NULL
              )
""")

Données=[
    ('Study',150000,'Abidjan','1'),
    ('Villa Luxe',800000,'Assinie','1'),
    ('Appartement',300000,'Abidjan','1'),
    ('Terrain',5000000,'Yamoussoukro','1')
]


# cusor.executemany("INSERT  INTO annonces (titre, prix, ville,disponible) VALUES (? , ? , ? , ?)",Données)
# cusor.execute("UPDATE annonces SET  disponible = ? WHERE  id = ?",(1,1))
# cusor.execute("UPDATE annonces SET  disponible = ? WHERE  id = ?",(1,2))
# cusor.execute("UPDATE annonces SET  disponible = ? WHERE  id = ?",(2,3))
# cusor.execute("UPDATE annonces SET  disponible = ? WHERE  id = ?",(1,4))


# Mission A : Afficher uniquement le titre et le prix de toutes les annonces situées à "Abidjan".

cusor.execute("DELETE FROM annonces WHERE ville =?" , ('Yamoussoukro' ,))
for I in cusor.fetchall():
   
     print(I)


bd.commit()
bd.close()

