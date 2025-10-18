import json
import os
from datetime import datetime


class HighScore:
    """
    Manages reading, updating, and displaying persistent high scores.
    Scores are stored in a JSON file so they remain after the game ends.
    """

    FILE_PATH = "high_scores.json"

    def __init__(self):
        # Load existing data or initialize an empty dictionary
        self.records = self._load_scores()

    def _load_scores(self):
        """Read the high score file if it exists, otherwise return an empty record."""
        if os.path.exists(self.FILE_PATH):
            try:
                with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                # If file is broken or unreadable, reset it
                return {}
        return {}

    def save_score(self, player_name, score):
        """
        Save a new high score if it's higher than the player's previous one.
        Supports both old (int) and new (dict) formats.
        """
        current_record = self.records.get(player_name, {"score": 0})

        # Handle backward compatibility: convert int → dict
        if isinstance(current_record, int):
            current_record = {"score": current_record}

        # Only save if new score is higher than old one
        if score > current_record.get("score", 0):
            self.records[player_name] = {
                "score": score,
                "achieved_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            self._save_to_file()

    def _save_to_file(self):
        """Write all scores to disk safely in a readable JSON format."""
        try:
            with open(self.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(self.records, file, indent=4)
        except IOError:
            print("⚠️ Could not save high scores to file.")

    def top_scores(self, limit=5):
        """Return the top N players sorted by score."""
        return sorted(
            self.records.items(),
            key=lambda item: item[1]["score"],
            reverse=True,
        )[:limit]

    def display(self):
        """Pretty-print the high score leaderboard."""
        print("\n🏅 HALL OF FAME – TOP PLAYERS 🏅")
        print("-" * 40)

        if not self.records:
            print("No high scores yet. Be the first to play!")
            return

        for rank, (player, info) in enumerate(self.top_scores(), start=1):
            print(f"{rank}. {player:<10} → {info['score']} pts ({info['achieved_on']})")

        print("-" * 40)
