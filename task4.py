import tkinter as tk
import random
from tkinter import messagebox


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"
def user_choice(choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"You chose: {choice}\nComputer chose: {computer_choice}\n{result}")

def reset_game():
    result_label.config(text="")
    play_again_button.grid_forget()


def play_again():
    reset_game()
    play_again_button.grid(row=4, column=1)


root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.configure(bg="#e0f7fa")

font = ("Arial", 14)


tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=font, bg="#e0f7fa").grid(row=0, column=0, columnspan=3, pady=20)

rock_button = tk.Button(root, text="Rock", font=font, command=lambda: user_choice('rock'))
rock_button.grid(row=1, column=0, padx=20, pady=10)

paper_button = tk.Button(root, text="Paper", font=font, command=lambda: user_choice('paper'))
paper_button.grid(row=1, column=1, padx=20, pady=10)

scissors_button = tk.Button(root, text="Scissors", font=font, command=lambda: user_choice('scissors'))
scissors_button.grid(row=1, column=2, padx=20, pady=10)

result_label = tk.Label(root, text="", font=font, bg="#e0f7fa")
result_label.grid(row=2, column=0, columnspan=3, pady=20)

play_again_button = tk.Button(root, text="Play Again", font=font, command=play_again)

root.mainloop()
