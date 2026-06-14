import tkinter as tk
from tkinter import messagebox, simpledialog

# Stores the top quiz scores and player names
leaderboard = []
scoreboard_label = None
error_dialog_open = False  # Flag to prevent multiple error dialogs

def open_quiz_page():
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz Page")
    quiz_window.geometry("1920x1080")

    root.iconify()  # Minimise the home page while the quiz is being played

    # Helper function to bring back home screen and close quiz
    def close_quiz_and_restore_home():
        root.deiconify()  # Unminimizes/restores home page
        quiz_window.destroy()  # Closes quiz page

    # Bind the window close 'X' button to restore the home page
    quiz_window.protocol("WM_DELETE_WINDOW", close_quiz_and_restore_home)

    # Title label for the quiz page
    tk.Label(
        quiz_window,
        text="Welcome to the Quiz Page!",
        font=("Arial", 18)
    ).pack(pady=20)

    # Prompt the user for their name
    player_name = simpledialog.askstring("Player Name", "Enter your name:")
    if not player_name:
        player_name = "Anonymous"

    # Quiz questions
    quiz_questions = [
        {"prompt": "What does 'Mahi' translate to?", "options": ["Work", "Car", "Fish", "School"], "answer": "Work"},
        {"prompt": "What does 'Whānau' translate to?", "options": ["Clothing", "Bird", "Family", "Food"], "answer": "Family"},
        {"prompt": "What does 'Aroha' translate to?", "options": ["Love", "Hate", "Friendship", "Money"], "answer": "Love"},
        {"prompt": "What does 'Kia ora' commonly mean?", "options": ["Goodbye", "Hello", "Please", "Sorry"], "answer": "Hello"},
        {"prompt": "What does 'Mana' most closely refer to?", "options": ["Prestige", "Water", "Food", "Clothing"], "answer": "Prestige"}
    ]

    current_question = 0
    score = 0

    # Create a label to display the quiz question
    question_label = tk.Label(
        quiz_window,
        text="",
        font=("Arial", 16),
        wraplength=600
    )
    question_label.pack(pady=20)

    # No button selected by default
    selected_answer = tk.StringVar(value="NONE")

    # Create 4 radio buttons for the answer options
    option_buttons = []
    for i in range(4):
        button = tk.Radiobutton(
            quiz_window,
            text="",
            variable=selected_answer,
            value=f"temp{i}",
            font=("Arial", 14)
        )
        button.pack(anchor="w", padx=200, pady=5)
        option_buttons.append(button)

    def load_question():
        selected_answer.set("NONE")
        question = quiz_questions[current_question]
        question_label.config(text=question["prompt"])
        for i, option in enumerate(question["options"]):
            option_buttons[i].config(
                text=option,
                value=option
            )

    def show_results():
        # Remove all option buttons and the next button
        for button in option_buttons:
            button.destroy()
        next_button.destroy()

        # Calculate the percentage score
        percentage = round((score / len(quiz_questions)) * 100)

        # Update the question label to show the final score
        question_label.config(
            text=(f"Quiz Complete!\n\n"
                  f"Score: {score}/{len(quiz_questions)}\n"
                  f"Percentage: {percentage}%")
        )

        # Add the player's score to the leaderboard
        leaderboard.append({"name": player_name, "score": score, "total": len(quiz_questions)})
        update_scoreboard()

        # Add a return button
        return_button = tk.Button(
            quiz_window,
            text="Return to Home Page",
            font=("Arial", 14),
            width=20,
            command=close_quiz_and_restore_home
        )
        return_button.pack(pady=20)

    def next_question():
        nonlocal current_question, score
        global error_dialog_open

        if selected_answer.get() == "NONE":
            if not error_dialog_open:  # Prevent multiple error dialogs
                error_dialog_open = True
                messagebox.showwarning(
                    "No Answer Selected",
                    "Please choose an answer first."
                )
                error_dialog_open = False
            return

        if selected_answer.get() == quiz_questions[current_question]["answer"]:
            score += 1

        current_question += 1

        if current_question < len(quiz_questions):
            load_question()
        else:
            show_results()

    # Next question button
    next_button = tk.Button(
        quiz_window,
        text="Next Question",
        font=("Arial", 14),
        command=next_question
    )
    next_button.pack(pady=20)

    load_question()

def update_scoreboard():
    """Updates the scoreboard shown on the home page."""
    if not leaderboard:
        text = "🏆 Scoreboard\n\nNo scores yet"
    else:
        text = "🏆 Scoreboard\n\n"
        sorted_scores = sorted(leaderboard, key=lambda x: x["score"], reverse=True)
        for position, player in enumerate(sorted_scores[:5], start=1):
            percentage = round((player["score"] / player["total"]) * 100)
            text += f"{position}. {player['name']} - {player['score']}/{player['total']} ({percentage}%)\n"
    scoreboard_label.config(text=text)

def home_page():
    global root, scoreboard_label

    # Create the main program window
    root = tk.Tk()
    root.title("Ngā kupu Māori Quest")
    root.geometry("1900x1000")

    # Title label
    status = tk.Label(
        root,
        text="Welcome to Ngā kupu Māori Quest!",
        font=("Arial", 50, "bold")
    )
    status.pack(pady=20)

    # Create a frame for the scoreboard on the left side
    scoreboard_frame = tk.Frame(root, width=400, height=800, bg="lightgray")
    scoreboard_frame.pack(side="left", fill="y")

    # Scoreboard label inside the frame
    scoreboard_label = tk.Label(
        scoreboard_frame,
        text="🏆 Scoreboard\n\nNo scores yet",
        font=("Arial", 18),
        justify="left",
        bg="lightgray"
    )
    scoreboard_label.pack(pady=20, padx=10)

    # Quiz button
    quiz_button = tk.Button(
        root,
        text="Quiz",
        command=open_quiz_page,
        width=50,
        height=5
    )
    quiz_button.pack(pady=20)

    # Start the Tkinter loop
    root.mainloop()

if __name__ == "__main__":
    home_page()