# Chess Program

 - **1.** [Introduction](#intro)
 - **2.** [Context Diagram](#context)
 - **3.** [User Stories](#stories)
 - **4.** [Project Plan](#plan)
 - **5.** [System Class Diagram](#sys_diagram)
 - **6.** [Object-Orientation in Chess Program](#oop_chess)
 - **7.** [Data Dictionary](#data_dict)
 - **8.** [Testing](#testing)
 - **9.** [Major Issues Faced](#issues)

## 1. Introduction<a name="intro"></a>

### Introduction

This project aims to design and develop a local chess program in Python, allowing users to play either against another player or an AI opponent. The program will include a chess engine for move validation and game state tracking, a computer opponent using a minimax algorithm, and a graphical user interface for seamless gameplay.

### Project Overview:

- **Game Engine**: This component will manage chess rules, move validation, board representation, and game state tracking (e.g., check, checkmate, stalemate, castling, en passant, etc.).
- **AI Opponent**: The AI will evaluate board positions and make optimal moves using a minimax and alpha-beta pruning algorithm.
- **User Interface**: The program will feature a local interface that allows players to interact with the game.

## 2. Context Diagram<a name="context"></a>

The interactions between the user and the chess program can be depicted through a context diagram, illustrating local gameplay and AI-based interactions.

<img width="616" alt="image" src="https://github.com/user-attachments/assets/7c0bf90b-86f9-4e40-9887-40ef18fc6ece" />


## 3. User Stories<a name="stories"></a>

User stories define how the software features will add value to users. Each user story follows the format:  
**"As a [type of user], I [want to], [so that]."**

- **As a Casual Player**, I want to play against a friend locally, so that we can enjoy a game without needing an internet connection.
- **As a Chess Enthusiast**, I want to play against a strong AI.
- **As a Beginner**, I want to use a computer to see what the best moves are.

## 4. Project Plan<a name="plan"></a>

The project is structured over six weeks with different phases of development:

![Project Plan](https://github.com/user-attachments/assets/ad0d41d5-e4a5-4db1-8b66-3d8376abf506)

### Key Phases:
- **Red** - System Design and Architecture Planning
- **Orange** - Research of well-known Chess Engines
- **Yellow** - Implementation of Game Engine, Algorithm and GUI
- **Green** - Testing and Bug Fixing
- **Blue** - Finalization and Documentation

## 5. System Class Diagram<a name="sys_diagram"></a>

![Class Diagram](https://github.com/user-attachments/assets/079cf817-be2f-4cc3-b4e2-fc839a95c588)

## 6. Object-Orientation in Chess Program<a name="oop_chess"></a>

This chess program follows object-oriented programming (OOP) principles for better maintainability and modularity.

### **Classes:**

These highlight the main functionality of the classes. However, these are not the full classes.

All classes used:

```python
class ChessGame:
def __init__(self):
   """Initialize the renderer."""
def draw_menu(self):
   """Draw the initial game menu."""
def menu(self):
   """Handle menu interactions to select game mode."""
def run(self):
   """Start the game based on the selected mode."""
```


```python
class Colors:
   """Static class containing color definitions for the chess board and pieces."""
```


```python
class Config:
   """Static class containing game configuration constants."""
```


```python
class ChessRenderer:
   """Handles all visual rendering aspects of the chess game."""
def __init__(self, window_size: int):
   """Initialize the renderer with window size and cache for piece images."""
def _initialize_piece_images(self):
   """Load and cache piece images."""
def draw_board(self, screen: pygame.Surface):
   """Draw the chess board squares with alternating colors."""
def draw_piece(self, screen: pygame.Surface, piece: chess.Piece, position: Tuple[int, int]):
   """Draw a chess piece at the specified position using cached PNG image."""
def draw_highlights(self, screen: pygame.Surface, selected_square: Optional[int],
                   valid_moves: list, coords_converter):
   """Draw highlights for selected square and valid moves."""
def draw_status(self, screen: pygame.Surface, board: chess.Board):
   """Draw game status (current turn or game over message)."""
```


```python
class CoordinateConverter:
   """Handles conversion between screen coordinates and chess board squares."""
def __init__(self, square_size: int):
   """Initialises the conversion"""
def coords_to_square(self, pos: Tuple[int, int]) -> chess.Square:
def square_to_coords(self, square: chess.Square) -> Tuple[int, int]:
```


```python
class GameState:
   """Manages the chess game state and move validation."""
def handle_click(self, clicked_square: chess.Square):
   """Handles any user clicks on the board"""
```

```python
class ChessAI:
   """Simple chess AI using minimax with depth 3."""
def evaluate_position(self, board: chess.Board) -> float:
   """Evaluate the current board position."""
def minimax(self, board: chess.Board, depth: int, alpha: float, beta: float, maximizing: bool) -> Tuple[
   float, Optional[chess.Move]]:
   """Minimax function that uses recursion to calculate best move"""
def get_best_move(self, board: chess.Board) -> chess.Move:
   """Get the best move for the current position."""
```

This chess game follows the four OOP principles:
Encapsulation: Each class encapsulates specific functionality. ChessRenderer._initialize_piece_images() keeps image caching private, while GameState.handle_click() restricts direct game state modifications.
Abstraction: ChessGame.run() hides game setup details, and ChessAI.get_best_move() abstracts AI logic, preventing direct interaction with minimax().
Polymorphism: ChessRenderer.draw_board(), draw_piece(), and draw_status() share a common screen parameter but perform different rendering tasks. ChessAI.minimax() adjusts behavior for maximizing or minimizing moves.
These principles make the code modular, maintainable, and extensible.



## 7. Data Dictionary<a name="data_dict"></a>

| Variable            | Data type               | Display format       | Size in bytes | Display size in bytes | Description                      | Example                   | Validation                 |
|---------------------|------------------------|----------------------|--------------|-------------------|----------------------------------|---------------------------|---------------------------|
| `board`        | `imported class from library`   | N/A                  | Variable     | Variable         | The main game display surface   | `Board()`                  | Must be a valid `Board` object |
| `selected_square` | `Optional[chess.Square]` | (x, y)                | 8            | 8                 | Currently selected chess square | `None` or `chess.Square`  | Must be `None` or `chess.Square` |
| `valid_moves`  | `imported class from library`  | List of `Move` objects | Variable | Variable | Stores all valid moves         | `[Move(...), Move(...)]`   | List elements must be of type `Move` |
| `player_color` | `bool`                  | `True`/`False`        | 1            | 1                 | Indicates the player's color (`True` for white, `False` for black) | `True` | Must be `True` or `False` |



## 8. Testing<a name="testing"></a>

The chess program implements comprehensive testing strategies to ensure reliability and correct functionality across all components.

### 8.1 Unit Testing

Unit tests are implemented using Python's built-in `unittest` framework, focusing on individual components and their functionality.

#### Key Test Cases:

| Test Case | Input | Expected Output |
|-----------|-------|----------------|
| **Board Initialization** | Initial game state | Correct piece placement, White to move |
| **Coordinate Conversion** | Screen position `(0, BOARD_OFFSET)` | Board square `A8` |
| **Move Validation** | Pawn at `E2` | Valid moves: `E3`, `E4` |
| **AI Evaluation** | Initial chess board | Score `0` |

##### Test Results:
```
pygame 2.6.1 (SDL 2.28.4, Python 3.9.5)
Hello from the pygame community. https://www.pygame.org/contribute.html
........
----------------------------------------------------------------------
Ran 8 tests in 2.990s
```
```
.test_initial_board_setup ... ok
.test_coordinate_conversion ... ok
.test_valid_pawn_moves ... ok
.test_chess_ai_evaluation ... ok
.test_game_state_initialization ... ok
.test_colors_constants ... ok
.test_config_values ... ok
.test_invalid_click_handling ... ok
```

### 8.2 Test Coverage

| Component | Notes |
|-----------|-------|
| **Game State** | Core game logic fully tested |
| **AI Logic** | Position evaluation and move selection covered |
| **UI/Renderer** | Visual components and user interaction covered |
| **Coordinate System** | Complete coverage of conversion logic |

### 8.3 Test Implementation

Test execution is managed through a dedicated test suite in `test_chess_game.py`. Tests can be run using:

```sh
python -m unittest test_chess_game.py
```

### 8.4 Testing Approach

#### 1. White Box Testing

- **Internal logic verification:** Verified AI position evaluation by checking the initial game state score.
- **Path coverage analysis:** Ensured all branches in move validation were tested.
- **Example:**
  ```python
  def test_chess_ai_evaluation(self):
      ai = ChessAI()
      initial_score = ai.evaluate_position(chess.Board())
      self.assertEqual(initial_score, 0)  # Initial position should be balanced
  ```

#### 2. Black Box Testing

- **Input validation:** Verified coordinate conversion using board coordinates.
- **Game flow verification:** Ensured proper handling of invalid clicks.
- **Example:**
  ```python
  def test_invalid_click_handling(self):
      invalid_pos = (100, 20)  # Y coordinate less than BOARD_OFFSET
      invalid_square = self.coords_converter.coords_to_square(invalid_pos)
      self.assertIsNone(invalid_square)
  ```

#### 3. Integration Testing

- **Component interaction:** Verified interaction between UI and game logic.
- **State management:** Ensured board updates correctly between moves.
- **Example:**
  ```python
  def test_game_state_initialization(self):
      self.assertIsNone(self.game_state.selected_square)
      self.assertTrue(self.game_state.board.turn)  # White to move
  ```

### 8.5 Test Categories

#### Functional Tests

- **Game rule enforcement:** Verified checkmate and stalemate conditions.
- **Move validation:** Ensured pawn move legality.
- **Example:**
  ```python
  def test_valid_pawn_moves(self):
      e2_square = chess.E2
      self.game_state.selected_square = e2_square
      self.game_state.valid_moves = [move.to_square for move in self.game_state.board.legal_moves
                                     if move.from_square == e2_square]
      self.assertIn(chess.E3, self.game_state.valid_moves)
  ```

#### User Interface Tests

- **Menu navigation:** Verified that menu selections work correctly.
- **Piece selection:** Ensured selected piece highlights correctly.
- **Example:**
  ```python
  def test_colors_constants(self):
      self.assertEqual(len(Colors.BROWN), 3)  # RGB tuple
  ```



## 9. Major Issues Faced<a name="issues"></a>

Throughout the development of this chess program, several major challenges were encountered that significantly impacted the project timeline and approach. These key issues required creative solutions and provided valuable learning opportunities.

### 9.1 GUI Implementation Challenges with Pygame

As a developer with no prior experience using Pygame, building the graphical user interface presented the most significant hurdle in this project:

#### 9.1.1 Learning Pygame's Event-Driven Architecture

Understanding and adapting to Pygame's core concepts required a substantial learning curve:

- **Event-based programming model**: Transitioning from traditional procedural programming to Pygame's event loop structure required a fundamental shift in thinking
- **Surface and rect management**: The concept of surfaces, blitting, and managing rectangular areas was initially confusing
- **Coordinate system**: Adapting to the top-left origin system and pixel-based positioning caused numerous early bugs

```python
# Early attempt at handling user input had event processing issues
def run_game(self):
    while True:
        # Problematic: Handling events incorrectly
        if pygame.MOUSEBUTTONDOWN:  # Incorrect event check
            self.handle_click()
        self.draw_board()
        
# Corrected implementation with proper event loop
def run_game(self):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_click(event.pos)
        self.draw_board()
        pygame.display.flip()
```

#### 9.1.2 Asset Management Challenges

Working with images and other assets in Pygame introduced several complications that weren't anticipated:

- **File path issues**: Cross-platform differences in file path handling caused loading failures
- **Image transparency**: Maintaining proper transparency for chess pieces over different board squares
- **Scaling and quality**: Balancing piece image quality with performance during scaling operations
- **Resource management**: Properly loading and unloading assets to prevent memory leaks

```python
# Initial asset loading approach had multiple issues
def load_assets(self):
    self.piece_images = {}
    # Problematic: Hard-coded paths and no error handling
    self.piece_images['P'] = pygame.image.load('assets/white_pawn.png')
    self.piece_images['R'] = pygame.image.load('assets/white_rook.png')
    # ...and so on for each piece

# Improved implementation with better path handling and error management
def load_assets(self):
    self.piece_images = {}
    piece_types = ['P', 'R', 'N', 'B', 'Q', 'K', 'p', 'r', 'n', 'b', 'q', 'k']
    
    try:
        for piece in piece_types:
            # Use os.path for cross-platform compatibility
            path = os.path.join('assets', f'{piece}.png')
            image = pygame.image.load(path).convert_alpha()
            # Scale relative to square size for consistency
            self.piece_images[piece] = pygame.transform.scale(
                image, 
                (int(self.square_size * 0.8), int(self.square_size * 0.8))
            )
    except pygame.error as e:
        print(f"Error loading piece image: {e}")
        # Fallback to colored rectangles with text
        for piece in piece_types:
            surf = pygame.Surface((self.square_size, self.square_size), pygame.SRCALPHA)
            color = (200, 200, 200) if piece.isupper() else (50, 50, 50)
            pygame.draw.rect(surf, color, surf.get_rect(), border_radius=10)
            font = pygame.font.SysFont('arial', 36)
            text = font.render(piece, True, (255, 0, 0))
            surf.blit(text, text.get_rect(center=surf.get_rect().center))
            self.piece_images[piece] = surf
```

#### 9.1.3 User Interaction and Move Visualization

Creating an intuitive, responsive interface for chess moves proved challenging:

- **Piece selection feedback**: Providing clear visual indication of the selected piece
- **Legal move highlighting**: Showing available moves while maintaining visual clarity
- **Move animation**: Implementing smooth transitions when pieces move or are captured
- **Screen-to-board coordinate conversion**: Translating pixel coordinates to chess positions

```python
# Highlighting legal moves was particularly challenging
def highlight_legal_moves(self, square):
    legal_moves = []
    for move in self.board.legal_moves:
        if move.from_square == square:
            # Create a highlight surface with transparency
            highlight = pygame.Surface((self.square_size, self.square_size), pygame.SRCALPHA)
            
            # Different highlighting for captures vs. regular moves
            if self.board.piece_at(move.to_square):
                # Red highlight with 40% opacity for captures
                pygame.draw.rect(highlight, (255, 0, 0, 102), highlight.get_rect(), 4)
            else:
                # Green highlight with 40% opacity for regular moves
                pygame.draw.circle(highlight, (0, 255, 0, 102), 
                                  (self.square_size // 2, self.square_size // 2), 
                                  self.square_size // 6)
            
            # Convert chess position to screen coordinates
            x = (move.to_square % 8) * self.square_size
            y = (move.to_square // 8) * self.square_size + Config.BOARD_OFFSET
            self.screen.blit(highlight, (x, y))
```

### 9.2 AI Checkmate Execution Limitation

A critical issue emerged with the AI's ability to execute checkmate sequences:

#### 9.2.1 Horizon Effect in Minimax Implementation

The AI would often fail to deliver checkmate even in clearly winning positions due to fundamental limitations in the minimax algorithm implementation:

- **Search depth limitation**: Checkmates beyond the configured search depth (typically 3-4 ply) were invisible to the AI
- **Evaluation function bias**: The AI would prioritize material gains over checkmate opportunities that were beyond its search horizon
- **Positional regression**: In some cases, the AI would actually retreat from checkmate positions toward material-gaining moves

```python
# Initial evaluation function that couldn't "see" checkmates beyond the horizon
def minimax(self, board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return self.evaluate_position(board)
    
    # Rest of minimax implementation...

def evaluate_position(self, board):
    # Simple material-based evaluation
    if board.is_checkmate():
        return float('inf') if board.turn != self.color else float('-inf')
    
    score = 0
    # Calculate material score
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = self.get_piece_value(piece.piece_type)
            if piece.color == chess.WHITE:
                score += value
            else:
                score -= value
    
    return score if self.color == chess.WHITE else -score
```

#### 9.2.2 Implementing Quiescence Search as a Solution

To address this limitation, a quiescence search was implemented to extend the search in volatile positions:

```python
def minimax(self, board, depth, alpha, beta, maximizing_player):
    # If at search limit, use quiescence search to avoid horizon effect
    if depth == 0:
        return self.quiescence_search(board, alpha, beta, 2)
        
    # Rest of minimax implementation...

def quiescence_search(self, board, alpha, beta, depth):
    """Extended search for volatile positions to mitigate horizon effect"""
    stand_pat = self.evaluate_position(board)
    
    # Base case
    if depth == 0:
        return stand_pat
        
    # Beta cutoff
    if stand_pat >= beta:
        return beta
        
    # Update alpha if standing pat is better
    if stand_pat > alpha:
        alpha = stand_pat
        
    # Only consider captures and check-giving moves
    for move in self.generate_tactical_moves(board):
        new_board = board.copy()
        new_board.push(move)
        
        score = -self.quiescence_search(new_board, -beta, -alpha, depth - 1)
        
        if score >= beta:
            return beta
            
        if score > alpha:
            alpha = score
            
    return alpha

def generate_tactical_moves(self, board):
    """Generate only captures and check-giving moves to keep search manageable"""
    tactical_moves = []
    
    for move in board.legal_moves:
        # Include capture moves
        if board.is_capture(move):
            tactical_moves.append(move)
            continue
            
        # Check if move gives check
        board_copy = board.copy()
        board_copy.push(move)
        if board_copy.is_check():
            tactical_moves.append(move)
            
    return tactical_moves
```

This implementation significantly improved the AI's ability to execute checkmate sequences by allowing it to "see" beyond the standard search depth in tactical situations, solving one of the most frustrating issues for users playing against the computer opponent.

### 9.3 Learning Outcomes

These major challenges led to significant learning in:
1. Event-driven GUI programming with Pygame
2. Chess engine design and implementation
3. AI search algorithms and horizon effect mitigation techniques
