import mysql.connector

mydb = mysql.connector.connect(
    host = "LaPlateforme",
    user = "root",
    password = "F1m13I12l5",
    database = "LaPlateforme"
)


cursor = mydb.cursor()


cursor.execute("SELECT nom, capacite FROM salle")

salles = cursor.fetchall()

for salle in salles:
    nom, capacite = salle
    print(f"Nom: {nom}, Capacité: {capacite}")

cursor.close()
mydb.close()