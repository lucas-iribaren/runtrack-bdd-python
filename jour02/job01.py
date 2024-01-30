import mysql.connector

mydb = mysql.connector.connect(
    host = "LaPlateforme",
    user = "root",
    password = "F1m13I12l5",
    database = "LaPlateforme"
)


cursor = mydb.cursor()

cursor.execute("SELECT * FROM etudiants")

results = cursor.fetchall()

results = cursor.fetchall()
print(results)

# Fermeture de la connexion
cursor.close()
mydb.close()