def open_quiz_page():
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz Page")
    quiz_window.geometry("800x600")

    tk.Label(
        quiz_window,
        text="Welcome to the Quiz Page!",
        font=("Arial", 18)
    ).pack(pady=20)

    # Quiz questions
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

    selected_answer = tk.StringVar(value=None)  # Initialize with None to avoid pre-selection

    option_buttons = []

    # Create radio buttons for options
    for i in range(4):
        btn = tk.Radiobutton(
            quiz_window,
            text="",
            variable=selected_answer,
            font=("Arial", 14),
            value=None  # Set the initial value to None
        )
        btn.pack(anchor="w", padx=200, pady=5)
        option_buttons.append(btn)

    def load_question():
        selected_answer.set(None)  # Reset the selected answer to None
        question = quiz_questions[current_question]
        question_label.config(text=question["prompt"])

        for i, option in enumerate(question["options"]):
            option_buttons[i].config(
                text=option,
                value=option
            )

    def next_question():
        nonlocal current_question, score

        question = quiz_questions[current_question]

        if selected_answer.get() == question["answer"]:
            score += 1

        current_question += 1

        if current_question < len(quiz_questions):
            load_question()
        else:
            show_result()

    def show_result():
        for button in option_buttons:
            button.destroy()

        next_button.destroy()

        question_label.config(
            text=f"Quiz Finished!\nYour score: {score}/{len(quiz_questions)}"
        )

    next_button = tk.Button(
        quiz_window,
        text="Next Question",
        font=("Arial", 14),
        command=next_question
    )
    next_button.pack(pady=20)

    load_question()