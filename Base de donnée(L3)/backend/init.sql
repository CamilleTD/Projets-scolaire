DROP DATABASE IF EXISTS PROJECT;
CREATE DATABASE PROJECT;
USE PROJECT;

CREATE TABLE Jeu
(
    id_jeu INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    description TEXT,
    annee_sortie INT,
    age_minimum INT,
    nombre_joueurs_min INT,
    nombre_joueurs_max INT,
    duree_moyenne INT,
    editeur VARCHAR(255),
    note_moyenne FLOAT DEFAULT 0
);

CREATE TABLE Utilisateur
(
    id_utilisateur INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    mot_de_passe VARCHAR(255),
    role ENUM('Administrateur', 'Membre')
);

CREATE TABLE Categorie
(
    id_categorie INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255)
);

CREATE TABLE Mecanique
(
    id_mecanique INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255)
);

CREATE TABLE Jeu_Categorie
(
    id_jeu INT,
    id_categorie INT,
    PRIMARY KEY (id_jeu, id_categorie),
    FOREIGN KEY (id_jeu) REFERENCES Jeu(id_jeu),
    FOREIGN KEY (id_categorie) REFERENCES Categorie(id_categorie)
);

CREATE TABLE Jeu_Mecanique
(
    id_jeu INT,
    id_mecanique INT,
    PRIMARY KEY (id_jeu, id_mecanique),
    FOREIGN KEY (id_jeu) REFERENCES Jeu(id_jeu),
    FOREIGN KEY (id_mecanique) REFERENCES Mecanique(id_mecanique)
);

CREATE TABLE Evaluation
(
    id_utilisateur INT,
    id_jeu INT,
    note INT,
    commentaire TEXT,
    date DATE,
    PRIMARY KEY (id_utilisateur, id_jeu),
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateur(id_utilisateur),
    FOREIGN KEY (id_jeu) REFERENCES Jeu(id_jeu)
);

CREATE TABLE Location
(
    id_location INT PRIMARY KEY AUTO_INCREMENT,
    id_utilisateur INT,
    id_jeu INT,
    date_location DATE,
    date_retour DATE,
    statut ENUM('en cours', 'retourné'),
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateur(id_utilisateur),
    FOREIGN KEY (id_jeu) REFERENCES Jeu(id_jeu)
);

DELIMITER $$

-- Création de la procédure stockée AddLocationAndEvaluation
DELIMITER $$

CREATE PROCEDURE AddLocationAndEvaluation (
    IN p_id_utilisateur INT,
    IN p_id_jeu INT,
    IN p_note INT,
    IN p_commentaire TEXT
)
BEGIN
    -- Déclaration de la variable pour stocker la moyenne de la note
    DECLARE moyenne_note FLOAT;

    -- Enregistrement de la location
    INSERT INTO Location (id_utilisateur, id_jeu, date_location, date_retour, statut)
    VALUES (p_id_utilisateur, p_id_jeu, CURDATE(), NULL, 'en cours');

    -- Enregistrement de l'évaluation
    INSERT INTO Evaluation (id_utilisateur, id_jeu, note, commentaire, date)
    VALUES (p_id_utilisateur, p_id_jeu, p_note, p_commentaire, CURDATE());

    -- Mise à jour de la note moyenne du jeu
    SELECT AVG(note) INTO moyenne_note
    FROM Evaluation
    WHERE id_jeu = p_id_jeu;

    UPDATE Jeu
    SET note_moyenne = moyenne_note
    WHERE id_jeu = p_id_jeu;
END $$

DELIMITER ;

-- Insérer des utilisateurs
INSERT INTO Utilisateur (id_utilisateur, nom, role) VALUES
(1, 'Alice Dupont', 'Membre'),
(2, 'Bob Martin', 'Membre'),
(3, 'Claire Lemoine', 'Administrateur'),
(4, 'David Tissot', 'Membre'),
(5, 'Eva Lefevre', 'Membre');

-- Insérer des jeux
INSERT INTO Jeu (id_jeu, nom, description, annee_sortie) VALUES
(1, 'Catan', 'Jeu de société de stratégie où les joueurs colonisent une île.', 1995),
(2, 'Monopoly', 'Jeu de société classique sur l\'achat de propriétés.', 1935),
(3, 'Pandemic', 'Jeu coopératif où les joueurs travaillent ensemble pour stopper une pandémie.', 2008),
(4, 'Carcassonne', 'Jeu de placement de tuiles pour construire des paysages médiévaux.', 2000),
(5, 'Ticket to Ride', 'Jeu de stratégie où les joueurs construisent des chemins de fer à travers le pays.', 2004);

