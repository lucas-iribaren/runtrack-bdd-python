-- Active: 1706528682669@@127.0.0.1@3306@laplateforme
SELECT *
FROM etudiant
WHERE age = (SELECT MAX(age) FROM etudiant);
