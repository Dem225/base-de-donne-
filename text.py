import sqlite3

bas_fex = sqlite3.connect("BAUME.db")
cursor = bas_fex.cursor()

# 2. Création de la table (Syntaxe ENFIN corrigée !)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        E_mail TEXT NOT NULL,
        MODE_PASSE TEXT NOT NULL,
        Date_creations TEXT DEFAULT (datetime('now','localtime'))
    )
""")

# 3. Récupération des données utilisateur
print("--- INSCRIPTION ---")
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prenom : ")
email = input("Entrez votre E-mail : ")
mdp = input("Entrez votre mot de passe : ")

nouvel_utilisateur = (nom, prenom, email, mdp)

# 4. Insertion dans la base de données
try:
    cursor.execute("""
        INSERT INTO user (nom, prenom, E_mail, MODE_PASSE) 
        VALUES (?, ?, ?, ?)
    """, nouvel_utilisateur)
    
    bas_fex.commit()
    print("\nFélicitations, utilisateur enregistré avec succès !")
except sqlite3.Error as e:
    print(f"Erreur lors de l'enregistrement : {e}")

# 5. Fermeture
bas_fex.close()