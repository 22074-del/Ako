import tkinter as tk


class Leaderboard:
    def __init__(self, parent):
        self.parent = parent
        self.scores = []

        self.frame = tk.Frame(
            parent,
            width=400,
            height=800,
            bg="lightgray"
        )
        self.frame.pack(side="left", fill="y")

        self.label = tk.Label(
            self.frame,
            text="🏆 Leaderboard\n\nNo scores yet",
            font=("Arial", 18),
            justify="left",
            bg="lightgray"
        )
        self.label.pack(pady=20)

    def add_score(self, name, score, total):
        self.scores.append({
            "name": name,
            "score": score,
            "total": total
        })

        self.update()

    def update(self):

        if not self.scores:
            self.label.config(
                text="🏆 Leaderboard\n\nNo scores yet"
            )
            return

        sorted_scores = sorted(
            self.scores,
            key=lambda x: x["score"],
            reverse=True
        )

        text = "🏆 Leaderboard\n\n"

        for position, player in enumerate(
            sorted_scores[:5],
            start=1
        ):
            percentage = round(
                player["score"] / player["total"] * 100
            )

            text += (
                f"{position}. "
                f"{player['name']} "
                f"({percentage}%)\n"
            )

        self.label.config(text=text)