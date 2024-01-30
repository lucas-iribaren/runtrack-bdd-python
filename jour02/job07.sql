USE DATABASE job07;

CREATE TABLE employe(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL,
    id_service INT
);

INSERT INTO employe(nom,prenom,salaire,id_service)VALUES
('Spaghetti','Betty', 1000.5,1),
('Steak','Chuck', 4500.7,1),
('Doe','John', 1800.2,2),
('Gertrude','Dupuis', 2066.6,2),
('Barnes','Binkie', 5000.1,3);

SELECT salaire FROM employe
WHERE salaire > 3000;

CREATE TABLE service(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255)
);

INSERT INTO service(nom)VALUES
('professeur'),
('directeur'),
('surveillant scolaire');

SELECT employe.nom, employe.prenom, employe.salaire, service.nom as service
FROM employe
JOIN service ON employe.id_service = service.id

