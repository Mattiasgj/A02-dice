from dice_game.dice import Dice

class Game:
    target_score = 20
    dice = Dice(6)

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn_points = 0

    def switch_turns(self, current_player):
        if current_player == self.player_1:
            return self.player_2
        elif current_player == self.player_2:
            return self.player_1

    def play_turn(self, player, hold):
        if not hold:
            score = self.dice.roll()
            if self.is_turn_over(score, player):
                self.update_turn_points(score)
                return False  # turn ends on a 1

            turn_points = self.update_turn_points(score)
            print(turn_points)
            return score

        else:  # hold == True
            player.add_score(self.turn_points)
            self.turn_points = 0  # reset turn points after holding
            return False

    
    def is_turn_over(self, score, player):
        if score == 1:
            return True

    def is_game_over(self, player_score):
        if player_score >= self.target_score:
            return True
    
    def update_turn_points(self, score):
        if score == 1:
            self.turn_points = 0  
        else:
            self.turn_points += score  
        return self.turn_points
    
    def update_player_score(self, current_player, score):
        current_player.add_score(score)
    
    def get_player_round_score(self, current_player):
        return self.turn_points