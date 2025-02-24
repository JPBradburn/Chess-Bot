# Chess Program

 - **1.** [Introduction](#intro)
 - **2.** [Context Diagram](#context)
 - **3.** [User Stories](#stories)
 - **4.** [Project Plan](#plan)
 - **5.** [System Class Diagram](#sys_diagram)
 - **6.** [Object-Orientation in Chess Program](#oop_chess)
 - **7.** [Data Dictionary](#data_dict)

## 1. Introduction<a name="intro"></a>

### Introduction

This project aims to design and develop a local chess program in Python, allowing users to play either against another player or an AI opponent. The program will include a chess engine for move validation and game state tracking, a computer opponent using a minimax algorithm, and a graphical user interface for seamless gameplay.

### Project Overview:

- **Game Engine**: This component will manage chess rules, move validation, board representation, and game state tracking (e.g., check, checkmate, stalemate, castling, en passant, etc.).
- **AI Opponent**: The AI will evaluate board positions and make optimal moves using a minimax and alpha-beta pruning algorithm.
- **User Interface**: The program will feature a local interface that allows players to interact with the game.

## 2. Context Diagram<a name="context"></a>

The interactions between the user and the chess program can be depicted through a context diagram, illustrating local gameplay and AI-based interactions.

![Context Diagram](https://github.com/user-attachments/assets/ad4dc476-5100-491d-8e93-eec1f79a9e08)

## 3. User Stories<a name="stories"></a>

User stories define how the software features will add value to users. Each user story follows the format:  
**"As a [type of user], I [want to], [so that]."**

- **As a Casual Player**, I want to play against a friend locally, so that we can enjoy a game without needing an internet connection.
- **As a Chess Enthusiast**, I want to play against an AI with different difficulty levels, so that I can practice and improve my skills.
- **As a Beginner**, I want to get hints or suggested moves, so that I can learn chess strategies while playing.
- **As an Advanced Player**, I want to customize the AI’s playstyle (aggressive, defensive, etc.), so that I can challenge myself in different ways.
- **As a Player with Limited Time**, I want to save and resume games, so that I can continue my matches later.

## 4. Project Plan<a name="plan"></a>

The project is structured over six weeks with different phases of development:

![Project Plan](https://github.com/user-attachments/assets/ad0d41d5-e4a5-4db1-8b66-3d8376abf506)

### Key Phases:
- **Red** - System Design and Architecture Planning
- **Orange** - Research and AI Algorithm Development
- **Yellow** - Implementation of Game Engine and GUI
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
                color = (200, 200, 200) if (row + col) % 2 == 0 else (100, 100, 100)
                pygame.draw.rect(screen, color, (col * 80, row * 80, 80, 80))
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
- **Single Responsibility Principle**: ChessGame controls the game flow, ChessRenderer handles the UI, and ChessAI manages decision-making.
- **Modularity**: Components can be updated or replaced independently.

## 7. Data Dictionary<a name="data_dict"></a>

| Variable | Type | Description |
|----------|------|-------------|
| `board` | `chess.Board` | Stores the current board position and move history |
| `player_turn` | `bool` | Indicates whether it is White’s or Black’s turn |
| `legal_moves` | `list` | Contains all possible legal moves for the current position |
| `ai_difficulty` | `int` | Sets the AI's difficulty level (1-5) |

This structured approach ensures an efficient, extensible, and user-friendly chess program for local play.

