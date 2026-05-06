import sqlite3

planigue = sqlite3.connect("employer.db")
c = planigue.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employer(
          Non text,
          prenom text
          
          )
""")

dicts = {"prenom":"lobognon", "Non": "ZEbi"}

c.execute("INSERT INTO employer VALUES(:Non, :prenom)", dicts)

planigue.commit()
planigue.close()

print("Données insérées avec succès !")

