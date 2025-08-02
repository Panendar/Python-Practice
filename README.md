# Python Practice Projects

Welcome to my Python Learning Journey! This repository showcases my progress in learning Python through hands-on projects. From basic command-line games to file handling applications, each project represents a step forward in mastering Python programming concepts and best practices.

## Project Directory

1. **Number Guessing Game** (`numberguessing.py`)
   - A fun game where players guess a number between 1-50
   - Features random number generation and user hints

2. **User Journal** (`user_journal.py`)
   - A personal journal application with file handling
   - Features:
     - Write journal entries with timestamps
     - Read all journal entries in formatted view
     - Search entries by date
     - Exit functionality

3. **Shopping Cart** (`shoppingcart.py`)
   - A shopping cart implementation

4. **Student Grade Manager** (`studentGradeManager.py`)
   - A system to manage student grades

5. **Unique Word Counter** (`unique_word_counter.py`)
   - A tool to count unique words

## Projects Details

### Number Guessing Game

## Description

This is a fun and interactive game where:
- The computer generates a random number between 1 and 50
- Players have 5 attempts to guess the correct number
- After each guess, the game provides hints whether the guess is too high or too low
- Players win by guessing the correct number within the allowed attempts

## How to Play

1. Run the Python script `numberguessing.py`
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
python numberguessing.py
```

## Game Rules

1. The number to guess is between 1 and 50
2. You have 5 attempts to guess the correct number
3. After each incorrect guess, you'll be told if your guess was too high or too low
4. The game ends when you either:
   - Guess the correct number (You win!)
   - Use all 5 attempts (Game over)

### User Journal Application

## Description

A command-line journal application that allows users to write, read, and search journal entries. Each entry is saved with a timestamp for easy tracking and searching.

## Features

- Write journal entries with automatic timestamps
- Read all entries in a formatted, easy-to-read view
- Search entries by specific dates (YYYY-MM-DD)
- Persistent storage using text files
- User-friendly menu interface

## How to Use

1. Run the Python script `user_journal.py`
2. Choose from the following options:
   - 1: Write a new journal entry
   - 2: Read all journal entries
   - 3: Search entries by date
   - 4: Exit the application

## Technical Features

- File handling with `open()` for persistent storage
- DateTime manipulation for timestamps
- Error handling for file operations
- Global variable management
- String formatting and text processing

## Requirements

- Python 3.x
- No additional packages required

## How to Run Any Project

```bash
python <script_name>.py
```

Replace `<script_name>` with the name of the Python file you want to run (e.g., `numberguessing.py`, `user_journal.py`, etc.).

## Project Structure

```
Python-practice/
├── README.md
├── numberguessing.py
├── user_journal.py
├── shoppingcart.py
├── studentGradeManager.py
├── unique_word_counter.py
└── journal.txt
```
