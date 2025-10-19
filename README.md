# Python Practice Projects

Welcome to my Python Learning Journey! This repository showcases my progress in learning Python through hands-on projects. From basic command-line games to API integrations, data visualization, and data analysis applications, each project represents a step forward in mastering Python programming concepts and best practices.

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

   - A shopping cart implementation with product management
   - Add/remove items, calculate total, and view cart

4. **Student Grade Manager** (`studentGradeManager.py`)

   - A system to manage and analyze student grades
   - Add students, record grades, calculate averages

5. **Unique Word Counter** (`unique_word_counter.py`)

   - A tool to count and analyze unique words in text
   - Text analysis and frequency counting

6. **Weather API Integration** (`weatherAPI.py`)

   - Real-time weather information retrieval
   - API integration with weather services

7. **Banking System** (`banking_system.py`)

   - Basic banking operations simulation
   - Account management, deposits, withdrawals

8. **Calculator** (`calculator.py`)

   - A command-line calculator application
   - Basic arithmetic operations

9. **Sales Analyzer** (`sales_analyzer.py`)

   - Data analysis tool for sales data
   - CSV file processing and analysis
   - Generates insights from sales records

10. **Movies Management** (`movies_set.py`)

    - Movie database management system
    - Data handling with CSV files

11. **Auto Messenger** (`auto_messenger.py`)

    - Automated messaging system
    - Message scheduling and delivery

12. **AI Utilities** (`ai_utils.py`)

    - Collection of AI-related utility functions
    - Helper tools for AI/ML tasks
    - Includes: text cleaning, word counting, average calculations, percentage functions
    - Used by `main.py` as a demonstration of modular programming

13. **NumPy Practice** (`NumPy.py`)

    - Exercises and examples using NumPy
    - Numerical computing demonstrations

14. **Matplotlib Visualization** (`mat-plot.py`)

    - Comprehensive data visualization examples using Matplotlib
    - Features:
      - Line plots with custom styling (markers, colors, line styles)
      - Bar charts (vertical and horizontal)
      - Pie charts with custom colors and effects
      - Scatter plots for correlation analysis
      - Histograms for data distribution
      - Subplots for multiple visualizations
      - Pandas integration with movie data analysis
    - Demonstrates visualization of IMDb ratings distribution

15. **Environment Configuration Demo** (`try.py`)

    - Demonstrates environment variable management
    - Uses `python-dotenv` for secure API key handling
    - Best practices for configuration management

16. **Main Demo** (`main.py`)
    - Demonstrates importing and using custom modules
    - Showcases the AI utilities module in action

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

## Technical Requirements

- Python 3.x
- Required packages:
  - `numpy` (for NumPy.py and mat-plot.py)
  - `pandas` (for data analysis projects and mat-plot.py)
  - `matplotlib` (for mat-plot.py data visualization)
  - `requests` (for weatherAPI.py)
  - `python-dotenv` (for try.py environment variable management)
  - Other dependencies as specified in individual projects

## How to Run the Projects

1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install numpy pandas matplotlib requests python-dotenv
   ```
3. For projects using environment variables (like `try.py`):
   - Create a `.env` file in the project root
   - Add your API keys and configuration variables
4. Navigate to the project directory
5. Run any project using Python:
   ```bash
   python <filename>.py
   ```

## Project Structure

```
├── .env                    # Environment variables (not tracked in git)
├── .gitignore             # Git ignore configuration
├── ai_utils.py            # AI utility functions module
├── auto_messenger.py      # Automated messaging system
├── banking_system.py      # Banking operations simulator
├── calculator.py          # Command-line calculator
├── data.json              # JSON data file
├── journal.txt            # Journal entries storage
├── main.py                # Demo of ai_utils module usage
├── mat-plot.py            # Matplotlib visualization examples
├── movie_data.csv         # Movie dataset (CSV format)
├── movie_data.txt         # Movie dataset (text format)
├── movies_set.py          # Movie database manager
├── numberguessing.py      # Number guessing game
├── NumPy.py               # NumPy practice exercises
├── sales_analyzer.py      # Sales data analysis tool
├── sales_data.csv         # Sales dataset
├── shoppingcart.py        # Shopping cart system
├── studentGradeManager.py # Student grade management
├── transactions.txt       # Banking transactions log
├── try.py                 # Environment variables demo
├── unique_word_counter.py # Word analysis tool
├── user_journal.py        # Journal application
└── weatherAPI.py          # Weather API integration
```

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

Replace `<script_name>` with the name of the Python file you want to run (e.g., `numberguessing.py`, `user_journal.py`, `mat-plot.py`, etc.).

## Data Files

The repository includes several data files for practicing data analysis:

- `data.json` - JSON format data for structured data handling
- `movie_data.csv` / `movie_data.txt` - Movie datasets for analysis and visualization
- `sales_data.csv` - Sales records for business analytics
- `journal.txt` - Persistent storage for journal entries
- `transactions.txt` - Banking transaction records

## Learning Concepts Covered

This repository demonstrates proficiency in:

- **Basic Python**: Variables, loops, conditionals, functions
- **File I/O**: Reading and writing files (TXT, CSV, JSON)
- **Data Structures**: Lists, dictionaries, sets
- **External Libraries**: NumPy, Pandas, Matplotlib, Requests
- **API Integration**: Working with external APIs (Weather)
- **Data Visualization**: Charts, plots, and graphs with Matplotlib
- **Modular Programming**: Creating and importing custom modules
- **Environment Management**: Using .env files for configuration
- **Object-Oriented Programming**: Classes and objects
- **Error Handling**: Try-except blocks and validation
- **Data Analysis**: Statistical analysis and insights generation

## Repository Information

- **Repository**: Number-Guessing
- **Owner**: Panendar
- **Last Updated**: October 2025

---

Feel free to explore each project and learn from the code! Each project is self-contained and can be run independently.
