# Import the tkinter library and rename it as "tk"
# tkinter is used to create graphical user interfaces (GUIs)
import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from collections import deque  # deque is used as a queue to manage quiz questions


# Leaderboard class - stores and displays scores
class Leaderboard:
    def __init__(self, parent):
        # Initializes the Leaderboard with a parent widget and sets up the frame and label
        self.parent = parent
        self.leaderboard_data = []  # Stores the top quiz scores and player names

        # Create a frame for the leaderboard on the left side of the window
        self.frame = tk.Frame(self.parent, width=400, height=800, bg="lightgray")
        self.frame.pack(side="left", fill="y")

        # Create a label inside the frame to display the leaderboard text
        self.label = tk.Label(
            self.frame,
            text="🏆 Scoreboard\n\nNo scores yet",
            font=("Arial", 18),
            justify="left",
            bg="lightgray"
        )
        self.label.pack(pady=20, padx=10)

    def add_score(self, name, score, total):
        # Adds a player's score to the leaderboard data and refreshes the display
        self.leaderboard_data.append({"name": name, "score": score, "total": total})
        self.update_leaderboard()

    def update_leaderboard(self):
        # Updates the leaderboard display with the top 5 scores, sorted highest first
        if not self.leaderboard_data:
            text = "🏆 Scoreboard\n\nNo scores yet"
        else:
            text = "🏆 Scoreboard\n\n"
            # Sort scores from highest to lowest
            sorted_scores = sorted(
                self.leaderboard_data,
                key=lambda x: x["score"],
                reverse=True
            )
            # Display the top 5 scores
            for position, player in enumerate(sorted_scores[:5], start=1):
                percentage = round((player["score"] / player["total"]) * 100)
                text += (
                    f"{position}. {player['name']} - "
                    f"{player['score']}/{player['total']} ({percentage}%)\n"
                )
        self.label.config(text=text)


