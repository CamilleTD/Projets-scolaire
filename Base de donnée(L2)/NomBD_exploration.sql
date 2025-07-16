DROP DATABASE if exists `Gestion_employe`;
create schema `Gestion_employe`;
use Gestion_employe;


CREATE TABLE DEPARTEMENT(
   id_departement INT,
   nom VARCHAR(255) NOT NULL,
   PRIMARY KEY(id_departement),
   UNIQUE(nom)
);

CREATE TABLE JOB(
   id_job INT,
   nom VARCHAR(255) NOT NULL,
   PRIMARY KEY(id_job),
   UNIQUE(nom)
);

CREATE TABLE MISSION(
   id_mission INT,
   nom VARCHAR(255) NOT NULL,
   description VARCHAR(255) NOT NULL,
   PRIMARY KEY(id_mission),
   UNIQUE(nom)
);

CREATE TABLE LIVRABLE(
   id_livrable INT,
   nom VARCHAR(255) NOT NULL,
   description VARCHAR(255) NOT NULL,
   date_livraison DATE NOT NULL check (date_livraison between '2024-01-01' and '2026-12-31'),
   id_mission INT NOT NULL,
   PRIMARY KEY(id_livrable),
   FOREIGN KEY(id_mission) REFERENCES MISSION(id_mission)
);

CREATE TABLE CLIENT(
   id_client INT,
   nom VARCHAR(255) NOT NULL,
   adresse VARCHAR(255) NOT NULL,
   PRIMARY KEY(id_client),
   UNIQUE(nom)
);

CREATE TABLE QUALIFICATION(
   id_qualification INT,
   nom VARCHAR(255) NOT NULL,
   PRIMARY KEY(id_qualification),
   UNIQUE(nom)
);

CREATE TABLE EMPLOYE(
   id_employe INT,
   nom VARCHAR(255) NOT NULL,
   date_embauche DATE NOT NULL check (date_embauche between '2022-01-01' and '2026-12-31'),
   commission DECIMAL(10,2) NOT NULL check ( commission >= 0),
   salaire DECIMAL(10,2) NOT NULL check (salaire >= 0),
   id_qualification INT NOT NULL,
   id_employe_1 INT,   
   id_job INT ,
   id_departement INT NOT NULL,
   PRIMARY KEY(id_employe),
   UNIQUE(nom),
   FOREIGN KEY(id_qualification) REFERENCES QUALIFICATION(id_qualification),
   FOREIGN KEY(id_employe_1) REFERENCES EMPLOYE(id_employe),
   FOREIGN KEY(id_job) REFERENCES JOB(id_job),
   FOREIGN KEY(id_departement) REFERENCES DEPARTEMENT(id_departement)
);

CREATE TABLE CONTRAT(
   id_contrat INT,
   description_intervenant VARCHAR(255) NOT NULL,
   date_debut DATE NOT NULL check ( date_debut between '2024-01-01' and '2026-12-31'),
   tarif DECIMAL(10,2) NOT NULL check (tarif >= 0),
   id_qualification INT NOT NULL,
   id_client INT NOT NULL,
   PRIMARY KEY(id_contrat),
   FOREIGN KEY(id_qualification) REFERENCES QUALIFICATION(id_qualification),
   FOREIGN KEY(id_client) REFERENCES CLIENT(id_client)
);

CREATE TABLE Effectue(
   id_employe INT,
   id_mission INT,
   PRIMARY KEY(id_employe, id_mission),
   FOREIGN KEY(id_employe) REFERENCES EMPLOYE(id_employe),
   FOREIGN KEY(id_mission) REFERENCES MISSION(id_mission)
);

CREATE TABLE Concerne(
   id_employe INT,
   id_contrat INT,
   PRIMARY KEY(id_employe, id_contrat),
   FOREIGN KEY(id_employe) REFERENCES EMPLOYE(id_employe),
   FOREIGN KEY(id_contrat) REFERENCES CONTRAT(id_contrat)
);

/*-----------------------------------------------------*/
-- ajout de 6 données dans la table DEPARTEMENT
INSERT INTO DEPARTEMENT (id_departement, nom)
VALUES (1, 'Marketing'),
       (2, 'Sales'),
       (3, 'Engineering'),
       (4, 'Human Resources'),
       (5, 'Finance'),
       (6, 'Customer Service');

-- ajout de 8 données dans la table JOB
INSERT INTO JOB (id_job, nom)
VALUES (1, 'Software Developer'),
       (2, 'Marketing Manager'),
       (3, 'Sales Representative'),
       (4, 'Human Resources Specialist'),
       (5, 'Account Manager'),
       (6, 'Business Analyst'),
       (7, 'Content Writer'),
       (8, 'User Experience (UX) Designer');

