from dice_game.dice_hand import DiceHand

class Game:
    target_score = 20
    dice = DiceHand()

    def __init__(self):
        pass

    def play_turn(self, player, hold):
        if hold == False:
            score = self.dice.roll()
            if self.is_turn_over(score) == True:
                return False
            player.add_score(score)
            return score
        elif hold == True:
            return False
    
    def is_turn_over(self, score):
        if score == [1]:
            return True

    def is_game_over(self, player_score):
        if player_score >= self.target_score:
            return True