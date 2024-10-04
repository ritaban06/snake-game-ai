# Enhanced Snake Game AI

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [How to Play](#how-to-play)
6. [AI Algorithm](#ai-algorithm)
7. [New Game Elements](#new-game-elements)
8. [Code Structure](#code-structure)
9. [Customization](#customization)
10. [Contributing](#contributing)
11. [License](#license)

## Introduction

This project implements an enhanced version of the classic Snake game with an AI player using Python and Pygame. The AI uses a Breadth-First Search (BFS) algorithm to navigate through obstacles and collect power-ups while finding the shortest path to the food. This project serves as an excellent example of pathfinding algorithms, game development, and AI decision-making in Python.

## Features

- Classic Snake game mechanics with additional elements
- AI-controlled snake using BFS pathfinding
- Obstacles to avoid
- Power-ups for bonus points
- Score tracking
- Path visualization
- Game over screen showing final game state
- Customizable game parameters

## Requirements

- Python 3.6+
- Pygame
- NumPy

## Installation

1. Clone this repository or download the source code.
2. Install the required libraries:

```bash
pip install pygame numpy
```

3. Run the game:

```bash
python main.py
```

## How to Play

- The game starts automatically with the AI controlling the snake.
- Watch as the AI navigates the snake to eat the food, avoid obstacles, and collect power-ups.
- The game ends when the snake collides with the wall, an obstacle, or itself.
- After the game ends, the final state is displayed for 3 seconds before the program closes.

## AI Algorithm

The AI uses a Breadth-First Search (BFS) algorithm to find the shortest path to the food or power-ups. Here's how it works:

1. The game board is represented as a grid.
2. The snake's body and obstacles are marked as blocked cells in the grid.
3. BFS is used to find the shortest path from the snake's head to the food or power-up.
4. If a path is found, the snake moves along that path.
5. If no path is found, the AI tries to move to a safe adjacent cell.
6. If no safe move is available, the snake continues in its current direction.

## New Game Elements

### Obstacles
- Static obstacles are randomly placed on the game board at the start of each game.
- The snake must navigate around these obstacles to reach the food.

### Power-ups
- Power-ups occasionally spawn on the game board.
- Collecting a power-up gives bonus points and may provide temporary abilities (e.g., speed boost, invincibility).

### Path Visualization
- The planned path of the AI is visualized on the game board, allowing you to see the AI's decision-making process in real-time.

## Code Structure

- `snake_game_ai.py`: Main game file containing all the code
  - `bfs()`: Implements the Breadth-First Search algorithm
  - `ai_make_decision()`: Decides the next move for the AI, considering obstacles and power-ups
  - `gameLoop()`: Main game loop handling game states, drawing, and new game elements
  - `our_snake()`: Draws the snake on the screen
  - `message()`: Displays text messages on the screen

## Customization

You can customize various aspects of the game by modifying the constants at the beginning of the script:

- `width` and `height`: Change the size of the game window
- `snake_block`: Adjust the size of the snake, food, and obstacle blocks
- `snake_speed`: Modify the speed of the game
- `obstacle_count`: Change the number of obstacles in the game
- `power_up_duration`: Adjust the duration of power-up effects

## Contributing

Contributions to this project are welcome! Here are some ways you can contribute:

1. Report bugs
2. Suggest enhancements
3. Add new features (e.g., new AI algorithms, game modes)
4. Improve documentation

Please fork the repository and create a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

---

Enjoy playing and learning from this Enhanced Snake Game AI! If you have any questions or suggestions, please open an issue on the GitHub repository.
