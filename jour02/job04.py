import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "F1m13I12l5*",
    database = "LaPlateforme"
)


cursor = mydb.cursor()


cursor.execute("SELECT nom, capacite FROM salle")

salle = cursor.fetchall()

print(salle)

cursor.close()
mydb.close()