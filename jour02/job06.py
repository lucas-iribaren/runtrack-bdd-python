import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "F1m13I12l5*",
    database = "LaPlateforme"
)

cursor = mydb.cursor()

cursor.execute("SELECT capacite FROM salle")

capacite = cursor.fetchall()
result = 0

for i in capacite:
    result += i[0]

print(f"La capacité de toutes les salles est de: {result}")

cursor.close()
mydb.close()