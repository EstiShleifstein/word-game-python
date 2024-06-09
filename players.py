class Player:

    def __init__(self):
        self.name = input("Welcome to the game! Please Enter Your Name to Start:\n")
        self.list_of_scores = []

    def __str__(self):
        return self.name

    def add_score_to_list(self, number):
        score = round(number, 2)
        self.list_of_scores.append(score)

    def get_highest_score(self):
        try:
            return max(self.list_of_scores)
        except ValueError:
            return "Oops! No scores yet."