-- Active: 1706528682669@@127.0.0.1@3306@zoo
CREATE TABLE animal(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
name VARCHAR(255) NOT NULL,
race VARCHAR(255),
id_cage INT NOT NULL, 
birthday INT NOT NULL,
country_origin VARCHAR(255));

CREATE TABLE cage(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
cage_status VARCHAR(255) NOT NULL , 
superficie INT NOT NULL,
capacity INT NOT NULL);

INSERT INTO animal (name, race, id_cage, birthday, country_origin) VALUES
('Luna', 'Chat', 1, 2019, 'France'),
('Max', 'Chien', 2, 2018, 'Allemagne'),
('Oscar', 'Perroquet', 3, 2017, 'Espagne'),
('Bella', 'Chat', 1, 2020, 'Italie'),
('Rocky', 'Labrador', 2, 2016, 'États-Unis'),
('Coco', 'Poisson rouge', 4, 2019, 'Japon'),
('Charlie', 'Hamster', 5, 2021, 'Canada'),
('Milo', 'Cocker Spaniel', 2, 2015, 'Australie'),
('Sophie', 'Serpent', 6, 2017, 'Brésil'),
('Simba', 'Lion', 7, 2014, 'Afrique du Sud');

INSERT INTO cage (superficie, capacity, cage_status) VALUES
(20, 5, 1),
(15, 3, 1),
(25, 8, 1),
(18, 4, 1),
(30, 10, 1),
(22, 6, 1),
(35, 12, 1),
(28, 8, 0),
(40, 15, 0),
(32, 10, 0),
(50, 3, 0);
