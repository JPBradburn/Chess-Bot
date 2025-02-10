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

<i>Figure 2: Context Diagram (NEW)</i>

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


<i>Figure 3: Project Management Plan</i>
## 5. System Class Diagram<a name="sys_diagram"></a>

## 6. Object-Orientation in Chess Bot<a name="oms_object"></a>

## 7. Data Dictionary<a name="data_dict"></a>
A data dictionary comprehensively describes each attribute and class variable used in the system. Note that it is not all variables. Data dictionaries are valuable during the system's post-delivery maintenance. A data dictionary commonly includes variable name, data type, format, size in bytes, and the number of characters to display the item, including the number of decimal places (if applicable), the purpose of the variable, and a relevant example. Validation rules have been included where applicable. Details of records or arrays of records have been included in data dictionaries. These following figures show the data dictionaries for all 8 classes in the project. The main variables and all class attributes have been included, and variables used solely for logic control have been excluded.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/711265fd-2725-4e59-9d3b-29ff384da6e9)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/e70a1bf3-b3ac-4cff-b7e8-6aec779ac733)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/4cb4df36-34fe-4f18-b98f-ba400713fe68)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/6705f900-0cef-4542-b7ac-3a2e6f15d37e)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/28e3e345-9415-42ef-840d-75e6b9560243)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/9489f815-4654-4d06-bd3b-6bdc43a98415)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/4a1fac99-1911-43b7-8197-bb8a6719ca76)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/3b1b5d61-a1af-4dbe-9978-a25e77c6f182)

