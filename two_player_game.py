import pygame
import chess
import sys
from typing import Optional, Tuple


class Colors:
    """Static class containing color definitions for the chess board and pieces."""
    BROWN = (181, 136, 99)  # Dark squares
    GREEN = (240, 217, 181)  # Light squares
    HIGHLIGHT = (255, 255, 0, 128)  # Selected square highlight
    VALID_MOVE = (0, 255, 0, 128)  # Valid move highlight


class Config:
    """Static class containing game configuration constants."""
    WINDOW_SIZE = 600  # Size of the game window in pixels
    BOARD_OFFSET = 40  # Offset from top of window to board
    SQUARE_SIZE = WINDOW_SIZE // 8  # Size of each chess square
    PIECE_SIZE = SQUARE_SIZE - 10  # Size of the chess pieces


class ChessRenderer:
    """Handles all visual rendering aspects of the chess game."""

    def __init__(self, window_size: int):
        """Initialize the renderer with window size and cache for piece images."""
        self.window_size = window_size
        self.square_size = window_size // 8
        self.font = pygame.font.SysFont('dejavusans', Config.SQUARE_SIZE // 3)

        self.piece_mapping = {
            'P': 'Chess_plt60.png',  # White pawn
            'R': 'Chess_rlt60.png',  # White rook
            'N': 'Chess_nlt60.png',  # White knight
            'B': 'Chess_blt60.png',  # White bishop
            'Q': 'Chess_qlt60.png',  # White queen
            'K': 'Chess_klt60.png',  # White king
            'p': 'Chess_pdt60.png',  # Black pawn
            'r': 'Chess_rdt60.png',  # Black rook
            'n': 'Chess_ndt60.png',  # Black knight
            'b': 'Chess_bdt60.png',  # Black bishop
            'q': 'Chess_qdt60.png',  # Black queen
            'k': 'Chess_kdt60.png',  # Black king
        }

        self.piece_images = {}
        self._initialize_piece_images()

    def _initialize_piece_images(self):
        """Load and cache piece images."""
        for piece_symbol, image_file in self.piece_mapping.items():
            try:
                image = pygame.image.load(image_file)
                scaled_image = pygame.transform.scale(image, (Config.PIECE_SIZE, Config.PIECE_SIZE))
                self.piece_images[piece_symbol] = scaled_image
            except pygame.error as e:
                print(f"Error loading image {image_file}: {e}")
                sys.exit(1)

    def draw_board(self, screen: pygame.Surface):
        """Draw the chess board squares with alternating colors."""
        for row in range(8):
            for col in range(8):
                x = col * self.square_size
                y = (row * self.square_size) + Config.BOARD_OFFSET  # Add offset to board position
                color = Colors.GREEN if (row + col) % 2 == 0 else Colors.BROWN
                pygame.draw.rect(screen, color, (x, y, self.square_size, self.square_size))

    def draw_piece(self, screen: pygame.Surface, piece: chess.Piece, position: Tuple[int, int]):
        """Draw a chess piece at the specified position using cached PNG image."""
        x, y = position
        x_centered = x + (self.square_size - Config.PIECE_SIZE) // 2
        y_centered = y + (self.square_size - Config.PIECE_SIZE) // 2 + Config.BOARD_OFFSET  # Add offset
        piece_image = self.piece_images[piece.symbol()]
        screen.blit(piece_image, (x_centered, y_centered))

    def draw_highlights(self, screen: pygame.Surface, selected_square: Optional[int],
                        valid_moves: list, coords_converter):
        """Draw highlights for selected square and valid moves."""
        if selected_square is not None:
            x, y = coords_converter.square_to_coords(selected_square)
            y += Config.BOARD_OFFSET  # Add offset
            s = pygame.Surface((self.square_size, self.square_size), pygame.SRCALPHA)
            pygame.draw.rect(s, Colors.HIGHLIGHT, s.get_rect())
            screen.blit(s, (x, y))

        for square in valid_moves:
            x, y = coords_converter.square_to_coords(square)
            y += Config.BOARD_OFFSET  # Add offset
            s = pygame.Surface((self.square_size, self.square_size), pygame.SRCALPHA)
            pygame.draw.rect(s, Colors.VALID_MOVE, s.get_rect())
            screen.blit(s, (x, y))

    def draw_status(self, screen: pygame.Surface, board: chess.Board):
        """Draw game status (current turn or game over message)."""
        if board.is_game_over():
            status = "Draw" if board.is_stalemate() else f"{'White' if not board.turn else 'Black'} wins!"
            if board.is_checkmate():
                status = f"Checkmate! {status}"
            text = self.font.render(status, True, (0, 0, 0))
            text_rect = text.get_rect(center=(Config.WINDOW_SIZE // 2, Config.BOARD_OFFSET // 2))
            screen.blit(text, text_rect)
        else:
            turn = "White" if board.turn else "Black"
            text = self.font.render(f"Current turn: {turn}", True, (0, 0, 0))
            text_rect = text.get_rect(center=(Config.WINDOW_SIZE // 2, Config.BOARD_OFFSET // 2))
            screen.blit(text, text_rect)


class CoordinateConverter:
    """Handles conversion between screen coordinates and chess board squares."""

    def __init__(self, square_size: int):
        """Initialises the conversion"""
        self.square_size = square_size

    def coords_to_square(self, pos: Tuple[int, int]) -> chess.Square:
        x, y = pos
        y -= Config.BOARD_OFFSET  # Subtract offset for coordinate conversion
        if y < 0:  # Click above the board
            return None
        col = x // self.square_size
        row = 7 - (y // self.square_size)
        return chess.square(col, row)

    def square_to_coords(self, square: chess.Square) -> Tuple[int, int]:
        col = chess.square_file(square)
        row = 7 - chess.square_rank(square)
        return (col * self.square_size, row * self.square_size)


class GameState:
    """Manages the chess game state and move validation."""

    def __init__(self):
        self.board = chess.Board()
        self.selected_square: Optional[chess.Square] = None
        self.valid_moves = []

    def handle_click(self, clicked_square: chess.Square):
        """Handles any user clicks on the board"""
        if clicked_square is None or self.board.is_game_over():
            return

        if self.selected_square is None:
            piece = self.board.piece_at(clicked_square)
            if piece and ((piece.color == chess.WHITE) == self.board.turn):
                self.selected_square = clicked_square
                self.valid_moves = [move.to_square for move in self.board.legal_moves
                                    if move.from_square == clicked_square]
        else:
            move = chess.Move(self.selected_square, clicked_square)
            if move.from_square == self.selected_square and clicked_square == move.to_square:
                if (self.board.piece_at(self.selected_square).piece_type == chess.PAWN and
                        ((chess.square_rank(clicked_square) == 7 and self.board.turn) or
                         (chess.square_rank(clicked_square) == 0 and not self.board.turn))):
                    move.promotion = chess.QUEEN

                if move in self.board.legal_moves:
                    self.board.push(move)

            self.selected_square = None
            self.valid_moves = []


class ChessGame:
    """Main game class that coordinates all game components."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.WINDOW_SIZE, Config.WINDOW_SIZE + Config.BOARD_OFFSET))
        pygame.display.set_caption('Chess Game')

        self.renderer = ChessRenderer(Config.WINDOW_SIZE)
        self.coords_converter = CoordinateConverter(Config.SQUARE_SIZE)
        self.game_state = GameState()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    clicked_square = self.coords_converter.coords_to_square(event.pos)
                    self.game_state.handle_click(clicked_square)
        return True

    def render(self):
        self.screen.fill((255, 255, 255))
        self.renderer.draw_board(self.screen)
        self.renderer.draw_highlights(
            self.screen,
            self.game_state.selected_square,
            self.game_state.valid_moves,
            self.coords_converter
        )

        for square in chess.SQUARES:
            piece = self.game_state.board.piece_at(square)
            if piece:
                coords = self.coords_converter.square_to_coords(square)
                self.renderer.draw_piece(self.screen, piece, coords)

        self.renderer.draw_status(self.screen, self.game_state.board)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.render()

        pygame.quit()
        sys.exit()


def main():
    game = ChessGame()
    game.run()

