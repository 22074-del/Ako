import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


class Quiz:

    def __init__(self, root, leaderboard):
        self.root = root
        self.leaderboard = leaderboard

        self.questions = [
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
        "prompt": "What does 'Kia ora' commonly mean?",
        "options": ["Goodbye", "Hello", "Please", "Sorry"],
        "answer": "Hello"
    },
    {
        "prompt": "What does 'Mana' most closely refer to?",
        "options": ["Prestige", "Water", "Food", "Clothing"],
        "answer": "Prestige"
    },
    {
        "prompt": "What does 'Kai' translate to?",
        "options": ["Food", "House", "Book", "Road"],
        "answer": "Food"
    },
    {
        "prompt": "What does 'Wai' translate to?",
        "options": ["Water", "Fire", "Wind", "Tree"],
        "answer": "Water"
    },
    {
        "prompt": "What does 'Tamariki' translate to?",
        "options": ["Parents", "Children", "Teachers", "Friends"],
        "answer": "Children"
    },
    {
        "prompt": "What does 'Kura' translate to?",
        "options": ["Hospital", "School", "Market", "Church"],
        "answer": "School"
    },
    {
        "prompt": "What does 'Waka' translate to?",
        "options": ["Boat/Canoe", "Mountain", "Food", "Bird"],
        "answer": "Boat/Canoe"
    },
    {
        "prompt": "What does 'Whare' translate to?",
        "options": ["House", "River", "Tree", "Road"],
        "answer": "House"
    },
    {
        "prompt": "What does 'Moana' translate to?",
        "options": ["Ocean", "Forest", "Mountain", "Valley"],
        "answer": "Ocean"
    },
    {
        "prompt": "What does 'Maunga' translate to?",
        "options": ["Lake", "Mountain", "Beach", "Cloud"],
        "answer": "Mountain"
    },
    {
        "prompt": "What does 'Awa' translate to?",
        "options": ["River", "Ocean", "Road", "Bridge"],
        "answer": "River"
    },
    {
        "prompt": "What does 'Rangi' translate to?",
        "options": ["Sky", "Earth", "Sea", "Tree"],
        "answer": "Sky"
    },
    {
        "prompt": "What does 'Whenua' translate to?",
        "options": ["Land", "House", "Food", "Water"],
        "answer": "Land"
    },
    {
        "prompt": "What does 'Hoa' translate to?",
        "options": ["Friend", "Enemy", "Teacher", "Parent"],
        "answer": "Friend"
    },
    {
        "prompt": "What does 'Hapū' translate to?",
        "options": ["Sub-tribe", "Mountain", "School", "River"],
        "answer": "Sub-tribe"
    },
    {
        "prompt": "What does 'Iwi' translate to?",
        "options": ["Tribe", "Food", "Family", "Village"],
        "answer": "Tribe"
    },
    {
        "prompt": "What does 'Kaumātua' translate to?",
        "options": ["Elder", "Child", "Warrior", "Teacher"],
        "answer": "Elder"
    },
    {
        "prompt": "What does 'Pukapuka' translate to?",
        "options": ["Book", "Chair", "Table", "Pen"],
        "answer": "Book"
    },
    {
        "prompt": "What does 'Kākahu' translate to?",
        "options": ["Clothing", "Food", "Water", "House"],
        "answer": "Clothing"
    },
    {
        "prompt": "What does 'Kurī' translate to?",
        "options": ["Dog", "Cat", "Horse", "Bird"],
        "answer": "Dog"
    },
    {
        "prompt": "What does 'Manu' translate to?",
        "options": ["Bird", "Fish", "Tree", "Mountain"],
        "answer": "Bird"
    },
    {
        "prompt": "What does 'Rākau' translate to?",
        "options": ["Tree", "River", "Cloud", "House"],
        "answer": "Tree"
    }
]

    def open(self):

        self.window = tk.Toplevel(self.root)

        self.current_question = 0
        self.score = 0

        self.player_name = simpledialog.askstring(
            "Name",
            "Enter your name:"
        )

        if not self.player_name:
            self.player_name = "Anonymous"

        self.create_widgets()

    def create_widgets(self):

        self.question_label = tk.Label(
            self.window,
            font=("Arial", 16)
        )

        self.question_label.pack()

        self.selected_answer = tk.StringVar()

        self.load_question()

    def load_question(self):
        pass

    def next_question(self):
        pass

    def show_results(self):

        self.leaderboard.add_score(
            self.player_name,
            self.score,
            len(self.questions)
        )