# QuizPage class - manages the quiz window, question queue, and scoring
class QuizPage:
    def __init__(self, parent, leaderboard):
        # Store references to the home window and leaderboard
        self.parent = parent
        self.leaderboard = leaderboard
        self.score = 0
        self.warning_window = None  # Tracks the open warning popup

        # Create the quiz window
        self.quiz_window = tk.Toplevel(self.parent)
        self.quiz_window.title("Quiz Page")
        self.quiz_window.geometry("390x844")

        # Minimise the home page while the quiz is open
        self.parent.iconify()

        # Bind the window's X button to the restore function
        self.quiz_window.protocol(
            "WM_DELETE_WINDOW", self.close_quiz_and_restore_home
        )

        # Title label for the quiz page
        tk.Label(
            self.quiz_window,
            text="Welcome to the Quiz Page!",
            font=("Arial", 18)
        ).pack(pady=20)

        # Ask the player for their name; default to "Anonymous" if left blank
        self.player_name = simpledialog.askstring("Player Name", "Enter your name:")
        if not self.player_name:
            self.player_name = "Anonymous"

        # All 25 quiz questions stored in a list before being loaded into the queue
        all_questions = [
            {"prompt": "What does 'Mahi' translate to?",
             "options": ["Work", "Car", "Fish", "School"], "answer": "Work"},
            {"prompt": "What does 'Whānau' translate to?",
             "options": ["Clothing", "Bird", "Family", "Food"], "answer": "Family"},
            {"prompt": "What does 'Aroha' translate to?",
             "options": ["Love", "Hate", "Friendship", "Money"], "answer": "Love"},
            {"prompt": "What does 'Kia ora' commonly mean?",
             "options": ["Goodbye", "Hello", "Please", "Sorry"], "answer": "Hello"},
            {"prompt": "What does 'Mana' most closely refer to?",
             "options": ["Prestige", "Water", "Food", "Clothing"], "answer": "Prestige"},
            {"prompt": "What does 'Kai' translate to?",
             "options": ["Food", "House", "Book", "Road"], "answer": "Food"},
            {"prompt": "What does 'Wai' translate to?",
             "options": ["Water", "Fire", "Wind", "Tree"], "answer": "Water"},
            {"prompt": "What does 'Tamariki' translate to?",
             "options": ["Parents", "Children", "Teachers", "Friends"], "answer": "Children"},
            {"prompt": "What does 'Kura' translate to?",
             "options": ["Hospital", "School", "Market", "Church"], "answer": "School"},
            {"prompt": "What does 'Waka' translate to?",
             "options": ["Boat/Canoe", "Mountain", "Food", "Bird"], "answer": "Boat/Canoe"},
            {"prompt": "What does 'Whare' translate to?",
             "options": ["House", "River", "Tree", "Road"], "answer": "House"},
            {"prompt": "What does 'Moana' translate to?",
             "options": ["Ocean", "Forest", "Mountain", "Valley"], "answer": "Ocean"},
            {"prompt": "What does 'Maunga' translate to?",
             "options": ["Lake", "Mountain", "Beach", "Cloud"], "answer": "Mountain"},
            {"prompt": "What does 'Awa' translate to?",
             "options": ["River", "Ocean", "Road", "Bridge"], "answer": "River"},
            {"prompt": "What does 'Rangi' translate to?",
             "options": ["Sky", "Earth", "Sea", "Tree"], "answer": "Sky"},
            {"prompt": "What does 'Whenua' translate to?",
             "options": ["Land", "House", "Food", "Water"], "answer": "Land"},
            {"prompt": "What does 'Hoa' translate to?",
             "options": ["Friend", "Enemy", "Teacher", "Parent"], "answer": "Friend"},
            {"prompt": "What does 'Hapū' translate to?",
             "options": ["Sub-tribe", "Mountain", "School", "River"], "answer": "Sub-tribe"},
            {"prompt": "What does 'Iwi' translate to?",
             "options": ["Tribe", "Food", "Family", "Village"], "answer": "Tribe"},
            {"prompt": "What does 'Kaumātua' translate to?",
             "options": ["Elder", "Child", "Warrior", "Teacher"], "answer": "Elder"},
            {"prompt": "What does 'Pukapuka' translate to?",
             "options": ["Book", "Chair", "Table", "Pen"], "answer": "Book"},
            {"prompt": "What does 'Kākahu' translate to?",
             "options": ["Clothing", "Food", "Water", "House"], "answer": "Clothing"},
            {"prompt": "What does 'Kurī' translate to?",
             "options": ["Dog", "Cat", "Horse", "Bird"], "answer": "Dog"},
            {"prompt": "What does 'Manu' translate to?",
             "options": ["Bird", "Fish", "Tree", "Mountain"], "answer": "Bird"},
            {"prompt": "What does 'Rākau' translate to?",
             "options": ["Tree", "River", "Cloud", "House"], "answer": "Tree"},
        ]

        # Shuffle question order and each question's options
        random.shuffle(all_questions)
        for q in all_questions:
            random.shuffle(q["options"])

        # Load the shuffled questions into a deque to use as a queue
        # popleft() removes and returns from the front, acting as a FIFO queue
        self.question_queue = deque(all_questions)
        self.total_questions = len(self.question_queue)

        # Label that shows the current question text
        self.question_label = tk.Label(
            self.quiz_window,
            text="",
            font=("Arial", 13),
            wraplength=340
        )
        self.question_label.pack(pady=20)

        # StringVar to track which radio button the player has selected
        self.selected_answer = tk.StringVar(value="NONE")

        # Create 4 radio buttons (text/value filled in by load_question)
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                self.quiz_window,
                text="",
                variable=self.selected_answer,
                value=f"temp{i}",
                font=("Arial", 12)
            )
            btn.pack(anchor="w", padx=20, pady=5)
            self.option_buttons.append(btn)

        # Button to submit the answer and move on
        self.next_button = tk.Button(
            self.quiz_window,
            text="Next Question",
            font=("Arial", 14),
            command=self.next_question
        )
        self.next_button.pack(pady=20)

        # Load the first question from the queue
        self.load_question()

    def close_quiz_and_restore_home(self):
        # Closes the quiz window and restores the home page
        self.parent.deiconify()
        self.quiz_window.destroy()

    def load_question(self):
        # Peeks at the front of the queue to display the current question
        self.selected_answer.set("NONE")
        question = self.question_queue[0]
        self.question_label.config(text=question["prompt"])
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def show_results(self):
        # Removes quiz controls and displays the final score, then saves to leaderboard
        for btn in self.option_buttons:
            btn.destroy()
        self.next_button.destroy()

        # Calculate the percentage score
        percentage = round((self.score / self.total_questions) * 100)

        # Update the question label to show the final score
        self.question_label.config(
            text=(
                f"Quiz Complete!\n\n"
                f"Score: {self.score}/{self.total_questions}\n"
                f"Percentage: {percentage}%"
            )
        )

        # Save the score to the leaderboard using the Leaderboard class
        self.leaderboard.add_score(self.player_name, self.score, self.total_questions)

        # Add a return button to go back to the home page
        tk.Button(
            self.quiz_window,
            text="Return to Home Page",
            font=("Arial", 14),
            width=20,
            command=self.close_quiz_and_restore_home
        ).pack(pady=20)

    def next_question(self):
        # Checks the selected answer, updates the score, and moves to the next question
        # Warn the player if they haven't picked an answer yet
        if self.selected_answer.get() == "NONE":
            if self.warning_window is not None:
                self.warning_window.destroy()
            self.warning_window = tk.Toplevel(self.quiz_window)
            self.warning_window.title("No Answer Selected")
            self.warning_window.geometry("300x100")
            tk.Label(
                self.warning_window,
                text="Please choose an answer first.",
                font=("Arial", 12)
            ).pack(pady=20)
            return

        # Pop the current question off the front of the queue
        current_question = self.question_queue.popleft()

        # Award a point if the answer is correct
        if self.selected_answer.get() == current_question["answer"]:
            self.score += 1

        # Either load the next question or show the results screen
        if self.question_queue:
            self.load_question()
        else:
            self.show_results()


# Builds and displays the main home page window
def home_page():
    global root, leaderboard

    # Create the main program window
    root = tk.Tk()
    root.title("Ngā kupu Māori Quest")
    root.geometry("390x844")

    # Big welcome title at the top
    tk.Label(
        root,
        text="Ngā kupu Māori Quest!",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    # Create the Leaderboard object - it builds its own frame on the left side
    leaderboard = Leaderboard(root)

    # Quiz button - creates a new QuizPage object when clicked
    tk.Button(
        root,
        text="Quiz",
        command=lambda: QuizPage(root, leaderboard),
        width=30,
        height=3
    ).pack(pady=20)

    # Opens a settings pop-up window
    def settings_page():
        settings_window = tk.Toplevel(root)
        settings_window.title("Settings")
        settings_window.geometry("390x844")
        tk.Label(
            settings_window,
            text="Settings - coming soon!",
            font=("Arial", 18)
        ).pack(pady=20)

    # Settings button placed in the bottom-right corner
    tk.Button(
        root,
        text="Settings",
        font=("Arial", 14),
        command=settings_page
    ).place(x=280, y=800)

    # Start the Tkinter event loop
    root.mainloop()


# Run the program
if __name__ == "__main__":
    home_page()