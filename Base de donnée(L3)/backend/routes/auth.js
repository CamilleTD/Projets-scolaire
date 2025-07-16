import express from 'express';
import { getUser, createUser } from '../db.js';

const router = express.Router();

router.post('/login', (req, res) => {
    const { email, password } = req.body;

    if (!email || !password) {
        return res.status(400).send('Email and password are required');
    }

    getUser(email, password)
        .then(user => {
            if (user) {
                res.send({
                    ...user,
                    mot_de_passe: undefined,
                });
            } else {
                res.status(401).send('Invalid email or password');
            }
        })
        .catch(error => {
            console.error(error);
            res.status(500).send('Error fetching user');
        });
});

router.post('/register', async (req, res) => {
  const { name, email, password } = req.body;
  try {
    const id = await createUser(name, email, password, 'Membre');
    res.status(201).json({ id });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

export default router;
