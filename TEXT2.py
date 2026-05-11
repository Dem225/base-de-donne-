import sqlite3

planigue = sqlite3.connect("liste.db")
c = planigue.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS liste(
          Non text,
          prenom text,
          salaire int 
          
          )
""")

dicts = {"salaire":100}

c.execute("INSERT INTO liste VALUES(salaire)", dicts)

planigue.commit()
planigue.close()

print("Données insérées avec succès !")

