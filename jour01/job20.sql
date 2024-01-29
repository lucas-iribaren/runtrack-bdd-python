-- Active: 1706528682669@@127.0.0.1@3306@laplateforme
SELECT COUNT(*) AS nombre_etudiants_mineurs
FROM etudiant
WHERE age < 18;
