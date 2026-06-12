# Import the tkinter library and rename it as "tk"
# tkinter is then used to create graphical user interfaces (GUIs)
import tkinter as tk
from tkinter import messagebox # Import messagebox so popup warning messages can be displayed

def open_quiz_page():     # Function that opens the quiz page when the Quiz button is clicked
    quiz_window = tk.Toplevel(root)     # Create a new window on top of the home page
    quiz_window.title("Quiz Page")      # Set the title shown at the top of the quiz window
    quiz_window.geometry("1920x1080")       # Set the size of the quiz window

    root.iconify()      # Minimise the home page while the quiz is being played

    # Helper function to bring back home screen and close quiz
    def close_quiz_and_restore_home():
        root.deiconify()       # Unminimizes/restores home page
        quiz_window.destroy()  # Closes quiz page

    # Bind the window close 'X' button to restore the home page
    quiz_window.protocol("WM_DELETE_WINDOW", close_quiz_and_restore_home)

    #Title label for the quiz page
    tk.Label(
        quiz_window,
        text="Welcome to the Quiz Page!",
        font=("Arial", 18)
    ).pack(pady=20)

    # 20 quiz questions with 4 options each and the correct answer given in the "answer" key
    quiz_questions = [
        {"prompt": "What does 'Mahi' translate to?", "options": ["Work", "Car", "Fish", "School"], "answer": "Work"},
        {"prompt": "What does 'Whānau' translate to?", "options": ["Clothing", "Bird", "Family", "Food"], "answer": "Family"},
        {"prompt": "What does 'Aroha' translate to?", "options": ["Love", "Hate", "Friendship", "Money"], "answer": "Love"},
        {"prompt": "What does 'Kia ora' commonly mean?", "options": ["Goodbye", "Hello", "Please", "Sorry"], "answer": "Hello"},
        {"prompt": "What does 'Mana' most closely refer to?", "options": ["Prestige", "Water", "Food", "Clothing"], "answer": "Prestige"},
        {"prompt": "What does 'Kai' translate to?", "options": ["Food", "House", "Book", "Road"], "answer": "Food"},
        {"prompt": "What does 'Wai' translate to?", "options": ["Water", "Fire", "Wind", "Tree"], "answer": "Water"},
        {"prompt": "What does 'Tamariki' translate to?", "options": ["Parents", "Children", "Teachers", "Friends"], "answer": "Children"},
        {"prompt": "What does 'Kura' translate to?", "options": ["Hospital", "School", "Market", "Church"], "answer": "School"},
        {"prompt": "What does 'Waka' translate to?", "options": ["Boat/Canoe", "Mountain", "Food", "Bird"], "answer": "Boat/Canoe"},
        {"prompt": "What does 'Whare' translate to?", "options": ["House", "River", "Tree", "Road"], "answer": "House"},
        {"prompt": "What does 'Moana' translate to?", "options": ["Ocean", "Forest", "Mountain", "Valley"], "answer": "Ocean"},
        {"prompt": "What does 'Maunga' translate to?", "options": ["Lake", "Mountain", "Beach", "Cloud"], "answer": "Mountain"},
        {"prompt": "What does 'Awa' translate to?", "options": ["River", "Ocean", "Road", "Bridge"], "answer": "River"},
        {"prompt": "What does 'Rangi' translate to?", "options": ["Sky", "Earth", "Sea", "Tree"], "answer": "Sky"},
        {"prompt": "What does 'Whenua' translate to?", "options": ["Land", "House", "Food", "Water"], "answer": "Land"},
        {"prompt": "What does 'Hoa' translate to?", "options": ["Friend", "Enemy", "Teacher", "Parent"], "answer": "Friend"},
        {"prompt": "What does 'Hapū' translate to?", "options": ["Sub-tribe", "Mountain", "School", "River"], "answer": "Sub-tribe"},
        {"prompt": "What does 'Iwi' translate to?", "options": ["Tribe", "Food", "Family", "Village"], "answer": "Tribe"},
        {"prompt": "What does 'Kaumātua' translate to?", "options": ["Elder", "Child", "Warrior", "Teacher"], "answer": "Elder"},
        {"prompt": "What does 'Pukapuka' translate to?", "options": ["Book", "Chair", "Table", "Pen"], "answer": "Book"},
        {"prompt": "What does 'Kākahu' translate to?", "options": ["Clothing", "Food", "Water", "House"], "answer": "Clothing"},
        {"prompt": "What does 'Kurī' translate to?", "options": ["Dog", "Cat", "Horse", "Bird"], "answer": "Dog"},
        {"prompt": "What does 'Manu' translate to?", "options": ["Bird", "Fish", "Tree", "Mountain"], "answer": "Bird"},
        {"prompt": "What does 'Rākau' translate to?", "options": ["Tree", "River", "Cloud", "House"], "answer": "Tree"}
    ]
    # Initialize the current question index and the user's score
    current_question = 0
    score = 0

    # Create a label to display the quiz question and set the font and size
    question_label = tk.Label(
        quiz_window,
        text="",
        font=("Arial", 16),
    )
    question_label.pack(pady=20)

    # No button selected by default
    selected_answer = tk.StringVar(value="NONE")

    # Create 4 radio buttons for the answer options and store them in a list for easy access
    option_buttons = []

    # Loop to create 4 radio buttons for the answer options, with the text and value set later when loading each question
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
        #Remove all option buttons from the screen and the next button as well since the quiz is over and they are no longer needed
        for button in option_buttons:
            button.destroy()

        next_button.destroy()

    	# Calculate the percentage score and round it to 2 dp
        percentage = round((score / len(quiz_questions)) * 100)

        #update the question label to show the final score and percentage as well as a message saying the quiz is complete
        question_label.config(
            text=(
                f"Quiz Complete!\n\n"
                f"Score: {score}/{len(quiz_questions)}\n"
                f"Percentage: {percentage}%"
            )
        )

        # Update the custom return button action
        return_button = tk.Button(
            quiz_window,
            text="Return to Home Page",
            font=("Arial", 14),
            width=20,
            command=close_quiz_and_restore_home  # Changed from quiz_window.destroy
        )
        return_button.pack(pady=20)

    # Function to handle the "Next Question" button and the making sure that if there is no answer given a warning pop-up is shown instead of moving to the next question
    def next_question():
        nonlocal current_question, score

        if selected_answer.get() == "NONE":
            messagebox.showwarning(
                "No Answer Selected",
                "Please choose an answer first."
            )
            return

    # Check if the selected answer is correct and update the score plus 1
        if selected_answer.get() == quiz_questions[current_question]["answer"]:
            score += 1

        current_question += 1

    # Check if there are more questions to load, if so load the next question, otherwise show the final results
        if current_question < len(quiz_questions):
            load_question()
        else:
            show_results()

    # Link the next question button to the next_question function
    next_button = tk.Button(
        quiz_window,
        text="Next Question",
        font=("Arial", 14),
        command=next_question
    )
    next_button.pack(pady=20)

    load_question()

    # Start the memory window's event loop
