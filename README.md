# Number Guessing Game

A simple command-line number guessing game implemented in Python where players try to guess a randomly generated number between 1 and 50.

## Description

This is a fun and interactive game where:
- The computer generates a random number between 1 and 50
- Players have 5 attempts to guess the correct number
- After each guess, the game provides hints whether the guess is too high or too low
- Players win by guessing the correct number within the allowed attempts

## How to Play

1. Run the Python script `number_guessing.py`
2. Enter a number between 1 and 50 when prompted
3. The game will tell you if your guess is too high or too low
4. You have 5 chances to guess the correct number
5. Keep guessing until you find the correct number or run out of attempts

## Features

- Random number generation between 1-50
- 5 attempts to guess the number
- Helpful hints after each guess
- Clear feedback messages
- Simple and user-friendly interface

## Requirements

- Python 3.x
- `random` module (built into Python)

## How to Run

```bash
python number_guessing.py
```

## Game Rules

1. The number to guess is between 1 and 50
2. You have 5 attempts to guess the correct number
3. After each incorrect guess, you'll be told if your guess was too high or too low
4. The game ends when you either:
   - Guess the correct number (You win!)
   - Use all 5 attempts (Game over)
