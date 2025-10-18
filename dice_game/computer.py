from dice_game.intelligence import Intelligence

class Computer:
    def __init__(self, intelligence, game, computer_player, human_player):
        self.intelligence = intelligence
        self.game = game
        self.computer_player = computer_player
        self.human_player = human_player

    def make_move(self):
        # The computer keeps rolling until it decides to hold
        while True:
            # Ask the AI whether to hold or roll
            should_hold = self.intelligence.decide(
                current_round_score=self.game.get_player_round_score(self.computer_player),
                total_score=self.computer_player.get_score(),
                opponent_score=self.human_player.get_score()
            )

            if should_hold:
                print("🤖 Computer decides to hold.")
                self.game.play_turn(self.computer_player, hold=True)
                break
            else:
                print("🤖 Computer rolls the dice...")
                result = self.game.play_turn(self.computer_player, hold=False)
                if result is False:
                    print("🤖 Computer rolled a 1! Turn over.")
                    break

                if self.game.is_game_over(self.computer_player.get_score()):
                    print(f"🎉 Computer wins with {self.computer_player.get_score()} points!")
                    break
