import mysql from 'mysql2/promise';

const connection = await mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'PROJECT',
});

export async function getUsers() {
    const [rows] = await connection.execute('SELECT u.id_utilisateur, nom, email, role, COUNT(DISTINCT e.id_jeu) AS nb_evaluations, COUNT(DISTINCT l.id_jeu) AS nb_locations FROM Utilisateur u LEFT JOIN Evaluation e ON u.id_utilisateur = e.id_utilisateur LEFT JOIN Location l ON u.id_utilisateur = l.id_utilisateur GROUP BY u.id_utilisateur');
    return rows;
}

export async function getUser(email, password) {
    const [rows] = await connection.execute('SELECT id_utilisateur, nom, email, role FROM Utilisateur WHERE email = ? AND mot_de_passe = ?', [email, password]);
    return rows[0];
}

export async function createUser(name, email, password, role) {
    const [result] = await connection.execute('INSERT INTO Utilisateur (nom, email, mot_de_passe, role) VALUES (?, ?, ?, ?)', [name, email, password, role]);
    return result.insertId;
}

export async function updateUser(id, name, email, password, role) {
    // Update only the fields that are provided
    const updates = [];
    const params = [];
    if (name) {
        updates.push('nom = ?');
        params.push(name);
    }
    if (email) {
        updates.push('email = ?');
        params.push(email);
    }
    if (password) {
        updates.push('mot_de_passe = ?');
        params.push(password);
    }
    if (role) {
        updates.push('role = ?');
        params.push(role);
    }
    if (updates.length === 0) {
        throw new Error('No fields to update');
    }
    params.push(id);
    const query = `UPDATE Utilisateur SET ${updates.join(', ')} WHERE id_utilisateur = ?`;
    const [result] = await connection.execute(query, params);
    return result.affectedRows > 0;
}

export async function deleteUser(id) {
    const [result] = await connection.execute('DELETE FROM Utilisateur WHERE id_utilisateur = ?', [id]);
    return result.affectedRows > 0;
}

// Fonctions jeux

// Récupérer 10 jeux les mieux notés
export async function getTopRatedGames() {
    const [rows] = await connection.execute('SELECT * FROM Jeu ORDER BY note_moyenne DESC LIMIT 10');
    return rows;
}

// Récupérer un jeu par id, avec ses catégories et mécaniques
export async function getGameById(id) {
    const [rows] = await connection.execute(`
        SELECT j.*, GROUP_CONCAT(DISTINCT c.nom) AS categories, GROUP_CONCAT(DISTINCT m.nom) AS mecanique
        FROM Jeu j
        LEFT JOIN Jeu_Categorie jc ON j.id_jeu = jc.id_jeu
        LEFT JOIN Categorie c ON jc.id_categorie = c.id_categorie
        LEFT JOIN Jeu_Mecanique jm ON j.id_jeu = jm.id_jeu
        LEFT JOIN Mecanique m ON jm.id_mecanique = m.id_mecanique
        WHERE j.id_jeu = ?
        GROUP BY j.id_jeu
    `, [id]);
    if (rows.length === 0) {
        throw new Error('Game not found');
    }
    return {
        ...rows[0],
        categories: rows[0].categories ? rows[0].categories.split(',') : [],
        mecanique: rows[0].mecanique ? rows[0].mecanique.split(',') : [],
    };
}

// Rechercher un jeu par nom, catégorie ou mécanique
// Utiliser la table Jeu, Categorie et la jointure Jeu_Categorie, Mecanique et la jointure Jeu_Mecanique
export async function searchGames(query) {
    const [rows] = await connection.execute(`
        SELECT DISTINCT j.*, GROUP_CONCAT(DISTINCT c.nom) AS categories, GROUP_CONCAT(DISTINCT m.nom) AS mecanique
        FROM Jeu j
        LEFT JOIN Jeu_Categorie jc ON j.id_jeu = jc.id_jeu
        LEFT JOIN Categorie c ON jc.id_categorie = c.id_categorie
        LEFT JOIN Jeu_Mecanique jm ON j.id_jeu = jm.id_jeu
        LEFT JOIN Mecanique m ON jm.id_mecanique = m.id_mecanique
        WHERE j.nom LIKE ? OR c.nom LIKE ? OR m.nom LIKE ?
        GROUP BY j.id_jeu
    `, [`%${query}%`, `%${query}%`, `%${query}%`]);
    return rows.map(row => ({
        ...row,
        categories: row.categories ? row.categories.split(',') : [],
        mecanique: row.mecanique ? row.mecanique.split(',') : [],
    }));
}

