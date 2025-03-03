# Car Racing Game - Pygame

## Overview
This repository contains a simple 2D Car Racing Game built using the Pygame library in Python. The objective of the game is to control a car, avoid obstacles, and score as many points as possible. The game features dynamic obstacle spawning, collision detection, and a scoring system.

## Game Features
- **Player Car:**
  - Controlled using arrow keys (LEFT, RIGHT, UP, DOWN) or WASD.
  - Represented by a red rectangle with a windshield and wheels.
- **Obstacles:**
  - Blue cars move down the screen at random speeds.
  - Obstacles respawn at the top of the screen after passing the bottom.
  - Speed of obstacles increases as the player's score increases.
- **Scoring System:**
  - Players earn 10 points for each obstacle that passes the bottom of the screen.
  - Score is displayed at the top-left corner of the screen.
- **Collision Detection:**
  - Detects collisions between the player's car and obstacles.
  - The game ends upon collision.
- **Game Over Screen:**
  - Displays "Game Over!" along with options to restart or quit the game.

## How to Play
### Clone the Repository:
```bash
git clone https://github.com/neyamul-hasan14/Car-Racing-Game-Pygame.git
```
### Navigate to the Project Directory:
```bash
cd Car-Racing-Game-Pygame
```
### Run the Game:
```bash
python cargame.py
```
### Controls:
- **Arrow Keys or WASD**: Move the car.
- **SPACE**: Restart the game after a game over.
- **ESC**: Quit the game.

## Dependencies
- Python 3.x
- Pygame (Install using pip):
```bash
pip install pygame
```

## Code Structure
- **Player Class**: Handles the player's car, including movement and drawing.
- **Obstacle Class**: Manages the behavior of obstacles, including movement, collision detection, and respawning.
- **Score Class**: Tracks and updates the player's score.
- **Main Game Loop**: Manages the game state, including rendering, event handling, and collision detection.

## Screenshots
Gameplay:

Game Over Screen:

## Future Improvements
- Add more types of obstacles (e.g., trucks, motorcycles).
- Introduce power-ups (e.g., speed boosts, invincibility).
- Add sound effects and background music.
- Implement a high-score system to save the player's best score.

## Conclusion
This project is a fun and simple implementation of a 2D car racing game using Pygame. It demonstrates fundamental game development concepts such as rendering, collision detection, and event handling. Feel free to fork the repository and add your own features!

