-- Active: 1706528682669@@127.0.0.1@3306@laplateforme
UPDATE etudiant
SET age = 20
WHERE nom = 'Spaghetti' AND prenom = 'Betty';

SELECT *
FROM etudiant
WHERE nom = 'Spaghetti' AND prenom = 'Betty';