export async function getRentedGames(userId) {
    const [rows] = await connection.execute(`
        SELECT j.*, l.date_location, l.date_retour FROM Jeu j
        JOIN Location l ON j.id_jeu = l.id_jeu
        WHERE l.id_utilisateur = ? AND l.date_retour IS NULL
    `, [userId]);
    return rows;
}

// Récupérer les jeux disponibles (utiliser la view)
export async function getAvailableGames() {
    const [rows] = await connection.execute('SELECT * FROM Jeux_Disponibles');
    return rows;
}

export async function getAllGames() {
    const [rows] = await connection.execute(`
        SELECT j.*, GROUP_CONCAT(DISTINCT c.nom) AS categories, GROUP_CONCAT(DISTINCT m.nom) AS mecanique
        FROM Jeu j
        LEFT JOIN Jeu_Categorie jc ON j.id_jeu = jc.id_jeu
        LEFT JOIN Categorie c ON jc.id_categorie = c.id_categorie
        LEFT JOIN Jeu_Mecanique jm ON j.id_jeu = jm.id_jeu
        LEFT JOIN Mecanique m ON jm.id_mecanique = m.id_mecanique
        GROUP BY j.id_jeu
    `);
    return rows.map(row => ({
        ...row,
        categories: row.categories ? row.categories.split(',') : [],
        mecanique: row.mecanique ? row.mecanique.split(',') : [],
    }));
}

// Fonctions location

// Vérifier état d'un jeu
export async function checkGameStatus(userId, gameId) {
    const [rows] = await connection.execute('SELECT * FROM Location WHERE id_jeu = ? AND date_retour IS NULL', [gameId]);
    if (rows.length > 0) {
        return { status: 'rented', byMe: parseInt(userId) === rows[0].id_utilisateur };
    }
    return { status: 'available' };
}

// Louer un jeu
export async function rentGame(userId, gameId) {
    const [result] = await connection.execute('INSERT INTO Location (id_utilisateur, id_jeu, date_location, statut) VALUES (?, ?, NOW(), ?)', [userId, gameId, 'en cours']);
    return result.insertId;
}

// Rendre un jeu (utiliser la procédure stockée MarquerRetourJeu)
export async function returnGame(userId, gameId) {
    // get location id
    const [rows] = await connection.execute('SELECT id_location FROM Location WHERE id_utilisateur = ? AND id_jeu = ? AND date_retour IS NULL', [userId, gameId]);
    if (rows.length === 0) {
        throw new Error('Location not found');
    }
    const locationId = rows[0].id_location;
    // call stored procedure
    const [result] = await connection.execute('CALL MarquerRetourJeu(?)', [locationId]);
    if (result.affectedRows === 0) {
        throw new Error('Error marking game as returned');
    }
    return result.affectedRows > 0;
}

// Fonctions evaluation

// Ajouter une évaluation (utilier la procédure stockée AjouterEvaluation)
export async function addReview(userId, gameId, rating, comment) {
    const [result] = await connection.execute('CALL AjouterEvaluation(?, ?, ?, ?)', [userId, gameId, rating, comment]);
    return result.insertId;
}

// Récupérer les évaluations d'un jeu
export async function getReviewsByGameId(gameId) {
    const [rows] = await connection.execute('SELECT e.*, u.nom FROM Evaluation e JOIN Utilisateur u ON e.id_utilisateur = u.id_utilisateur WHERE e.id_jeu = ?', [gameId]);
    return rows;
}

// Supprimer une évaluation
export async function deleteReview(userId, gameId) {
    const [result] = await connection.execute('DELETE FROM Evaluation WHERE id_utilisateur = ? AND id_jeu = ?', [userId, gameId]);
    return result.affectedRows > 0;
}

// Mettre à jour une évaluation
export async function updateReview(userId, gameId, rating, comment) {
    const [result] = await connection.execute('UPDATE Evaluation SET note = ?, commentaire = ? WHERE id_utilisateur = ? AND id_jeu = ?', [rating, comment, userId, gameId]);
    return result.affectedRows > 0;
}
