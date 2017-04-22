
import stats
import csv
from stats import Game, Team
import datetime

class Scraper:
    def get_teams_dict(self):
        with open('teams_2015.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            team_names=[]
            for row in reader:
                try:
                    team_names.append(row["Team"].replace("*",""))
                except ValueError:
                    break
            team_names.append('Charlotte Bobcats')
            team_names.append('New Jersey Nets')
            team_names.append('New Orleans Hornets')
            teams_dictionary = dict.fromkeys(team_names)
            for team_name in teams_dictionary.keys():
                teams_dictionary.__setitem__(team_name, [0,0])
        return teams_dictionary

    def get_games(self):
        format = "%a %b %d %Y"
        with open('games13.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            my_games = []
            for row in reader:
                try:
                    my_games.append(
                        Game(row['Home/Neutral'], row['Visitor/Neutral'], int(row['PTSH']), int(row['PTSA']), datetime.datetime.strptime(row['Date'], format)))
                except ValueError:
                    break
        return my_games

    def get_teams_rest(self, num_of_game):
        games = self.get_games()
        result = []
        for i in range(len(games)):
            # print 'i=', i
            if i == num_of_game:
                home_team = games[i].home()
                away_team = games[i].away()
                c=0
                # print away_team, ' ', home_team
                for j in range(i - 1, 0, -1):
                    # print 'j1=', j
                    cur_game = games[j]
                    if cur_game.home() == home_team:
                        c = c + 1
                        result.append((games[i].g_date()-cur_game.g_date()).days)
                    if cur_game.away() == home_team:
                        c = c + 1
                        result.append((games[i].g_date() - cur_game.g_date()).days)
                    if c == 1:
                        # print 'gonna break j1'
                        break
                    else:
                        continue
                for k in range(i - 1, 0, -1):
                    # print 'j2=', k
                    cur_game = games[k]
                    if cur_game.home() == away_team:
                        c = c + 1
                        result.append((games[i].g_date() - cur_game.g_date()).days)
                    if cur_game.away() == away_team:
                        c = c + 1
                        result.append((games[i].g_date() - cur_game.g_date()).days)
                    if c == 2:
                        # print 'gonna break j2'
                        break
                    else:
                        continue
                break
        # print 'rest done with ', num_of_game
        return result

    def get_teams_shape(self, num_of_game):
        games = self.get_games()
        result = []
        for i in range(len(games)):
            #print 'i=', i
            if i == num_of_game:
                home_team = games[i].home()
                away_team = games[i].away()
                #print away_team, ' ', home_team
                c=0
                for j in range(i - 1, 0, -1):
                    #print 'j1=', j
                    cur_game=games[j]
                    if cur_game.home() == home_team:
                        c = c + 1
                        result.append(cur_game.home_score()-cur_game.away_score())
                    if cur_game.away() == home_team:
                        c = c + 1
                        result.append(cur_game.away_score() - cur_game.home_score())
                    if c == 5:
                        #print 'gonna break j1'
                        break
                    else:
                        continue
                for k in range(i - 1, 0, -1):
                    #print 'j2=', k
                    cur_game=games[k]
                    if cur_game.home() == away_team:
                        c = c + 1
                        result.append(cur_game.home_score() - cur_game.away_score())
                    if cur_game.away() == away_team:
                        c = c + 1
                        result.append(cur_game.away_score()-cur_game.home_score())
                    if c == 10:
                        #print 'gonna break j2'
                        break
                    else:
                        continue
                break
        print 'done with ',num_of_game
        return result
