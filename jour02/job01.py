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

print(results)

cursor.close()
mydb.close()