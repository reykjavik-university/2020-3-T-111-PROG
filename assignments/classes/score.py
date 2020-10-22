class Score():
    def __init__(self, score = 0):
        self.score = score
    
    def add(self, score):
        self.score += score
        
    def decrease(self, score):
        self.score -= score
            
    def __str__(self):
        return str(self.score)
        
        