import sqlite3

connection=sqlite3.connect("NAN.db")

cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT  EXISTS  Nan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom text not null,
            prenom text NOT null,
            age integer not null,
            specialite not null ,
            matricul not null unique
               );

""")

connection.commit()
connection.close()