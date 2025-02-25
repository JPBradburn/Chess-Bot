# Chess Program

 - **1.** [Introduction](#intro)
 - **2.** [Context Diagram](#context)
 - **3.** [User Stories](#stories)
 - **4.** [Project Plan](#plan)
 - **5.** [System Class Diagram](#sys_diagram)
 - **6.** [Object-Orientation in Chess Program](#oop_chess)
 - **7.** [Data Dictionary](#data_dict)
 - **8.** [Testing](#testing)

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

### **Key Classes:**

#### ChessGame Class (Main Controller)
Manages the game loop, board state, and user input.

```python
class ChessGame:
    def __init__(self):
        self.renderer = ChessRenderer()
        self.board = GameState()
        self.ai = ChessAI()
```

#### ChessRenderer Class (GUI and Display)
Handles drawing the board, pieces, and move highlights.

```python
class ChessRenderer:
    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                x = col * self.square_size
                y = (row * self.square_size) + Config.BOARD_OFFSET
```

#### GameState Class (Game Logic)
Manages board positions, move validation, and checkmate conditions.

```python
class GameState:
    def is_legal_move(self, move):
        return move in self.board.legal_moves
```

#### ChessAI Class (AI Opponent)
Implements decision-making using minimax and alpha-beta pruning.

```python
class ChessAI:
    def choose_best_move(self, board):
        best_move = self.minimax(board, depth=3)
        return best_move
```

### **OOP Principles Used:**
- **Encapsulation**: Each class manages its own responsibilities (e.g., game state, AI logic, rendering).
- **Single Responsibility Principle**: ChessGame controls the game flow and handles menu interactions.
- **Modularity**: Components (e.g., `two_player_game`, `play_as_white_vs_ai`, `play_as_black_vs_ai`) can be updated independently.

## 7. Data Dictionary<a name="data_dict"></a>

| Variable | Type | Description |
|----------|------|-------------|
| `screen` | `pygame.Surface` | The main game display surface |
| `clock` | `pygame.time.Clock` | Manages game loop timing |
| `running` | `bool` | Determines whether the game is running |
| `mode` | `str` | Stores the selected game mode (two-player or AI) |
| `font` | `pygame.font.Font` | Font object used for rendering text |
| `buttons` | `list` | Stores clickable button areas for menu selection |

## 8. Testing<a name="testing"></a>
## 8. Testing<a name="testing"></a>

The chess program implements comprehensive testing strategies to ensure reliability and correct functionality across all components.

### 8.1 Unit Testing

Unit tests are implemented using Python's built-in `unittest` framework, focusing on individual components and their functionality.

#### Key Test Cases:

1. **Board Initialization Tests**
   - Verify correct piece placement
   - Validate initial game state
   - Check starting player (White)

```python
def test_initial_board_setup(self):
    self.assertEqual(str(self.game_state.board.piece_at(chess.E1)), 'K')
    self.assertEqual(str(self.game_state.board.piece_at(chess.E8)), 'k')
```

2. **Coordinate Conversion Tests**
   - Screen coordinates to board positions
   - Board positions to screen coordinates
   - Boundary condition handling

3. **Move Validation Tests**
   - Legal pawn movements
   - Valid piece selections
   - Invalid move handling

4. **AI Component Tests**
   - Position evaluation accuracy
   - Move generation correctness
   - Decision-making logic

### 8.2 Test Coverage

| Component | Notes |
|-----------|-------|
| Game State | Core game logic fully tested |
| AI Logic | Position evaluation and move selection |
| UI/Renderer | Visual components and user interaction |
| Coordinate System | Complete coverage of conversion logic |

### 8.3 Test Implementation

Test execution is managed through a dedicated test suite in `test_chess_game.py`. Tests can be run using:

```bash
python -m unittest test_chess_game.py
```

### 8.4 Testing Approach

1. **White Box Testing**
   - Internal logic verification
   - Path coverage analysis
   - Branch testing for decision points

2. **Black Box Testing**
   - Input validation
   - Game flow verification
   - User interface interaction

3. **Integration Testing**
   - Component interaction verification
   - Game mode transitions
   - State management between modules

### 8.5 Test Categories

#### Functional Tests
- Game rule enforcement
- Move validation
- Checkmate detection
- Stalemate recognition
- Special move handling (castling, en passant)

#### Performance Tests
- AI response time
- UI rendering efficiency
- Game state updates

#### User Interface Tests
- Menu navigation
- Piece selection
- Move visualization
- Game status display