-- ajout de 6 données dans la table MISSION
INSERT INTO MISSION (id_mission, nom, description)
VALUES (1, 'Develop e-commerce platform', 'Create a user-friendly online store for a clothing retailer'),
       (2, 'Design marketing campaign', 'Develop a comprehensive marketing strategy to reach new customers'),
       (3, 'Implement CRM system', 'Set up a customer relationship management system for improved client interactions'),
       (4, 'Develop internal communication strategy', 'Create a plan to improve communication and collaboration within the company'),
       (5, 'Update company website', 'Redesign and update the company website to reflect the latest brand identity and improve user experience'),
       (6, 'Conduct market research', 'Gather data and insights on customer preferences, market trends, and competitor analysis');
       
-- ajout de 6 données dans la table LIVRABLE
INSERT INTO LIVRABLE (id_livrable, nom, description, date_livraison, id_mission)
VALUES (1, 'Backend development', 'Develop the server-side functionality of the e-commerce platform', '2024-04-30', 1),
       (2, 'Marketing materials', 'Create brochures, social media posts, and email campaigns', '2024-04-15', 2),
       (3, 'CRM system configuration', 'Set up user accounts, customize workflows, and integrate with existing systems', '2024-05-10', 3),
       (4, 'Content calendar', 'Develop a plan for creating and publishing content across various marketing channels', '2024-05-20', 4),
       (5, 'Wireframes and prototypes', 'Create low-fidelity and high-fidelity wireframes and prototypes for the new website design',	'2024-04-25', 5),
       (6, 'Market research report', 'Compile and analyze data from market research activities, presenting key findings and recommendations', '2024-06-15',6);

-- ajout de 4 données dans la table CLIENT
INSERT INTO CLIENT (id_client, nom, adresse)
VALUES (1, 'ABC Clothing', '123 Main Street, Anytown, CA 12345'),
       (2, 'Tech Solutions Inc.', '456 Elm Street, Springfield, NY 54321'),
       (3, 'GreenTech Solutions', '789 Oak Avenue, Sunnyvale, CA 94089'),
       (4, 'Medical Supplies Inc.', '45 High Street, Boston, MA 02110');

-- ajout de 8 données dans la table QUALIFICATION
INSERT INTO QUALIFICATION (id_qualification, nom)
VALUES (1, 'Software Engineering'),
       (2, 'Marketing'),
       (3, 'Sales'),
       (4, 'Human Resources Management'),
       (5, 'Project Management'),
       (6, 'Graphic Design'),
       (7, 'Copywriting'),
       (8, 'Data Analysis');

-- ajout de 4 données dans la table CONTRAT
INSERT INTO CONTRAT (id_contrat, description_intervenant, date_debut, tarif, id_qualification, id_client)
VALUES (1, 'Develop mobile app for fitness tracker', '2024-02-15', 12000.00, 1, 1),
       (2, 'Create social media marketing strategy', '2024-03-01', 8000.00, 2, 2),
       (3, 'Develop e-learning modules', '2024-03-15', 15000.00, 5, 3),
       (4, 'Design company logo and branding materials', '2024-04-01', 10000.00, 6, 4);

-- ajout de 7 données dans la table EMPLOYE
INSERT INTO EMPLOYE (id_employe, nom, date_embauche, commission, salaire, id_qualification, id_employe_1, id_job, id_departement)
VALUES (1, 'John Doe', '2023-01-01', 0.10, 80000.00, 1, NULL, 1, 1),
       (2, 'Jane Smith', '2022-06-15', 0.15, 75000.00, 2, 1, 2, 1),
       (3, 'Michael Lee', '2023-07-20', 0.05, 65000.00, 3, 2, 3, 2),
       (4, 'Alice Johnson', '2024-02-05', 0.20, 50000.00, 4, 3, 1, 3),
       (5, 'David Jones', '2023-05-12', 0.05, 70000.00, 3, NULL, 5, 2),
       (6, 'Sarah Rodriguez', '2024-01-10', 0.10, 60000.00, 7, 1, 7, 1),
       (7, 'Emily Williams', '2023-11-08', 0.00, 55000.00, 8, 5, 8, 3);

-- ajout de donnée aux 2 association car (1,N) de chaque coté 
INSERT INTO Effectue (id_employe, id_mission)
VALUES (1, 1); 

INSERT INTO Concerne (id_employe, id_contrat)
VALUES (1, 1);

/*---------------------------------------------*/

