-- Création de la base de donnée
DROP DATABASE if exists `Gestion_employe`;
create schema `Gestion_employe`;
use Gestion_employe;

-- Création de la table DEPARTEMENT
CREATE TABLE DEPARTEMENT(
   id_departement INT,
   nom VARCHAR(255) NOT NULL,
   PRIMARY KEY(id_departement),
   UNIQUE(nom)
);

-- Création de la table JOB
CREATE TABLE JOB(
   id_job INT,
   nom VARCHAR(255) NOT NULL,
   PRIMARY KEY(id_job),
   UNIQUE(nom)
);

-- Création de la table MISSION
CREATE TABLE MISSION(
   id_mission INT,
   nom VARCHAR(255) NOT NULL,
   description VARCHAR(255) NOT NULL,
   PRIMARY KEY(id_mission),
   UNIQUE(nom)
);

-- Création de la table LIVRABLE
CREATE TABLE LIVRABLE(
   id_livrable INT,
   nom VARCHAR(255) NOT NULL,
   description VARCHAR(255) NOT NULL,
   date_livraison DATE NOT NULL,
   id_mission INT NOT NULL,
   PRIMARY KEY(id_livrable),
   FOREIGN KEY(id_mission) REFERENCES MISSION(id_mission)
);

-- Création de la table CLIENT
CREATE TABLE CLIENT(
   id_client INT,
   nom VARCHAR(255) NOT NULL,
   adresse VARCHAR(255) NOT NULL,
   PRIMARY KEY(id_client),
   UNIQUE(nom)
);

-- Création de la table QUALIFICATION
CREATE TABLE QUALIFICATION(
   id_qualification INT,
   nom VARCHAR(255) NOT NULL,
   PRIMARY KEY(id_qualification),
   UNIQUE(nom)
);

-- Création de la table EMPLOYE
CREATE TABLE EMPLOYE(
   id_employe INT,
   nom VARCHAR(255) NOT NULL,
   date_embauche DATE NOT NULL,
   commission DECIMAL(10,2) NOT NULL,
   salaire DECIMAL(10,2) NOT NULL,
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

-- Création de la table CONTRAT
CREATE TABLE CONTRAT(
   id_contrat INT,
   description_intervenant VARCHAR(255) NOT NULL,
   date_debut DATE NOT NULL,
   tarif DECIMAL(10,2) NOT NULL,
   id_qualification INT NOT NULL,
   id_client INT NOT NULL,
   PRIMARY KEY(id_contrat),
   FOREIGN KEY(id_qualification) REFERENCES QUALIFICATION(id_qualification),
   FOREIGN KEY(id_client) REFERENCES CLIENT(id_client)
);

-- Création de la table Effectue (car lors de la cardinalités (1,n) de chaque coté)
CREATE TABLE Effectue(
   id_employe INT,
   id_mission INT,
   PRIMARY KEY(id_employe, id_mission),
   FOREIGN KEY(id_employe) REFERENCES EMPLOYE(id_employe),
   FOREIGN KEY(id_mission) REFERENCES MISSION(id_mission)
);

-- Création de la table Concerne (car lors de la cardinalités (1,n) de chaque coté)
CREATE TABLE Concerne(
   id_employe INT,
   id_contrat INT,
   PRIMARY KEY(id_employe, id_contrat),
   FOREIGN KEY(id_employe) REFERENCES EMPLOYE(id_employe),
   FOREIGN KEY(id_contrat) REFERENCES CONTRAT(id_contrat)
);

