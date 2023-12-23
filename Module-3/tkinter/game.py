import tkinter as tk
from random import choice

def play(user_choice):
    # Function to handle the game logic when the user makes a choice
    computer_choice = choice(["Rock", "Paper", "Scissors"])

    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "User win!"
        user_scores[0] += 1
    else:
        result = "Computer wins!"
        computer_scores[0] += 1

    
    update_scores()
    label_result["text"] = (f"\n{result}\nUser chose {user_choice}, computer chose {computer_choice}")

def update_scores():
    
    label_user["text"] = f"User: {user_scores[0]}"
    label_computer["text"] = f"Computer: {computer_scores[0]}"

# Initialize scores
user_scores = [0]
computer_scores = [0]

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("700x700")
root.resizable(False,False)

# labels for scores and result
label_user = tk.Label(root, text=f"User Score: {user_scores[0]}", font=("Helvetica", 16))
label_user.pack()

label_computer = tk.Label(root, text=f"Computer Score: {computer_scores[0]}", font=("Helvetica", 16))
label_computer.pack()

label_result = tk.Label(root, text="", font=("Helvetica", 16))
label_result.pack()

#  buttons for  choice 
button_rock = tk.Button(root, text="Rock", command=lambda: play("Rock"), font=("Helvetica", 20), width=7,bg="#5341C5",fg="white")
button_rock.place(x="50",y="320")

button_paper = tk.Button(root, text="Paper", command=lambda: play("Paper"), font=("Helvetica", 20), width=7,bg="#9541C5",fg="white")
button_paper.place(x="250",y="320")

button_scissors = tk.Button(root, text="Scissors", command=lambda: play("Scissors"), font=("Helvetica", 20), width=7,bg="#4171C5",fg="white")
button_scissors.place(x="450",y="320")

# Start the main event loop
root.mainloop()
