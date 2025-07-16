import igdb from 'igdb-api-node';
import axios from 'axios';

async function getAccessToken() {
    return await axios.post('https://id.twitch.tv/oauth2/token', null, {
        params: {
            client_id: process.env.TWITCH_CLIENT_ID,
            client_secret: process.env.TWITCH_CLIENT_SECRET,
            grant_type: 'client_credentials',
        },
    }).then(response => response.data);
}

let accessToken = null;

async function refreshToken() {
    const data = await getAccessToken();
    accessToken = data.access_token;
    setTimeout(refreshToken, (data.expires_in - 60));
}
refreshToken();

// const client = igdb.default(process.env.TWITCH_CLIENT_ID, process.env.TWITCH_APP_ACCESS_TOKEN);

export async function getImage(name, width, height) {
    const gameResponse = await igdb.default(process.env.TWITCH_CLIENT_ID, accessToken)
        .fields('cover')
        .where(`name="${name}"`)
        .limit(1)
        .request('games');

    const coverId = gameResponse.data[0]?.cover;
    if (!coverId) {
        throw new Error('No cover found');
    }

    const coverResponse = await igdb.default(process.env.TWITCH_CLIENT_ID, accessToken)
        .fields('url')
        .where(`id=${coverId}`)
        .request('covers');

    const coverUrl = coverResponse.data[0]?.url;
    if (!coverUrl) {
        throw new Error('No cover URL found');
    }
    return coverUrl.replace('t_thumb', `t_cover_big`).replace('t_720p', `t_${width}x${height}`);
}