import random
import time
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.difficulties = {
            "Easy": (50, 8),
            "Medium": (100, 6),
            "Hard": (200, 5)
        }
        self.current_difficulty = "Easy"
        self.high_scores = self.load_high_scores()
        self.answer = None
        self.guesses_left = None
        self.game_active = False
        self.start_time = None
        
        self.setup_gui()
        
    def load_high_scores(self):
        try:
            with open("high_scores.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"Easy": float('inf'), "Medium": float('inf'), "Hard": float('inf')}
            
    def save_high_scores(self):
        with open("high_scores.json", "w") as f:
            json.dump(self.high_scores, f)

    def setup_gui(self):
        # Style configuration
        style = ttk.Style()
        style.configure("TButton", padding=5, font=('Helvetica', 10))
        style.configure("TLabel", font=('Helvetica', 10), background="#f0f0f0")
        
        # Title
        title_label = ttk.Label(
            self.root, 
            text="🎮 Number Guessing Game 🎮",
            font=('Helvetica', 16, 'bold'),
            background="#f0f0f0"
        )
        title_label.pack(pady=20)
        
        # Difficulty selection
        diff_frame = ttk.Frame(self.root)
        diff_frame.pack(pady=10)
        
        ttk.Label(
            diff_frame,
            text="Select Difficulty:",
            font=('Helvetica', 10),
            background="#f0f0f0"
        ).pack(side=tk.LEFT, padx=5)
        
        self.diff_var = tk.StringVar(value="Easy")
        diff_menu = ttk.OptionMenu(
            diff_frame,
            self.diff_var,
            "Easy",
            *self.difficulties.keys(),
            command=self.change_difficulty
        )
        diff_menu.pack(side=tk.LEFT)
        
        # Game info frame
        self.info_frame = ttk.Frame(self.root)
        self.info_frame.pack(pady=10)
        
        self.range_label = ttk.Label(
            self.info_frame,
            text="Range: 1-50",
            background="#f0f0f0"
        )
        self.range_label.pack()
        
        self.guesses_label = ttk.Label(
            self.info_frame,
            text="Guesses left: 8",
            background="#f0f0f0"
        )
        self.guesses_label.pack()
        
        # Input frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)
        
        self.guess_entry = ttk.Entry(input_frame, width=10)
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        
        self.submit_button = ttk.Button(
            input_frame,
            text="Submit Guess",
            command=self.check_guess
        )
        self.submit_button.pack(side=tk.LEFT)
        
        # Feedback label
        self.feedback_label = ttk.Label(
            self.root,
            text="",
            font=('Helvetica', 12),
            background="#f0f0f0"
        )
        self.feedback_label.pack(pady=10)
        
        # High score label
        self.high_score_label = ttk.Label(
            self.root,
            text=f"Best Score: {self.format_high_score(self.high_scores[self.current_difficulty])}",
            background="#f0f0f0"
        )
        self.high_score_label.pack(pady=5)
        
        # Control buttons
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10)
        
        self.start_button = ttk.Button(
            control_frame,
            text="Start New Game",
            command=self.start_game
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to submit guess
        self.root.bind('<Return>', lambda e: self.check_guess())
        
        self.guess_entry.config(state='disabled')
        self.submit_button.config(state='disabled')

    def format_high_score(self, score):
        return "Not set" if score == float('inf') else str(score)

    def change_difficulty(self, difficulty):
        self.current_difficulty = difficulty
        max_num, max_guesses = self.difficulties[difficulty]
        self.range_label.config(text=f"Range: 1-{max_num}")
        self.guesses_label.config(text=f"Guesses left: {max_guesses}")
        self.high_score_label.config(
            text=f"Best Score: {self.format_high_score(self.high_scores[difficulty])}"
        )

    def start_game(self):
        self.current_difficulty = self.diff_var.get()
        max_num, max_guesses = self.difficulties[self.current_difficulty]
        self.answer = random.randint(1, max_num)
        self.guesses_left = max_guesses
        self.game_active = True
        self.start_time = time.time()
        
        self.guess_entry.config(state='normal')
        self.submit_button.config(state='normal')
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()
        
        self.guesses_label.config(text=f"Guesses left: {self.guesses_left}")
        self.feedback_label.config(text="Game started! Make your guess!")
        
    def check_guess(self):
        if not self.game_active:
            return
            
        try:
            guess = int(self.guess_entry.get())
            max_num = self.difficulties[self.current_difficulty][0]
            
            if not (1 <= guess <= max_num):
                messagebox.showwarning(
                    "Invalid Input",
                    f"Please enter a number between 1 and {max_num}!"
                )
                return
                
        except ValueError:
            messagebox.showwarning(
                "Invalid Input",
                "Please enter a valid number!"
            )
            return
            
        self.guess_entry.delete(0, tk.END)
        self.guesses_left -= 1
        self.guesses_label.config(text=f"Guesses left: {self.guesses_left}")
        
        if guess == self.answer:
            elapsed_time = round(time.time() - self.start_time, 2)
            score = self.difficulties[self.current_difficulty][1] - self.guesses_left
            
            if score < self.high_scores[self.current_difficulty]:
                self.high_scores[self.current_difficulty] = score
                self.save_high_scores()
                self.high_score_label.config(
                    text=f"Best Score: {score}"
                )
                
            messagebox.showinfo(
                "Congratulations!",
                f"You found the number {self.answer}!\n"
                f"Time taken: {elapsed_time} seconds\n"
                f"Score: {score} guesses"
            )
            self.end_game()
        else:
            if guess > self.answer:
                self.feedback_label.config(text="📉 Your guess is TOO HIGH!")
            else:
                self.feedback_label.config(text="📈 Your guess is TOO LOW!")
                
            if self.guesses_left == 0:
                messagebox.showinfo(
                    "Game Over",
                    f"Sorry, you're out of guesses! The number was {self.answer}"
                )
                self.end_game()
                
    def end_game(self):
        self.game_active = False
        self.guess_entry.config(state='disabled')
        self.submit_button.config(state='disabled')
        self.feedback_label.config(text="Game Over! Click 'Start New Game' to play again!")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
        