import mysql.connector


class Employe:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        
    def create_employee(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(sql, values)
        self.connection.commit()
        
    def read_all_employees(self):
        sql = "SELECT * FROM employe"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def update_employee_salary(self, employee_id, new_salary):
        sql = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salary, employee_id)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def delete_employee(self, employee_id):
        sql = "DELETE FROM employe WHERE id = %s"
        values = (employee_id,)
        self.cursor.execute(sql, values)
        self.connection.commit()
        
    def close(self):
        self.connection.close()

e = Employe("localhost", "root", "F1m13I12l5*", "job07")
e.create_employee("Test", "Test", 4500.00, 2)
e.read_all_employees()
e.update_employee_salary(1, 3800.00)
e.read_all_employees()
e.delete_employee(2)
e.read_all_employees()
e.close()

