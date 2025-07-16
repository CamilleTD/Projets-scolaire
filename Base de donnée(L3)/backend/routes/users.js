import express from 'express';
import { getUsers, createUser, updateUser, deleteUser } from '../db.js';

const router = express.Router();

router.get('/', async (req, res) => {
    try {
        const users = await getUsers();
        res.json(users);
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching users');
    }
})

router.post('/', async (req, res) => {
    const { name, email, password, role } = req.body;

    if (!name || !email || !password || !role) {
        return res.status(400).send('Name, email, password and role are required');
    }

    try {
        const id = await createUser(name, email, password, role);
        res.status(201).json({ id });
    } catch (error) {
        console.error(error);
        res.status(500).send('Error creating user');
    }
})

router.patch('/:id', async (req, res) => {
    const { id } = req.params;
    const { name, email, password, role } = req.body;

    if (!name && !email && !password && !role) {
        return res.status(400).send('At least one field is required');
    }

    try {
        await updateUser(id, name, email, password, role);
        res.status(200).send({success: true, message: 'User updated successfully'});
    } catch (error) {
        console.error(error);
        res.status(500).send('Error updating user');
    }
});

router.delete('/:id', async (req, res) => {
    const { id } = req.params;

    if (!id) {
        return res.status(400).send('User ID is required');
    }

    try {
        await deleteUser(id);
        res.status(200).send({success: true, message: 'User deleted successfully'});
    } catch (error) {
        console.error(error);
        res.status(500).send('Error deleting user');
    }
})

export default router;
