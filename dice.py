import tkinter as tk
from tkinter import ttk
import random
 
#Rolling the dice
def roll_dice():
    return random.randint(1, 6)

#update the board with the dice result
def update_board():
    dice_result = roll_dice()
    result_label.config(text=f"Dice Roll: {dice_result}")

    #Clear the board
    for button in board_buttons:
        button.config(text="")
    #conditions for result to  be place as circle in cells
    if dice_result == 6:
        # Place circles in cells [0,2,3,5,6,8]
        for i in [0, 2, 3, 5, 6, 8]:
            board_buttons[i].config(text="O")
    elif dice_result == 5:
        # Place circles in cells [0,2,4,6,8]
        for i in [0, 2, 4, 6, 8]:
            board_buttons[i].config(text="O")
    elif dice_result == 4:
        # Place circles in cells [0,2,6,8]
        for i in [0, 2, 6, 8]:
            board_buttons[i].config(text="O")
    elif dice_result == 3:
        # Place circles in cells [2,4,6]
        for i in [2, 4, 6]:
            board_buttons[i].config(text="O")
    elif dice_result == 2:
        # Place circles in cells [0,8]
        for i in [0, 8]:
            board_buttons[i].config(text="O")
    elif dice_result == 1:
        # Place a circle in cell 4 (middle)
        board_buttons[4].config(text="O")

    #Update the history
    history.append(dice_result)
    update_history_tree()

def update_history_tree():
    
    for item in history_tree.get_children():
        history_tree.delete(item)

    # Add rounds to the history treeview
    rounds = [history[i:i+10] for i in range(0, len(history), 10)]
    for i, round_results in enumerate(rounds, start=1):
        round_str = " ".join(map(str, round_results))
        history_tree.insert("", "end", values=(f"Round {i}", round_str))

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe with Dice")

# Create a label to display the dice result
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=0, column=0, padx=10, pady=10)

# Create a frame for the Tic Tac Toe board
board_frame = tk.Frame(root)
board_frame.grid(row=1, column=0)

# Create buttons for the Tic Tac Toe board
board_buttons = []
for i in range(9):
    button = tk.Button(board_frame, text="", font=("Helvetica", 24), width=4, height=2)
    button.grid(row=i // 3, column=i % 3)
    board_buttons.append(button)

# Create a button to roll the dice and update the board
roll_button = tk.Button(root, text="Roll Dice and Play", command=update_board, font=("Helvetica", 16))
roll_button.grid(row=2, column=0, padx=10, pady=10)

# Create a history treeview with columns for Round and Results
history_tree = ttk.Treeview(root, columns=("Round", "Results"), show="headings")
history_tree.heading("Round", text="Round")
history_tree.heading("Results", text="Results")
history_tree.column("Round", width=110, anchor="center")
history_tree.column("Results", width=300, anchor="center")  # Adjust the width as needed
history_tree.grid(row=3, column=0, padx=10, pady=10)

# Initialize the history list to store results
history = []

# Start the main event loop

#to reset the results
def reset_game():
    global history
    history = []
    result_label.config(text="")
    for button in board_buttons:
        button.config(text="")
    update_history_tree()

#button for the result
 
reset_button = tk.Button(root, text="Clear and Retry", command=reset_game, font=("Helvetica", 16))
reset_button.grid(row=4, column=0, padx=10, pady=10)

root.mainloop()