-- ouverture de la table DEPARTEMENT
SELECT * FROM DEPARTEMENT;
-- ouverture de la table EMPLOYE
SELECT * FROM EMPLOYE;
-- ouverture de la table CONTRAT
SELECT * FROM CONTRAT;
-- ouverture de la table CLIENT
SELECT * FROM CLIENT;
-- ouverture de la table LIVRABLE
SELECT * FROM LIVRABLE;
-- ouverture de la table QUALIFCATION
SELECT * FROM QUALIFICATION ;
-- ouverture de la table JOB
SELECT * FROM JOB;
-- nombre total d'employe
SELECT COUNT(*) FROM EMPLOYE;
-- Salaire moyen des employés du département Marketing
SELECT AVG(salaire) FROM EMPLOYE WHERE id_departement = 1;
-- Somme des commissions versées aux employés
SELECT SUM(commission) FROM EMPLOYE;
-- Salaire maximum des employés
SELECT MAX(salaire) FROM EMPLOYE;
-- Nombre de missions en cours
SELECT COUNT(*) FROM LIVRABLE WHERE date_livraison >= '2024-03-08';
-- Liste des clients et des qualifications requises pour leurs contrats
SELECT c.nom, q.nom FROM CLIENT c JOIN CONTRAT ct ON c.id_client = ct.id_client JOIN QUALIFICATION q ON ct.id_qualification = q.id_qualification;
-- Chiffre d'affaires par qualification des employés
SELECT q.nom, SUM(tarif) AS chiffre_affaire FROM QUALIFICATION q JOIN CONTRAT ct ON q.id_qualification = ct.id_qualification JOIN Concerne co ON ct.id_contrat = co.id_contrat JOIN EMPLOYE e ON co.id_employe = e.id_employe GROUP BY q.id_qualification;
-- Pour chaque département, afficher le nombre d'employés et la moyenne de leur salaire
SELECT d.nom, COUNT(*) AS nb_employes, AVG(e.salaire) AS salaire_moyen FROM DEPARTEMENT d JOIN EMPLOYE e ON d.id_departement = e.id_departement GROUP BY d.id_departement;
-- Liste des employés embauchés après le 1er janvier 2024
SELECT nom, date_embauche FROM EMPLOYE WHERE date_embauche > '2024-01-01';
-- Liste des missions dont le nom contient "développement"
SELECT nom FROM MISSION WHERE nom LIKE '%développement%';
-- Liste des contrat pour le client ABC clothing avec pour date de début 8 mars 2004
SELECT * FROM CONTRAT c JOIN CLIENT cl ON c.id_client = cl.id_client WHERE cl.nom = 'ABC Clothing' AND c.date_debut <= '2024-03-08';
-- Liste des employés ayant une commission supérieure à 10%
SELECT nom, commission FROM EMPLOYE WHERE commission > 0.1;
-- Trier les employés par ordre décroissant de salaire
SELECT nom, salaire FROM EMPLOYE ORDER BY salaire DESC;
-- Liste des employés qui n'ont pas encore effectué de mission
SELECT nom FROM EMPLOYE e WHERE NOT EXISTS (SELECT * FROM Effectue ef WHERE ef.id_employe = e.id_employe);
-- Liste des employés ayant participé à au moins deux missions
SELECT nom FROM EMPLOYE e JOIN Effectue ef ON e.id_employe = ef.id_employe GROUP BY e.id_employe HAVING COUNT(*) >= 2;
-- Liste des clients ayant un contrat avec un tarif supérieur à 10 000€
SELECT c.nom FROM CLIENT c JOIN CONTRAT ct ON c.id_client = ct.id_client WHERE ct.tarif > 10000;
-- Afficher les noms des employés et leur qualification, triés par qualification
SELECT e.nom, q.nom AS qualification
FROM EMPLOYE e
JOIN QUALIFICATION q ON e.id_qualification = q.id_qualification
ORDER BY q.nom;
-- Afficher le nombre de missions pour chaque employé
SELECT e.nom, COUNT(*) AS nb_missions
FROM EMPLOYE e
JOIN Effectue ef ON e.id_employe = ef.id_employe
GROUP BY e.id_employe;
-- Afficher les noms des missions et les noms des employés qui les effectuent
SELECT m.nom, e.nom
FROM MISSION m
JOIN Effectue ef ON m.id_mission = ef.id_mission
JOIN EMPLOYE e ON ef.id_employe = e.id_employe;
-- Afficher les informations des employés, de leurs départements et de leurs jobs
SELECT e.nom, d.nom AS departement, j.nom AS job
FROM EMPLOYE e
JOIN DEPARTEMENT d ON e.id_departement = d.id_departement
JOIN JOB j ON e.id_job = j.id_job;
-- Afficher toutes les combinaisons possibles d'employés et de clients
SELECT e.nom, c.nom
FROM EMPLOYE e, CLIENT c;
-- Afficher les noms des employés qui ont participé à au moins deux missions
SELECT e.nom
FROM EMPLOYE e
JOIN Effectue ef ON e.id_employe = ef.id_employe
GROUP BY e.id_employe
HAVING COUNT(*) >= 2;
-- Afficher le nom du département avec le plus grand nombre d'employés
SELECT d.nom
FROM DEPARTEMENT d
JOIN EMPLOYE e ON e.id_departement = d.id_departement
GROUP BY d.id_departement
ORDER BY COUNT(*) DESC
LIMIT 1;

-- auto jointure quel employé sont les responsables et de qui
SELECT e1.nom AS nom_responsable, e2.nom AS nom_employe
FROM EMPLOYE e1
LEFT JOIN EMPLOYE e2 ON e1.id_employe = e2.id_employe_1
WHERE e1.id_employe_1 IS NOT NULL;
