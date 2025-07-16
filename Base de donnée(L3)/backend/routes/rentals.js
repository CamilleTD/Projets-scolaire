import express from 'express';
import {checkGameStatus, getRentedGames, rentGame, returnGame} from '../db.js';

const router = express.Router();

router.get('/status/:userId/:gameId', async (req, res) => {
    const { userId, gameId } = req.params;
    try {
        const rented = await checkGameStatus(userId, gameId);
        res.json(rented);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

router.post('/rent', async (req, res) => {
  const { userId, gameId } = req.body;
  try {
    const id = await rentGame(userId, gameId);
    res.status(201).json({ rentalId: id });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.post('/return', async (req, res) => {
  const { userId, gameId } = req.body;
  try {
    const success = await returnGame(userId, gameId);
    res.json({ returned: success });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

export default router;