def open_memory_page():
    memory_window = tk.Toplevel(root)
    memory_window.title("Memory Page")
    memory_window.geometry("800x600")

    # Create a title inside the new memory pop-up window
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


import tkinter as tk

def home_page():
    # Make root global so other page functions can access it
    global root

    # Create the main program window
    root = tk.Tk()
    root.title("Ngā kupu Māori Quest")
    
    # Set the size of the main window to 1900 pixels wide by 1000 pixels high
    root.geometry("1900x1000")

    # Create the big welcome text at the top
    status = tk.Label(
        root,
        text="Welcome to Ngā kupu Māori Quest!",
        font=("Arial", 50, "bold")
    )
    # Put the text on the screen with 20 pixels of extra space above and below it
    status.pack(pady=20)

    # Create the Quiz menu button
    quiz_button = tk.Button(
        root,
        text="Quiz",
        command=open_quiz_page, # Runs the quiz page function when clicked
        width=50,               # Makes the button 50 text-characters wide
        height=5                # Makes the button 5 text-lines tall
    )
    # Stack the Quiz button below the title with 20 pixels of space
    quiz_button.pack(pady=20)

    # Create the Memory menu button
    game_button = tk.Button(
        root,
        text="Memory",
        command=open_memory_page, # Runs the memory page function when clicked
        width=50,
        height=5
    )
    # Stack the Memory button below the Quiz button
    game_button.pack(pady=20)

    # Create the Revision menu button
    revision_button = tk.Button(
        root,
        text="Revision",
        command=open_revision_page, # Runs the revision page function when clicked
        width=50,
        height=5
    )
    # Stack the Revision button below the Memory button
    revision_button.pack(pady=20)

    # Create the Challenge menu button
    challenge_button = tk.Button(
        root,
        text="Challenge",
        command=open_challenge_page, # Runs the challenge page function when clicked
        width=50,
        height=5
    )
    # Stack the Challenge button at the bottom of the main menu list
    challenge_button.pack(pady=20)

    # Define what happens when the settings button is clicked
    def settings_page():
        # Create a temporary pop-up window on top of the main root window
        settings_window = tk.Toplevel(root)
        settings_window.title("Settings Page")
        settings_window.geometry("800x600") # Set the pop-up size to 800x600

        # Create a title inside the new settings pop-up window
        tk.Label(
            settings_window,
            text="Settings page in progress",
            font=("Arial", 18)
        ).pack(pady=20) # Center the text inside the pop-up with spacing

    # Create the Settings button
    settingsbtn = tk.Button(
        root,                   # Put this button inside the main root window
        text="Settings",
        font=("Arial", 14),
        command=settings_page   # Links the button to run the settings_page function
    )
    # Force the Settings button to sit at the exact top-right corner coordinates
    settingsbtn.place(x=1750, y=60)
    
    # Start the Tkinter loop to keep the window open and listening for clicks
    root.mainloop()



if __name__ == "__main__":
    home_page()