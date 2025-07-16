import express from 'express';
import cors from 'cors';
import * as db from './db.js';
import { getImage } from './igdb.js';
import {expressjwt} from "express-jwt";
import authRouter from './routes/auth.js';
import gamesRouter from './routes/games.js';
import reviewsRouter from './routes/reviews.js';
import rentalsRouter from './routes/rentals.js';
import usersRouter from './routes/users.js';

const PORT = process.env.PORT || 8080;
const HOST = process.env.HOST || '0.0.0.0';

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(cors({
    origin: '*'
}));

app.use(expressjwt({
    secret: process.env.JWT_SECRET,
    algorithms: ["HS256"],
    credentialsRequired: false,
}))

app.use('/auth', authRouter);
app.use('/games', gamesRouter);
app.use('/reviews', reviewsRouter);
app.use('/rentals', rentalsRouter);
app.use('/users', usersRouter);

app.get('/igdb/img/:name', async (req, res) => {
    const { name } = req.params;
    const { width, height } = req.query;

    if (!name) {
        return res.status(400).send('Game name is required');
    }

    try {
        const imageUrl = await getImage(name, width, height);
        res.send({url: imageUrl});
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching image');
    }
})

app.listen(PORT, HOST, () => {
    console.log(`Server is running on http://${HOST}:${PORT}`);
});
