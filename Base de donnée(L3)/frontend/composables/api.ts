export async function getGameImage(label: string) {
    const response = await fetch(
        `${useRuntimeConfig().public.apiUrl}/igdb/img/${label}`,
        {
            method: 'GET',
            headers: {
                Accept: 'application/json',
            },
        },
    )
    return await response.json().then((data) => data.url)
}

// AUTH
export async function login(email: string, password: string) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
    });
    return await res.json();
}

export async function register(name: string, email: string, password: string) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password }),
    });
    return await res.json();
}

// USERS
export async function getUsers() {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/users/`);
    return await res.json() as UserInfo[];
}

export async function createUser(name: string, email: string, password: string, role: 'Administrateur' | 'Membre') {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/users/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password, role }),
    });
    return await res.json();
}

export async function updateUser(id: number, name: string | undefined, email: string | undefined, password: string | undefined, role: 'Administrateur' | 'Membre') {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/users/${id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password, role }),
    });
    return await res.json();
}

export async function deleteUser(id: number) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/users/${id}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
    });
    return await res.json();
}

// GAMES
export async function getTopRatedGames() {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/games/top-rated`);
    return await res.json() as Game[];
}

export async function getRentedGames(userId: number) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/games/rented/${userId}`);
    return await res.json() as Game[];
}

export async function getAvailableGames() {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/games/available`);
    return await res.json() as Game[];
}

export async function searchGames(query: string) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/games/search?q=${encodeURIComponent(query)}`);
    return await res.json() as Game[];
}

export async function getGameById(id: number) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/games/${id}`);
    return await res.json() as Game;
}

export async function getAllGames() {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/games/`);
    return await res.json() as Game[];
}

// RENTALS
export async function checkGameStatus(userId: number, gameId: number) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/rentals/status/${userId}/${gameId}`);
    return await res.json() as { status: 'available' | 'rented', byMe?: boolean };
}

export async function rentGame(userId: number, gameId: number) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/rentals/rent`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userId, gameId }),
    });
    return await res.json();
}

export async function returnGame(userId: number, gameId: number) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/rentals/return`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userId, gameId }),
    });
    return await res.json();
}

// REVIEWS
export async function getReviewsByGameId(gameId: number) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/reviews/${gameId}`);
    return await res.json();
}

export async function addReview(userId: number, gameId: number, rating: number, comment: string) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/reviews`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userId, gameId, rating, comment }),
    });
    return await res.json();
}

export async function updateReview(userId: number, gameId: number, rating: number, comment: string) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/reviews`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userId, gameId, rating, comment }),
    });
    return await res.json();
}

export async function deleteReview(userId: number, gameId: number) {
    const res = await fetch(`${useRuntimeConfig().public.apiUrl}/reviews`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userId, gameId }),
    });
    return await res.json();
}
