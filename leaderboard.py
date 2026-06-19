import tkinter as tk
    #Made a class a leader board to display the top scores and player names
class Leaderboard:
    def __init__(self, parent):     #defines the init method for the class, which initializes the leaderboard using a parent widget and sets up the needed attributes and UI elements.
        """
        Initialize the Leaderboard class.
        :param parent: The parent Tkinter widget (e.g., a frame or root window).
        """
        self.parent = parent        #Stores the reference to the parent widget
        self.leaderboard_data = []  # Stores the top quiz scores and player names

        # Create a frame for the leaderboard
        self.frame = tk.Frame(self.parent, width=400, height=800, bg="lightgray")
        self.frame.pack(side="left", fill="y")

        # Create a label to display the leaderboard
        self.label = tk.Label(
            self.frame,
            text="🏆 Scoreboard\n\nNo scores yet",
            font=("Arial", 18),
            justify="left",
            bg="lightgray"
        )
        self.label.pack(pady=20, padx=10)

        #Initialize the leaderboard display
    def add_score(self, name, score, total):
        """
        Add a player's score to the leaderboard.
        :param name: The player's name.
        :param score: The player's score.
        :param total: The total possible score.
        """
        self.leaderboard_data.append({"name": name, "score": score, "total": total})    #Adds a new score entry to the leaderboard data list, which is a dictionary containing the player's name, their score, and the total possible score.
        self.update_leaderboard()                                                       #After adding a new score, it calls the update_leaderboard to refresh the leaderboard display with the latest scores.

        #Updates the leaderboard display with the top scores, sorting them from highest to lowest and showing the top 5 scores along with the player's name, score, total possible score, and percentage.
    def update_leaderboard(self):
        """
        Update the leaderboard display with the top scores.
        """
        if not self.leaderboard_data:
            text = "🏆 Scoreboard\n\nNo scores yet"
        else:
            text = "🏆 Scoreboard\n\n"
            # Sort scores from highest to lowest
            sorted_scores = sorted(self.leaderboard_data, key=lambda x: x["score"], reverse=True)
            # Display the top 5 scores
            for position, player in enumerate(sorted_scores[:5], start=1):
                percentage = round((player["score"] / player["total"]) * 100)
                text += f"{position}. {player['name']} - {player['score']}/{player['total']} ({percentage}%)\n"

        self.label.config(text=text)