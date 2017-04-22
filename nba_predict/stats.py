class Game:
    def __init__(self, team1, team2, score1, score2, when):
        self.home_name = team1
        self.away_name = team2
        self.diff = score1 - score2
        self.home_sc=score1
        self.away_sc=score2
        self.date = when

    def g_date(self):
        return self.date

    def home(self):
    	return self.home_name

    def away(self):
    	return self.away_name
    	
    def result(self):
    	return self.diff

    def home_score(self):
        return self.home_sc

    def away_score(self):
        return self.away_sc



class Team:
    def __init__(self, s):
        self.stats = s

    def team_stats(self):
        return self.stats
