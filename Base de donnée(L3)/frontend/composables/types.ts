export interface UserInfo {
    id_utilisateur: number
    nom: string
    email: string
    role: 'Administrateur' | 'Membre'
    nb_evaluations?: number
    nb_locations?: number
}

export interface Game {
    id_jeu: number
    nom: string
    description: string
    annee_sortie: string
    age_minimum: number
    nombre_joueurs_min: number
    nombre_joueurs_max: number
    duree_moyenne: number
    editeur: string
    note_moyenne: number

    categories: string[]
    mecanique: string[]

    // Optional properties
    date_location?: string
    date_retour?: string
    statut?: string
}

export interface Evaluation {
    commentaire: string
    date: string
    id_jeu: number
    id_utilisateur: number
    nom: string
    note: number
}