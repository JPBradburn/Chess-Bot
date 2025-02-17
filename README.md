# Chess-Bot

 - **1.** [Introduction](#intro) 
 - **2.** [Context Diagram](#context) 
 - **3.** [User Stories](#stories) 
 - **4.** [Project Plan](#plan) 
 - **5.** [System Class Diagram](#sys_diagram)
 - **6.** [Object-Orientation in OMS](#oms_object)
 - **7.** [Data Dictionary](#data_dict)

## 1. Introduction<a name="intro"></a>
## Introduction

This project aims to design and develop a chess bot for Lichess using Python, focusing on three key components: the game engine, chess AI (strategy and decision-making), and Lichess API integration (communication and user interface).

The division of the project into these components ensures maintainability, reflecting real-world scenarios where the user interface (Lichess platform interaction) can evolve, while the core AI logic and game strategies remain consistent. This project will utilize Python and the Lichess API for handling game interactions, allowing the bot to analyze positions, make moves, and communicate with the platform.

Project Overview:
Game Engine: This component will focus on handling the rules of chess, move validation, board state representation, and game status tracking. It ensures that the bot operates within the constraints of chess, such as legal moves, castling, en passant, and check/checkmate conditions.

Chess AI (Strategy and Decision-Making): The AI component will be designed to evaluate different board positions and determine optimal moves. This will involve a minimax algorithm, along with optimizations like alpha-beta pruning, to enhance decision-making. The AI will consider various factors such as material balance, piece activity, and tactical motifs when selecting moves.

Testing and Refinement: After the initial implementation, the bot will be tested in various game scenarios, including different time controls and opponent strengths. Based on these tests, the AI’s performance will be refined, and the system will be optimized for faster response times and improved decision-making.

Documentation and Finalization: The  phase will include comprehensive documentation, covering how the bot works, how to set it up, and how to use it with Lichess. Additionally, the bot's performance and limitations will be analyzed and reported. This documentation process will be completed throughout the project's development.


## 2. Context Diagram<a name="context"></a>
The interactions between the end user and the chess bot can be depicted via a context diagram, as shown below in Figure 2. Further details of the context diagram are not shown to keep this document brief wherever possible.

![Coolest Context Diagram you've ever seen](https://github.com/user-attachments/assets/ad4dc476-5100-491d-8e93-eec1f79a9e08)


## 3. User Stories<a name="stories"></a>
User Stories are typically used in Agile frameworks to articulate how each software feature will add value to the user. Each user story is the smallest unit of work in an agile framework and has the following structure:
“As a [person], I [want to], [so that].”  

As a Chess Enthusiast, I want to be able to challenge the chess bot with varying difficulty levels, so that I can improve my skills at my own pace.

As a New Player, I want to be able to get hints or suggestions from the chess bot during the game, so that I can learn from my mistakes and improve.

As a Player with a Busy Schedule, I want to be able to start a game and pause it, so that I can return later without losing progress.

As a Chess Coach, I want to be able to see what the best stategies are so that I can teach my students well.

As an Advanced Player, I want to be able to adjust the chess bot’s style of play (aggressive, defensive, etc.), so that I can challenge myself with different types of strategies.

As a Competitive Player, I want to be able to increase the difficulty of the bot so that I can constantly challenge myself.

</ol>

## 4. Project Plan<a name="plan"></a>
The project is planned to be completed in 6 weeks.

<img width="1056" alt="Screenshot 2025-02-10 at 12 40 06 pm" src="https://github.com/user-attachments/assets/ad0d41d5-e4a5-4db1-8b66-3d8376abf506" />

Key:
Red - Identifying and Designing

Orange - Research and Planning

Yellow - Producing and Implementing

Green - Testing and Evaluating

Blue - Project Version Control / Submission


## 5. System Class Diagram<a name="sys_diagram"></a>

## 6. Object-Orientation in Chess Bot<a name="oms_object"></a>

This chess implementation leverages object-oriented programming principles through several key classes that handle different aspects of the game. Here's how OOP is used throughout the project:

### ChessGame Class
The main game class that coordinates all components and manages the game loop. It uses composition to combine the renderer, game state, and coordinate converter into a cohesive system.

```python
class ChessGame:
    def __init__(self):
        self.renderer = ChessRenderer(Config.WINDOW_SIZE)
        self.coords_converter = CoordinateConverter(Config.SQUARE_SIZE)
        self.game_state = GameState()
```

### ChessRenderer Class
Handles all visual aspects of the game, encapsulating the complexity of rendering chess pieces, the board, and game status:

```python
class ChessRenderer:
    def draw_board(self, screen: pygame.Surface):
        """Draw the chess board squares with alternating colors."""
        for row in range(8):
            for col in range(8):
                x = col * self.square_size
                y = row * self.square_size + Config.BOARD_OFFSET
                color = Colors.GREEN if (row + col) % 2 == 0 else Colors.BROWN
                pygame.draw.rect(screen, color, (x, y, self.square_size, self.square_size))
```

### GameState Class
Manages the game's state using the python-chess library, handling moves and validating game rules:

```python
class GameState:
    def handle_click(self, clicked_square: chess.Square):
        """Handle player clicks on the chess board."""
        if clicked_square is None or self.board.is_game_over():
            return
```

### CoordinateConverter Class
Provides conversion between screen coordinates and chess board positions:

```python
class CoordinateConverter:
    def coords_to_square(self, pos: Tuple[int, int]) -> chess.Square:
        """Convert screen coordinates to chess board square."""
        x, y = pos
        y -= Config.BOARD_OFFSET  # Subtract offset for coordinate conversion
        if y < 0:  # Click above the board
            return None
        col = x // self.square_size
        row = 7 - (y // self.square_size)
        return chess.square(col, row)
```

### Key OOP Principles Used

1. **Encapsulation**
   - Each class manages its own data and methods
   - Internal implementation details are hidden
   - Clean public interfaces for interaction

2. **Single Responsibility**
   - ChessGame: Game flow and coordination
   - ChessRenderer: Visual representation
   - GameState: Game rules and state
   - CoordinateConverter: Coordinate transformations

3. **Composition**
   - Classes are composed rather than inherited
   - Components can be modified independently
   - Flexible architecture for future changes

4. **Clean Interfaces**
   - Well-defined method signatures
   - Clear separation of concerns
   - Type hints for better code clarity

This object-oriented approach makes the code:
-  Modular and maintainable
-  Easy to modify and extend
-  Simple to test
-  Clear to understand

The use of classes creates a robust foundation for adding new features, such as:
- Additional piece types
- Different game modes
- Custom rule sets
- AI opponents

## 7. Data Dictionary<a name="data_dict"></a>

