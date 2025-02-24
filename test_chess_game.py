import unittest
import chess
import pygame
from two_player_game import ChessGame, GameState, CoordinateConverter, Colors, Config, ChessRenderer
from play_as_white_vs_ai import ChessAI


class TestChessGame(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        pygame.init()
        self.game_state = GameState()
        self.coords_converter = CoordinateConverter(Config.SQUARE_SIZE)

    def test_initial_board_setup(self):
        """Test that the board is properly initialized."""
        self.assertEqual(str(self.game_state.board.piece_at(chess.E1)), 'K')  # White king
        self.assertEqual(str(self.game_state.board.piece_at(chess.E8)), 'k')  # Black king
        self.assertEqual(str(self.game_state.board.piece_at(chess.D1)), 'Q')  # White queen
        self.assertEqual(str(self.game_state.board.piece_at(chess.D8)), 'q')  # Black queen

    def test_coordinate_conversion(self):
        """Test coordinate conversion between screen and board coordinates."""
        # Test conversion from screen coordinates to board square
        screen_pos = (0, Config.BOARD_OFFSET)  # Top-left of board
        square = self.coords_converter.coords_to_square(screen_pos)
        self.assertEqual(square, chess.A8)

        # Test conversion from board square to screen coordinates
        coords = self.coords_converter.square_to_coords(chess.E4)
        expected_x = 4 * Config.SQUARE_SIZE  # E file is index 4
        expected_y = 4 * Config.SQUARE_SIZE  # Rank 4 from bottom
        self.assertEqual(coords, (expected_x, expected_y))

    def test_valid_pawn_moves(self):
        """Test that pawns have correct valid moves from starting position."""
        # White pawn at e2
        e2_square = chess.E2
        self.game_state.selected_square = e2_square
        self.game_state.valid_moves = [move.to_square for move in self.game_state.board.legal_moves
                                       if move.from_square == e2_square]

        # Pawn should be able to move one or two squares forward from starting position
        self.assertIn(chess.E3, self.game_state.valid_moves)
        self.assertIn(chess.E4, self.game_state.valid_moves)
        self.assertEqual(len(self.game_state.valid_moves), 2)

    def test_chess_ai_evaluation(self):
        """Test that the AI can evaluate basic positions."""
        ai = ChessAI()
        # Test initial position evaluation
        initial_score = ai.evaluate_position(chess.Board())
        self.assertEqual(initial_score, 0)  # Initial position should be equal

        # Test position with extra white pawn
        board = chess.Board()
        board.remove_piece_at(chess.E7)  # Remove black pawn
        score_with_advantage = ai.evaluate_position(board)
        self.assertLess(score_with_advantage, 0)  # White should be better

    def test_game_state_initialization(self):
        """Test initial game state properties."""
        self.assertIsNone(self.game_state.selected_square)
        self.assertEqual(len(self.game_state.valid_moves), 0)
        self.assertTrue(self.game_state.board.turn)  # White to move
        self.assertFalse(self.game_state.board.is_game_over())

    def test_colors_constants(self):
        """Test that color constants are properly defined."""
        self.assertEqual(len(Colors.BROWN), 3)  # RGB tuple
        self.assertEqual(len(Colors.GREEN), 3)
        self.assertEqual(len(Colors.HIGHLIGHT), 4)  # RGBA tuple
        self.assertEqual(len(Colors.VALID_MOVE), 4)

    def test_config_values(self):
        """Test that configuration values are properly set."""
        self.assertEqual(Config.WINDOW_SIZE, 600)
        self.assertEqual(Config.BOARD_OFFSET, 40)
        self.assertEqual(Config.SQUARE_SIZE, Config.WINDOW_SIZE // 8)
        self.assertEqual(Config.PIECE_SIZE, Config.SQUARE_SIZE - 10)

    def test_invalid_click_handling(self):
        """Test handling of invalid clicks."""
        # Click above the board
        invalid_pos = (100, 20)  # Y coordinate less than BOARD_OFFSET
        invalid_square = self.coords_converter.coords_to_square(invalid_pos)
        self.assertIsNone(invalid_square)

        # Click should not affect game state
        original_state = str(self.game_state.board)
        self.game_state.handle_click(invalid_square)
        self.assertEqual(str(self.game_state.board), original_state)

    def tearDown(self):
        """Clean up after each test method."""
        pygame.quit()


if __name__ == '__main__':
    unittest.main()