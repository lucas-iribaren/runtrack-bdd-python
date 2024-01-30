-- Active: 1706528682669@@127.0.0.1@3306@laplateforme
INSERT INTO etage(id,nom,numero,superficie) VALUES
(1,'RDC',0,500),
(2,'R+1',1,500)

INSERT INTO salle(id,nom,id_etage,capacite) VALUES
(1,'Lounde',1,100),
(2,'Studio son',1,5),
(3,'Broadcasting',2,50),
(4,'Bocal pPeda',2,4),
(5,'Coworking',2,80),
(6,'Studio Video',2,5)