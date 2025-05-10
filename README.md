# Space Invaders Game

A Python implementation of the classic Space Invaders arcade game using the Turtle graphics library.

![image](https://github.com/user-attachments/assets/cc1455b2-2acc-4e05-a393-185951562d24)


## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Controls](#controls)
- [Game Mechanics](#game-mechanics)
- [Contributing](#contributing)
- [License](#license)

## Description

This Space Invaders game is a Python implementation of the classic arcade game first released in 1978. The player controls a spaceship at the bottom of the screen, shooting at alien invaders that move in formation across and down the screen. Defensive barriers provide temporary protection from alien attacks.

## Features

- Classic Space Invaders gameplay
- Smooth animations using Turtle graphics
- Multiple rows of alien enemies
- Defensive barriers
- Score tracking system with high score saving
- Level progression
- Collision detection
- Game over screen

## Installation

1. Make sure you have Python 3.x installed on your system
2. Clone this repository to your local machine:
   ```
   git clone https://github.com/yourusername/SpaceInvaders_Game.git
   ```
3. Navigate to the project directory:
   ```
   cd SpaceInvaders_Game
   ```
4. Run the game:
   ```
   python main.py
   ```

## How to Play

The objective is to eliminate all alien invaders while avoiding their projectiles. The game becomes progressively more challenging as you advance through levels.

## Project Structure

The game is organized into multiple Python files, each handling a specific aspect of gameplay:

- `main.py` - The main game loop and gameplay coordination
- `spaceship.py` - Player-controlled spaceship functionality
- `aliens.py` - Alien enemies and their behavior
- `barrier.py` - Defensive barriers
- `scorecard.py` - Score tracking and display
- `high_score.txt` - File storing the highest score achieved

## Controls

- **A key**: Move spaceship left
- **D key**: Move spaceship right
- **C key**: Shoot

## Game Mechanics

### Spaceship
- The player controls a blue spaceship at the bottom of the screen
- The spaceship can move left and right and shoot projectiles upward
- The player can have up to 5 bullets on screen at once

### Aliens
- Multiple rows of green alien invaders move in formation
- Aliens periodically shoot red projectiles downward
- When all aliens are destroyed, a new wave appears and the level increases

### Barriers
- White barriers provide protection from alien projectiles
- Barriers can be damaged and destroyed by both alien and player projectiles

### Scoring
- Each alien destroyed awards 10 points
- The high score is saved between game sessions
- The current score, level, and high score are displayed at the top of the screen

### Game Over
- The game ends if an alien projectile hits the player's spaceship
- The game also ends if any alien reaches the bottom of the screen or collides with the player
- When the game ends, a "GAME OVER" message appears with the final score

## Contributing

Contributions to improve the game are welcome! Please feel free to fork the repository, make changes, and submit a pull request.

Possible enhancements:
- Add sound effects
- Add different types of aliens with varying behaviors
- Implement power-ups
- Create start menu and difficulty options
- Add animations for explosions

## License

This project is licensed under the MIT License - see the LICENSE file for details.

