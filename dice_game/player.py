class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def add_score(self, points):
        self.score = self.score + sum(points)
    
    def get_score(self):
        return self.score
    
    def set_score(self):
        self.score = 0

    def get_name(self):
        return self.name
