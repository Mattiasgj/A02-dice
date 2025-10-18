import cmd
import random
from dice_game.game import Game
from dice_game.player import Player
from dice_game.high_score import HighScore  # ✅ import the HighScore class
from dice_game.intelligence import Intelligence
from dice_game.computer import Computer  # import this class at top

class PigShell(cmd.Cmd):
    intro = "Welcome to Dice Pig! Type 'help' or '?' to list commands.\n"
    prompt = "(pig) "

    def __init__(self):
        super().__init__()
        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.game = None
        self.hold = False
        self.high_scores = HighScore()  # ✅ Initialize high score manager

    def do_start(self, arg):
        """Start a new game. Usage: start"""
        print("Starting a new game of Dice Pig!")
        name1 = input("Enter Player 1 name: ")
        opponent_type = input("Play against 'computer' or 'friend'? ").lower()

        self.player1 = Player(name1)
        if opponent_type == "computer":
            self.player2 = Player("Computer")
            self.game = Game(self.player1, self.player2)
            self.current_player = self.player1

            # ✅ Create the AI brain and Computer controller
            ai = Intelligence(risk_factor=0.5)
            self.computer_controller = Computer(ai, self.game, self.player2, self.player1)
        else:
            name2 = input("Enter Player 2 name: ")
            self.player2 = Player(name2)
            self.game = Game(self.player1, self.player2)
            self.current_player = self.player1
            self.computer_controller = None 

        print(f"{self.current_player.get_name()} goes first!")

    def do_roll(self, arg):
        """Roll the dice for the current player."""
        if not self.game:
            print("Start a game first with 'start'.")
            return

        result = self.game.play_turn(self.current_player, self.hold)
        if result is False:
            print(f"Turn over! Unlucky, you rolled a 1!")
            self.current_player = self.game.switch_turns(self.current_player)
            print(f"Now it’s {self.current_player.get_name()}’s turn.")
            
             # ✅ If it's the computer's turn, let AI play automatically
            if self.current_player.get_name() == "Computer" and self.computer_controller:
                self.computer_controller.make_move()
                self.current_player = self.game.switch_turns(self.current_player)
        else:
            print(f"{self.current_player.get_name()} rolled a {result}! "
                f"Score: {self.current_player.get_score()}")

            # ✅ Check if player won
            if self.game.is_game_over(self.current_player.get_score()):
                print(f"🎉 {self.current_player.get_name()} wins with "
                      f"{self.current_player.get_score()} points!")

                # ✅ Save to high scores
                self.high_scores.save_score(
                    self.current_player.get_name(),
                    self.current_player.get_score()
                )
                print("🏆 High score saved!")
                self.high_scores.display()

                # Reset game
                self.game = None
                self.player1 = None
                self.player2 = None
                self.current_player = None

    def do_hold(self, arg):
        """Hold your current score and end your turn."""
        if not self.game:
            print("Start a game first with 'start'.")
            return

        self.hold = True

        # ✅ Actually apply the hold — update player’s score
        self.game.play_turn(self.current_player, self.hold)

        # ✅ Check for win before switching
        if self.game.is_game_over(self.current_player.get_score()):
            print(f"🎉 {self.current_player.get_name()} wins with "
                f"{self.current_player.get_score()} points!")
            self.high_scores.save_score(
                self.current_player.get_name(),
                self.current_player.get_score()
            )
            self.high_scores.display()
            self.game = None
            self.player1 = None
            self.player2 = None
            self.current_player = None
            return

        # Switch to next player after holding
        self.current_player = self.game.switch_turns(self.current_player)
        print(f"You held. Now it’s {self.current_player.get_name()}’s turn.")
        
        # ✅ Trigger computer move
        if self.current_player.get_name() == "Computer" and self.computer_controller:
            self.computer_controller.make_move()
            self.current_player = self.game.switch_turns(self.current_player)

        self.hold = False


    def do_score(self, arg):
        """Show both players' scores."""
        if not self.game:
            print("Start a game first with 'start'.")
            return
        print(f"{self.player1.get_name()}: {self.player1.get_score()} points")
        print(f"{self.player2.get_name()}: {self.player2.get_score()} points")

    def do_highscore(self, arg):
        """Show the top high scores. Usage: highscore"""
        print("\n📜 Displaying the top high scores:")
        self.high_scores.display()

    def do_change_name(self, arg):
        """Change the name of one or both players."""
        if not self.game:
            print("Start a game first with 'start'.")
            return

        if self.player2.get_name() == "Computer":
            name = str(input("Write your new name: "))
            self.player1.set_name(name)
        else:
            what_player = str(input("Which player wants to change their name (write name): "))

            if self.player1.get_name() == what_player:
                name = str(input("Write your new name: "))
                self.player1.set_name(name)
            elif self.player2.get_name() == what_player:
                name = str(input("Write your new name: "))
                self.player2.set_name(name)

    def do_cheat(self, arg):
        """Cheat the game."""
        cheat = str(input("Write the cheat code: "))
        if cheat == "1234":
            score = int(input("how many points do you want: "))
            self.player1.set_score(score)

    def do_quit(self, arg):
        """Quit the game."""
        print("Thanks for playing Dice Pig!")
        return True  # exits the cmd loop
