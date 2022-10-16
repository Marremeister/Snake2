from main import *


class Score_history:

    def __init__(self, game, player, player_score):
        self.game = game
        self.player = player
        self.player_score = player_score
        self.score_history = []
        self.score_history_append()
        self.find_top_score()

    def score_history_append(self):
        self.score_history.append([self.player, self.player_score])

    def find_top_score(self):
        for round in range(len(self.score_history)):
            if round == 0:
                self.top_score = self.score_history[round][1]
            else:
                if self.score_history[round][1] > self.top_score:
                    self.top_score = self.score_history[round][1]

    def draw_highscore(self):
        self.draw_text = Special_text(self.game, f"Highscore is {self.top_score[0]} with a score of {self.top_score[1]}", 1200, 300, "freesansbold.ttf", 16)
        self.draw_text.draw()





