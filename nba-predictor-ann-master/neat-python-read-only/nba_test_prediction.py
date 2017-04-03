import random
import cPickle as pickle
import math

from scraper import Scraper

from neat.nn import nn_pure as nn

stats_scraper = Scraper()
games = stats_scraper.retrieve_games()
teams = stats_scraper.retrieve_teams()

file = open("winner_chromosome")
chromo = pickle.load(file)
best_net = nn.create_ffphenotype(chromo)
file.close()

j=0
s=0
for i in range((len(games)-50)):
	j=j+1
	print j
	game = games[i]
	home_team = game.home()
	away_team = game.away()
	inputs = []
	home_stats = teams[home_team].team_stats()
	away_stats = teams[away_team].team_stats()
	for i in range(0, len(home_stats)):
		inputs.append(home_stats[i]-away_stats[i])
	outcome_prediction = best_net.sactivate(inputs)[0]
	mov = best_net.sactivate(inputs)[1]
	print "Probability home team wins: " + str(outcome_prediction)
	print "Margin of victory: " + str(mov)
	if(outcome_prediction>float(0.5)):
		if(game.result() > 0):
			print "SUCCESS"
			s=s+1
		if(game.result() < 0):
			print "FAIL"
	else:
		if(game.result() < 0):
			print "SUCCESS"
			s=s+1
		if(game.result() > 0):
			print "FAIL"
	print str(math.fabs(game.result()/float(100)-mov))
print "successful predicted:"+str(s)+" out of "+str(len(games))



