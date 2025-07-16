import express from 'express';
import {
  getTopRatedGames,
  getGameById,
  searchGames,
  getRentedGames,
  getAvailableGames,
  getAllGames,
} from '../db.js';

const router = express.Router();

router.get('/top-rated', async (req, res) => {
  try {
    const games = await getTopRatedGames();
    res.json(games);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.get('/available', async (req, res) => {
  try {
    const games = await getAvailableGames();
    res.json(games);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.get('/rented/:userId', async (req, res) => {
    try {
        const games = await getRentedGames(req.params.userId);
        res.json(games);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
})

router.get('/search', async (req, res) => {
  try {
    const games = await searchGames(req.query.q || '');
    res.json(games);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.get('/:id', async (req, res) => {
  try {
    const game = await getGameById(req.params.id);
    if (game) res.json(game);
    else res.status(404).json({ error: 'Game not found' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.get('/', async (req, res) => {
    try {
        const games = await getAllGames();
        res.json(games);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
})

export default router;
