-- Active: 1706528682669@@127.0.0.1@3306@laplateforme
CREATE TABLE etage(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
nom VARCHAR(255) NOT NULL,
numero INT,
superficie INT
);

CREATE TABLE salle(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
nom VARCHAR(255) NOT NULL,
id_etage INT,
capacite INT
);