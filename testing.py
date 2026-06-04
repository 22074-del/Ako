import tkinter as tk
from tkinter import messagebox


def open_quiz_page():
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz Page")
    quiz_window.geometry("800x600")

    tk.Label(
        quiz_window,
        text="Welcome to the Quiz Page!",
        font=("Arial", 18)
    ).pack(pady=20)

    quiz_questions = [
        {
            "prompt": "What does 'Mahi' translate to?",
            "options": ["Work", "Car", "Fish", "School"],
            "answer": "Work"
        },
        {
            "prompt": "What does 'Whānau' translate to?",
            "options": ["Clothing", "Bird", "Family", "Food"],
            "answer": "Family"
        },
        {
            "prompt": "What does 'Aroha' translate to?",
            "options": ["Love", "Hate", "Friendship", "Money"],
            "answer": "Love"
        },
        {
            "prompt": "What does 'Kia ora' translate to?",
            "options": ["Goodbye", "Hello", "Thank you", "Please"],
            "answer": "Hello"
        },
        {
            "prompt": "What does 'Mana' translate to?",
            "options": ["Prestige", "Water", "Food", "Clothing"],
            "answer": "Prestige"
        }
    ]

    current_question = 0
    score = 0

    question_label = tk.Label(
        quiz_window,
        text="",
        font=("Arial", 16),
        wraplength=600
    )
    question_label.pack(pady=20)

    # No button selected by default
    selected_answer = tk.StringVar(value="NONE")

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
        for button in option_buttons:
            button.destroy()

        next_button.destroy()

        percentage = round((score / len(quiz_questions)) * 100)

        question_label.config(
            text=(
                f"Quiz Complete!\n\n"
                f"Score: {score}/{len(quiz_questions)}\n"
                f"Percentage: {percentage}%"
            )
        )

        return_button = tk.Button(
            quiz_window,
            text="Return to Home Page",
            font=("Arial", 14),
            width=20,
            command=quiz_window.destroy
        )
        return_button.pack(pady=20)

    def next_question():
        nonlocal current_question, score

        if selected_answer.get() == "NONE":
            messagebox.showwarning(
                "No Answer Selected",
                "Please choose an answer first."
            )
            return

        if selected_answer.get() == quiz_questions[current_question]["answer"]:
            score += 1

        current_question += 1

        if current_question < len(quiz_questions):
            load_question()
        else:
            show_results()

    next_button = tk.Button(
        quiz_window,
        text="Next Question",
        font=("Arial", 14),
        command=next_question
    )
    next_button.pack(pady=20)

    load_question()


def open_memory_page():
    memory_window = tk.Toplevel(root)
    memory_window.title("Memory Page")
    memory_window.geometry("800x600")

    tk.Label(
        memory_window,
        text="Welcome to the Memory Page!",
        font=("Arial", 18)
    ).pack(pady=20)


def open_revision_page():
    revision_window = tk.Toplevel(root)
    revision_window.title("Revision Page")
    revision_window.geometry("800x600")

    tk.Label(
        revision_window,
        text="Welcome to the Revision Page!",
        font=("Arial", 18)
    ).pack(pady=20)


def open_challenge_page():
    challenge_window = tk.Toplevel(root)
    challenge_window.title("Challenge Page")
    challenge_window.geometry("800x600")

    tk.Label(
        challenge_window,
        text="Welcome to the Challenge Page!",
        font=("Arial", 18)
    ).pack(pady=20)


def home_page():
    global root

    root = tk.Tk()
    root.title("Kupu Quest")
    root.geometry("1900x1000")

    title_label = tk.Label(
        root,
        text="Welcome to Kupu Quest!",
        font=("Arial", 50, "bold")
    )
    title_label.pack(pady=20)

    quiz_button = tk.Button(
        root,
        text="Quiz",
        command=open_quiz_page,
        width=50,
        height=5
    )
    quiz_button.pack(pady=20)

    memory_button = tk.Button(
        root,
        text="Memory",
        command=open_memory_page,
        width=50,
        height=5
    )
    memory_button.pack(pady=20)

    revision_button = tk.Button(
        root,
        text="Revision",
        command=open_revision_page,
        width=50,
        height=5
    )
    revision_button.pack(pady=20)

    challenge_button = tk.Button(
        root,
        text="Challenge",
        command=open_challenge_page,
        width=50,
        height=5
    )
    challenge_button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    home_page()