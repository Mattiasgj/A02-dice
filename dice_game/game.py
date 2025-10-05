class Game:
    target_score = 100

    def __init__(self):
        pass

    def is_game_over(self, player1_score, player2_score):
        if player1_score >= self.target_score or player2_score >= self.target_score:
            return True