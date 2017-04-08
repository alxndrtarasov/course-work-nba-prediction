import csv
import scraper
import cPickle as pickle
from scraper import Scraper

stats_scraper = Scraper()
games = stats_scraper.get_games()
i=0
shapes=[]
for game in games:
    if i >=100:
        shape=stats_scraper.get_teams_shape(i)
        shapes.append(shape)
    else:
        shapes.append([0,0,0,0,0,0,0,0,0,0])
    i=i+1
file = open('shapes', 'w')
pickle.dump(shapes, file)
file.close()



