class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def track_score(self, points):
        self.score = self.score + points
    
    def get_score(self):
        return self.score
