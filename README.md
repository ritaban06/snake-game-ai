# Snake Game AI

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [How to Play](#how-to-play)
6. [AI Algorithm](#ai-algorithm)
7. [Code Structure](#code-structure)
8. [Customization](#customization)
9. [Contributing](#contributing)
10. [License](#license)

## Introduction

This project implements a classic Snake game with an AI player using Python and Pygame. The AI uses a Breadth-First Search (BFS) algorithm to find the shortest path to the food while avoiding obstacles. This project serves as an excellent example of pathfinding algorithms and game development in Python.

## Features

- Classic Snake game mechanics
- AI-controlled snake using BFS pathfinding
- Score tracking
- Game over screen showing final game state
- Customizable game parameters (snake speed, grid size, etc.)

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
python snake_game_ai.py
```

## How to Play

- The game starts automatically with the AI controlling the snake.
- Watch as the AI navigates the snake to eat the food and grow longer.
- The game ends when the snake collides with the wall or itself.
- After the game ends, the final state is displayed for 3 seconds before the program closes.

## AI Algorithm

The AI uses a Breadth-First Search (BFS) algorithm to find the shortest path to the food. Here's how it works:

1. The game board is represented as a grid.
2. The snake's body is marked as obstacles in the grid.
3. BFS is used to find the shortest path from the snake's head to the food.
4. If a path is found, the snake moves along that path.
5. If no path is found, the AI tries to move to a safe adjacent cell.
6. If no safe move is available, the snake continues in its current direction.

## Code Structure

- `snake_game_ai.py`: Main game file containing all the code
  - `bfs()`: Implements the Breadth-First Search algorithm
  - `ai_make_decision()`: Decides the next move for the AI
  - `gameLoop()`: Main game loop handling game states and drawing
  - `our_snake()`: Draws the snake on the screen
  - `message()`: Displays text messages on the screen

## Customization

You can customize various aspects of the game by modifying the constants at the beginning of the script:

- `width` and `height`: Change the size of the game window
- `snake_block`: Adjust the size of the snake and food blocks
- `snake_speed`: Modify the speed of the game

## Contributing

Contributions to this project are welcome! Here are some ways you can contribute:

1. Report bugs
2. Suggest enhancements
3. Add new features
4. Improve documentation

Please fork the repository and create a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

---

Enjoy playing and learning from this Snake Game AI! If you have any questions or suggestions, please open an issue on the GitHub repository.
