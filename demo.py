import sqlite3

db = sqlite3.connect("MA_basse_de_donnée.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    date_creation TEXT DEFAULT (datetime('now', 'localtime'))
)
""")

# utilisateurs = [
#     'ZEBI', 'WILFEID', 'Zebi.ddddd@gmail.com'
# ]
# cursor.execute("INSERT INTO user(nom,prenom,email) VALUES (:nom,:prenom, :email)",utilisateurs)


cursor.execute("DELETE FROM user WHERE email=?",('wilsone@hate.th',))
db.commit()
db.close()

# print("Bravo ! La base de données a été créée et les utilisateurs ajoutés.")

