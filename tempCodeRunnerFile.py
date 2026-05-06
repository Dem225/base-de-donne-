import sqlite3

planigue = sqlite3.connect("employer")

c= planigue.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employer(
          Name text ,
          prenom text ,
          )
""")

dicts={"Name":"ZEbi","prenom":"lobognon"}


c.execute("INSERT INTO employer VALUES(:Name,:prenom)",dicts)

planigue.commit()
planigue.close()
