import unittest
import chess
import pygame
from unittest.mock import patch
from main import GameState, CoordinateConverter, Config


class TestGameState(unittest.TestCase):
    def setUp(self):
        self.game_state = GameState()

    def test_initial_board_setup(self):
        self.assertTrue(self.game_state.board.is_fen_valid(self.game_state.board.fen()))
        self.assertFalse(self.game_state.board.is_game_over())

    def test_valid_pawn_move(self):
        move = chess.Move.from_uci("e2e4")
        self.assertIn(move, self.game_state.board.legal_moves)
        self.game_state.board.push(move)
        self.assertEqual(self.game_state.board.piece_at(chess.E4).symbol(), 'P')

    def test_invalid_move(self):
        move = chess.Move.from_uci("e2e5")  # Pawns can't move two squares unless from starting position
        self.assertNotIn(move, self.game_state.board.legal_moves)

    def test_capture_move(self):
        self.game_state.board.set_fen("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")
        move = chess.Move.from_uci("d7d5")
        self.game_state.board.push(move)
        capture_move = chess.Move.from_uci("e4d5")
        self.assertIn(capture_move, self.game_state.board.legal_moves)
        self.game_state.board.push(capture_move)
        self.assertEqual(self.game_state.board.piece_at(chess.D5).symbol(), 'P')


class TestCoordinateConverter(unittest.TestCase):
    def setUp(self):
        self.converter = CoordinateConverter(Config.SQUARE_SIZE)

    def test_coords_to_square(self):
        self.assertEqual(self.converter.coords_to_square((0, Config.BOARD_OFFSET)), chess.A8)
        self.assertEqual(self.converter.coords_to_square((Config.SQUARE_SIZE * 4, Config.BOARD_OFFSET + Config.SQUARE_SIZE * 4)), chess.E4)

    def test_square_to_coords(self):
        self.assertEqual(self.converter.square_to_coords(chess.A8), (0, 0))
        self.assertEqual(self.converter.square_to_coords(chess.E4), (Config.SQUARE_SIZE * 4, Config.SQUARE_SIZE * 4))


if __name__ == "__main__":
    unittest.main()
