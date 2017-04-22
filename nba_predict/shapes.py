import csv
import scraper
import cPickle as pickle
from scraper import Scraper
import copy
from copy import deepcopy

stats_scraper = Scraper()
games = stats_scraper.get_games()
teams_dictionary = stats_scraper.get_teams_dict()
i = 0
shapes = []
tables = []
rests = []
# print teams_dictionary
for game in games:
    teams_dictionary.__setitem__(game.home(), [teams_dictionary.__getitem__(game.home())[0] + (game.result() > 0),
                                               teams_dictionary.__getitem__(game.home())[1] + (game.result() < 0)])
    teams_dictionary.__setitem__(game.away(), [teams_dictionary.__getitem__(game.away())[0] + (game.result() < 0),
                                               teams_dictionary.__getitem__(game.away())[1] + (game.result() > 0)])
    tables.append(deepcopy(teams_dictionary))
    if i >= 100:
        shape = stats_scraper.get_teams_shape(i)
        shapes.append(shape)
        rest = stats_scraper.get_teams_rest(i)
        rests.append(rest)
    else:
        rests.append([0,0])
        shapes.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    i = i + 1
file = open('shapes', 'w')
pickle.dump(shapes, file)
file.close()
file = open('tables', 'w')
pickle.dump(tables, file)
file.close()
file = open('rests', 'w')
pickle.dump(rests, file)
file.close()
print "saved"
#print tables
#print rests
