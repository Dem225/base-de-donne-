import sqlite3

# 1. Connexion (crée le fichier s'il n'existe pas)
db = sqlite3.connect("MA_basse_de_donnée.db")
cursor = db.cursor()

# 2. Création de la table (Syntaxe corrigée)
cursor.execute("""
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    date_creation TEXT DEFAULT (datetime('now', 'localtime'))
)
""")

# 3. Insertion des données (Correction des tuples)
# On utilise une liste de tuples pour plus de clarté
utilisateurs = [
    ('ZEBI', 'LOBOGNON', 'Zebi.lobognon@gmail.com'),
    ('ZEBI', 'MANASSE', 'Zebi.MANASSE@gmail.com'),
    ('ZEBI', 'WILFEID', 'Zebi.WILFEID@gmail.com')
]

# On insère tout d'un coup avec executemany
cursor.executemany("INSERT INTO user (nom, prenom, email) VALUES (?, ?, ?)", utilisateurs)

# 4. Validation et fermeture
db.commit()
db.close()

# print("Bravo ! La base de données a été créée et les utilisateurs ajoutés.")

