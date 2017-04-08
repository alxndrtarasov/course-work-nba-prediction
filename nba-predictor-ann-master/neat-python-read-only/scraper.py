import stats
import csv
from stats import Game, Team

class Scraper:
    def get_games(self):
        with open('games.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			my_games=[]
			for row in reader:
				try:
					my_games.append(Game(row['Home/Neutral'], row['Visitor/Neutral'], int(row['PTSH']), int(row['PTSA'])))
				except ValueError:
					break
        return my_games

    def get_teams_shape(self, num_of_game):
        with open('games.csv') as csvfile:
			result = [0,0,0,0,0,0,0,0,0,0]
			reader = csv.DictReader(csvfile)
			i=1
			for row in reader:
				print 'i=',i
				if i == num_of_game:
					home_team = row['Home/Neutral']
					away_team = row['Visitor/Neutral']
					c=0
					j=1
					for jrow in reader:
						print 'j1=',j
						if(j==(i-1)):
							if jrow['Home/Neutral']==home_team:
								c=c+1
								result[c]=int(jrow['PTSH'])-int(jrow['PTSA'])
								i=i-1
							if jrow['Visitor/Neutral']==home_team:
								c=c+1
								result[c]=int(jrow['PTSA'])-int(jrow['PTSH'])
								i=i-1
							if c==5:
								print 'gonna break j1'
								break
							else:
								continue
						j=j+1
					j=1
					i=num_of_game
					for krow in reader:
						print 'j2=',j
						if(j==(i-1)):
							if krow['Home/Neutral']==home_team:
								c=c+1
								result[c]=int(krow['PTSH'])-int(krow['PTSA'])
								i=i-1
							if jrow['Visitor/Neutral']==home_team:
								c=c+1
								result[c]=int(krow['PTSA'])-int(krow['PTSH'])
								i=i-1
							if c==10:
								print 'gonna break j2'
								break
							else:
								continue
						j=j+1
					print 'gonna break all'
					break
				else:
					i=i+1
					continue
			return result
