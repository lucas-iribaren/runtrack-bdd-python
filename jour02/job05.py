import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "F1m13I12l5*",
    database = "LaPlateforme"
)


cursor = mydb.cursor()


cursor.execute("SELECT superficie FROM etage")

superficie = cursor.fetchall()
result = 0

for i in superficie:
    result += i[0]

print("La superficie de La Plateforme est de", result,"m2")

cursor.close()
mydb.close()