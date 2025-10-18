class Histogram:
    """
    Tracks and visualizes how often each dice face appears
    across all rolls in the game session.
    """

    def init(self):
        # Create a dictionary to count how often each face (1–6) appears.
        # Using dict comprehension makes it compact and efficient.
        self.roll_stats = {side: 0 for side in range(1, 7)}

    def update(self, rolled_values):
        """
        Update histogram counts based on the dice rolled in the last turn.
        Example: rolled_values = [3, 5, 3] → increments for 3 and 5
        """
        for face_value in rolled_values:
            if face_value in self.roll_stats:
                self.roll_stats[face_value] += 1

    def get_total_rolls(self):
        """Return total number of dice rolls recorded."""
        return sum(self.roll_stats.values())

    def display(self):
        """
        Display a text-based bar chart showing dice face frequency.
        Each '' represents one occurrence of that face value.
        """
        print("\n🎲 Dice Roll Frequency Histogram")
        print("-" 40)

        total = self.get_total_rolls()
        if total == 0:
            print("No rolls yet. Start playing to see statistics!")
            return

        for face, count in self.roll_stats.items():
            percentage = (count / total) * 100
            bar = "█" * count
            print(f"Face {face}: {bar:<20} ({count} rolls, {percentage:.1f}%)")

        print("-" * 40)
        print(f"Total rolls recorded: {total}")