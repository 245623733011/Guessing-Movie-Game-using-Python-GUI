import random
import tkinter as tk
from tkinter import messagebox

# List of movie names for guessing
movies = [
    "Mr.Bachchan", "Hanu-Man", "Eagle", "Maharaja", "Satyabhama", "Buddy", 
    "Raayan", "Ooru Peru Bhairavakona", "Kalki", "The Family Star", "Saindhav", 
    "Om Bheem Bush", "Nannaku Prematho", "Chatrapathi", "Loafer", "Oke Oka Jeevitham", 
    "Bimbisara", "Ori Devuda", "Purushothamudu", "Naa Saami Ranga", "Guntur Kaaram", 
    "Double Ismart", "Aa Okkati Adakku", "Jawan", "Salaar", "Extra Ordinary Man", 
    "Hi Nanna", "Bhagavanth Kesari", "Virupaksha", "Aadikeshava", "Kalyanam Kamaneeyam", 
    "Samajavaragamana", "Rangabali", "Bedurulanka", "Waltair Veerayya", "Ravanasura", 
    "Premadesam"
]

# Variables to keep track of the game state
current_player = 1
player1_score = 0
player2_score = 0
turn_count = 0
total_turns = 5  # Number of turns for each player

# Function to shuffle the letters in the movie title
def shuffle_movie(movie):
    shuffled = list(movie)
    random.shuffle(shuffled)
    return ''.join(shuffled)

# Function to reset the game with a new movie
def reset_game():
    global current_movie, turn_count, current_player
    if turn_count < total_turns * 2:  # Each player gets 'total_turns' turns
        current_movie = random.choice(movies).upper()
        scrambled_movie.set(shuffle_movie(current_movie))
        guess_entry.delete(0, tk.END)
        update_turn_label()
    else:
        declare_winner()

# Function to check the guess entered by the player
def check_guess():
    global player1_score, player2_score, current_player, turn_count
    guess = guess_entry.get().upper()
    
    if guess == current_movie:
        if current_player == 1:
            player1_score += 1
            messagebox.showinfo("Correct!", "Player 1 guessed the movie!")
        else:
            player2_score += 1
            messagebox.showinfo("Correct!", "Player 2 guessed the movie!")
    else:
        messagebox.showwarning("Incorrect", "Wrong guess! Try again.")

    # Move to the next player
    turn_count += 1
    current_player = 2 if current_player == 1 else 1
    reset_game()

# Function to update the turn label to show whose turn it is
def update_turn_label():
    turn_label.config(text=f"Player {current_player}'s turn")

# Function to declare the winner
def declare_winner():
    if player1_score > player2_score:
        winner = "Player 1"
    elif player2_score > player1_score:
        winner = "Player 2"
    else:
        winner = "It's a tie!"
    
    messagebox.showinfo("Game Over", f"Final Scores:\nPlayer 1: {player1_score}\nPlayer 2: {player2_score}\n\n{winner} wins!")
    root.quit()

# Setting up the main window
root = tk.Tk()
root.title("Two-Player Movie Guessing Game")
root.geometry("600x400")
root.configure(bg="black")  # Set the window background to black

# Creating and placing widgets
scrambled_movie = tk.StringVar()

# Title of the game (place it over the background)
title_label = tk.Label(root, text="Two-Player Movie Guessing Game", font=("Arial", 24, "bold"), bg="black", fg="white")
title_label.pack(pady=20)

# Instructions for the player (place it over the background)
instructions_label = tk.Label(root, text="Instructions: Unscramble the letters to guess the movie name.\nEach player takes turns guessing. After 5 rounds, the winner will be declared.",
                              font=("Arial", 14), justify="center", bg="black", fg="white")
instructions_label.pack(pady=10)

# Scrambled movie display
scrambled_label = tk.Label(root, textvariable=scrambled_movie, font=("Arial", 36), bg="black", fg="yellow")
scrambled_label.pack(pady=20)

# Label to show whose turn it is
turn_label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 16), bg="black", fg="white")
turn_label.pack()

# Label for input field
guess_label = tk.Label(root, text="Enter your guess:", font=("Arial", 16), bg="black", fg="white")
guess_label.pack()

# Entry widget for the user to type the guess
guess_entry = tk.Entry(root, font=("Arial", 20))
guess_entry.pack(pady=10)

# Button to check the guess
check_button = tk.Button(root, text="Check Guess", command=check_guess, font=("Arial", 16), bg="blue", fg="white")
check_button.pack(pady=10)

# Reset button to start a new game
reset_button = tk.Button(root, text="Reset", command=reset_game, font=("Arial", 16), bg="red", fg="white")
reset_button.pack(pady=10)

# Initialize the game with the first movie
reset_game()

# Start the Tkinter event loop
root.mainloop()
