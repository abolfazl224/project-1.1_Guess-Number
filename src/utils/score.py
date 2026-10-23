class score:
    def __init__(self, score):
        self.score = score

    def decrease_score(self):
        self.score = self.score - 10

    def result(self):
        return f'the score is {self.score}' 