import mysql.connector

class Zoo:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "F1m13I12l5*",
        database = "zoo"
        )
        self.cursor = self.mydb.cursor()
    
    def menu(self):
        while True:
            choose = int(input(
"""Bienvenue dans le programme de modification des données du zoo, veuillez entrer le chiffre correspondant à votre demande :
    1 - Ajouter un animal au zoo
    2 - Supprimer un animal du zoo 
    3 - Modifier une information d'un animal
            
    4 - Ajouter une cage au zoo
    5 - Supprimer une cage du zoo
    6 - Modifier une information de la cage
    0 - Quitter
    """))
            if choose == 0:
                print("Merci d'avoir utilisé le programme. Au revoir!")
                break
            elif choose == 1:
                print("Ajout d'un animal au zoo:")
                name = input("Nom de l'animal : ")
                race = input("Race de l'animal : ")
                id_cage = int(input("ID de la cage : "))
                birthday = input("Année de naissance : ")
                country_origin = input("Pays d'origine : ")
                self.add_animal(name, race, id_cage, birthday, country_origin)
            elif choose == 2:
                print("Suppression d'un animal du zoo:")
                name_to_remove = input("Nom de l'animal à supprimer : ")
                self.remove_animal(name_to_remove)
            elif choose == 3:
                print("Modification d'une information d'un animal:")
                # Ajoutez ici le code pour la modification d'une information d'un animal
            elif choose == 4:
                print("Ajout d'une cage au zoo:")
                # Ajoutez ici le code pour l'ajout d'une cage
            elif choose == 5:
                print("Suppression d'une cage du zoo:")
                # Ajoutez ici le code pour la suppression d'une cage
            elif choose == 6:
                print("Modification d'une information de la cage:")
                # Ajoutez ici le code pour la modification d'une information de la cage
            else:
                print("Choix non valide. Veuillez entrer un chiffre entre 0 et 6.")

    def add_animal(self,name,race,id_cage,birthday,country_origin):
        try :
            self.cursor.execute(f"INSERT INTO animal (name,race, id_cage, birthday, country_origin) VALUES ({name},{race}, {id_cage}, {birthday}, {country_origin})")
            print(f"L'animal '{name}' a été ajouté avec succès.")
        except ValueError:
            print("Veuillez rentrez le nom, la race, l'id de la cage, l'année de naissance et le pays d'origine")
        
    def del_animal(self,name):
        try:
            self.cursor.execute(f"DELETE FROM animal WHERE {name}")
            print(f"L'animal '{name}' a été supprimé avec succès.")
        except ValueError:
            print(f"Erreur lors de la suppression de l'animal '{name}'.")

    def modif_animal(self):
        pass

    def add_cage(self):
        pass 

zoo_instance = Zoo()
zoo_instance.menu()