-- Insérer des catégories
INSERT INTO Categorie (id_categorie, nom) VALUES
(1, 'Stratégie'),
(2, 'Familial'),
(3, 'Coopératif');

-- Insérer des mécaniques
INSERT INTO Mecanique (id_mecanique, nom) VALUES
(1, 'Placement d\'ouvriers'),
(2, 'Déduction'),
(3, 'Gestion de ressources');

-- Associer jeux et catégories
INSERT INTO Jeu_Categorie (id_jeu, id_categorie) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 2),
(5, 2);

-- Associer jeux et mécaniques
INSERT INTO Jeu_Mecanique (id_jeu, id_mecanique) VALUES
(1, 1),
(2, 3),
(3, 3),
(4, 1),
(5, 2);

-- Insérer des évaluations
INSERT INTO Evaluation (id_utilisateur, id_jeu, note, commentaire, date) VALUES
(1, 1, 8, 'Très bon jeu de stratégie', '2024-01-15'),
(2, 2, 7, 'Classique mais un peu long', '2024-02-10'),
(3, 3, 9, 'Super jeu coopératif, vraiment immersif', '2024-03-05');

-- Insérer des locations
INSERT INTO Location (id_location, id_utilisateur, id_jeu, date_location, date_retour, statut) VALUES
(1, 1, 1, '2024-04-01', '2024-04-10', 'Retourné'),
(2, 2, 4, '2024-04-02', '2024-04-15', 'Retourné'),
(3, 3, 5, '2024-04-05', '2024-04-12', 'Retourné');



-- FONCTIONS AVANCEES

-- Vues
-- Vue des jeux disponibles
CREATE VIEW Jeux_Disponibles AS
SELECT j.nom
FROM Jeu j
WHERE j.id_jeu NOT IN (SELECT id_jeu FROM Location WHERE statut = 'en cours');

-- Vue des évaluations des jeux
CREATE VIEW Evaluations_Jeux AS
SELECT u.nom AS utilisateur, j.nom AS jeu, e.note, e.commentaire
FROM Evaluation e
JOIN Utilisateur u ON u.id_utilisateur = e.id_utilisateur
JOIN Jeu j ON j.id_jeu = e.id_jeu;

-- Index
-- Index sur le nom des jeux pour accélérer les recherches
CREATE INDEX idx_jeu_nom ON Jeu(nom);

-- Index sur le statut de location pour améliorer les performances des requêtes sur les locations en cours
CREATE INDEX idx_location_statut ON Location(statut);

-- Triggers
-- Trigger pour empêcher la location de plusieurs fois du même jeu sans retour
CREATE TRIGGER prevent_multiple_rentals
BEFORE INSERT ON Location
FOR EACH ROW
BEGIN
  IF EXISTS (SELECT 1 FROM Location WHERE id_utilisateur = NEW.id_utilisateur AND id_jeu = NEW.id_jeu AND statut = 'en cours') THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Jeu déjà loué par cet utilisateur';
  END IF;
END;

-- Trigger pour mettre à jour automatiquement le statut de la location à "retourné" si la date de retour est renseignée
CREATE TRIGGER auto_update_statut
BEFORE UPDATE ON Location
FOR EACH ROW
BEGIN
  IF NEW.date_retour IS NOT NULL THEN
    SET NEW.statut = 'retourné';
  END IF;
END;

-- Procédures stockées
-- Procédure pour ajouter une évaluation
CREATE PROCEDURE AjouterEvaluation(IN utilisateur_id INT, IN jeu_id INT, IN note_val INT, IN com TEXT)
BEGIN
  INSERT INTO Evaluation(id_utilisateur, id_jeu, note, commentaire, date)
  VALUES (utilisateur_id, jeu_id, note_val, com, CURDATE());
END;

-- Procédure pour marquer le retour d'un jeu
CREATE PROCEDURE MarquerRetourJeu(IN location_id INT)
BEGIN
  UPDATE Location SET date_retour = CURDATE(), statut = 'retourné'
  WHERE id_location = location_id;
END;

-- update jeu average note
CREATE TRIGGER update_jeu_average_note
AFTER INSERT ON Evaluation
FOR EACH ROW
BEGIN
    DECLARE moyenne_note FLOAT;

    SELECT AVG(note) INTO moyenne_note
    FROM Evaluation
    WHERE id_jeu = NEW.id_jeu;

    UPDATE Jeu
    SET note_moyenne = moyenne_note
    WHERE id_jeu = NEW.id_jeu;
END;

DELIMITER ;
