"""Unit tests for NimGame.

Author: JosephBany
Created: 2025-09-05
Collaborators: ChatGPT (AI assistant)
"""
import unittest

from nim21.game import NimGame
from nim21.exceptions import InvalidMoveError


class TestNimGame(unittest.TestCase):
    def test_init_defaults(self):
        g = NimGame()
        self.assertEqual(g.total_sticks, 21)
        self.assertEqual(g.max_take, 3)
        self.assertEqual(g.current_player, 0)
        self.assertEqual(g.remaining, 21)
        self.assertFalse(g.is_over())
        self.assertIsNone(g.winner())

    def test_legal_take_range(self):
        g = NimGame()
        self.assertEqual(list(g.legal_take_range()), [1, 2, 3])
        g.apply_move(3)  # 18 left
        for _ in range(5):  # take fifteen more -> 3 left
            g.apply_move(3)  # alternating players
        self.assertEqual(g.remaining, 3)
        self.assertEqual(list(g.legal_take_range()), [1, 2, 3])
        g.apply_move(2)  # 1 left
        self.assertEqual(list(g.legal_take_range()), [1])

    def test_invalid_moves(self):
        g = NimGame()
        with self.assertRaises(InvalidMoveError):
            g.apply_move(0)
        with self.assertRaises(InvalidMoveError):
            g.apply_move(4)
        with self.assertRaises(InvalidMoveError):
            g.apply_move(99)

    def test_cannot_take_more_than_remaining(self):
        g = NimGame(total_sticks=2, max_take=3)
        with self.assertRaises(InvalidMoveError):
            g.apply_move(3)
        # Legal move then illegal attempt
        g.apply_move(1)
        with self.assertRaises(InvalidMoveError):
            g.apply_move(2)

    def test_turns_and_winner(self):
        g = NimGame(total_sticks=5, max_take=3, starting_player=0)
        g.apply_move(1)  # P0 takes 1 -> 4 left
        self.assertEqual(g.current_player, 1)
        g.apply_move(3)  # P1 takes 3 -> 1 left
        self.assertEqual(g.current_player, 0)
        g.apply_move(1)  # P0 takes last -> 0 left
        self.assertTrue(g.is_over())
        self.assertEqual(g.winner(), 0)

    def test_reset(self):
        g = NimGame()
        g.apply_move(2)
        g.reset()
        self.assertEqual(g.remaining, g.total_sticks)
        self.assertEqual(g.history, [])


if __name__ == "__main__":
    unittest.main()
