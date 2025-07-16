import express from 'express';
import {
  addReview,
  getReviewsByGameId,
  deleteReview,
  updateReview
} from '../db.js';

const router = express.Router();

router.get('/:gameId', async (req, res) => {
  try {
    const reviews = await getReviewsByGameId(req.params.gameId);
    res.json(reviews);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.post('/', async (req, res) => {
  const { userId, gameId, rating, comment } = req.body;
  try {
    const id = await addReview(userId, gameId, rating, comment);
    res.status(201).json({ reviewId: id });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.put('/', async (req, res) => {
  const { userId, gameId, rating, comment } = req.body;
  try {
    const updated = await updateReview(userId, gameId, rating, comment);
    res.json({ updated });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.delete('/', async (req, res) => {
  const { userId, gameId } = req.body;
  try {
    const deleted = await deleteReview(userId, gameId);
    res.json({ deleted });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

export default router;
