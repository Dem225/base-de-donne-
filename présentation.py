import sqlite3

connect=sqlite3.connect("ecole.bd")

cursor=connect.cursor()


cursor.execute( """
             CREATE TABLE IF NOT EXISTS ecole(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               Nom TEXT NOT NULL,
               Age INTEGER NOT NULL                

               )
            """)

# lists = {  "Nom": "Porll", "Age": 70, }
# lists = {"Nom": "manasse", "Age": 45, }

# cursor.execute(" INSERT INTO  ecole (Nom , Age ) VALUES (:Nom ,:Age) ",lists)
# cursor.execute("SELECT  * FROM ecole ")
# cursor.execute("SELECT * FROM  ecole WHERE Age >?", (20,))
# cursor.execute("UPDATE  ecole  SET Age=? WHERE id=?",(30 ,1))
# cursor.execute("DELETE FROM ecole  WHERE id=? ", (1, ))
# cursor.execute("SELECT * FROM ecole ORDER BY age desc")

cursor.execute("SELECT * FROM ecole WHERE Nom LIKE ? ",("%i%",))
resulat=cursor.fetchall()
if resulat:
    for i in resulat :
        print(i)
else:
    print('auccun resultat')
connect.commit()
connect.close()
