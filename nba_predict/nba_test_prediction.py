import random
import cPickle as pickle
import math

from scraper import Scraper
from neat import visualize
from neat.nn import nn_pure as nn

stats_scraper = Scraper()
games = stats_scraper.get_games()

file = open("winner_chromosome")
chromo = pickle.load(file)
best_net = nn.create_ffphenotype(chromo)
file.close()
visualize.draw_net(chromo)
print '\nBest network output:'
brain = nn.create_ffphenotype(chromo)
print brain.neurons
print brain.synapses

file = open("shapes")
shapes = pickle.load(file)
file.close()

j = 0
s = float(0)
tp = float(0)
fp = float(0)
fn = float(0)
hw = float(0)
rhw = float(0)
pred_start = 100
for i in range(pred_start, len(games)):
    j = j + 1
    print j
    game = games[i]
    home_team = game.home()
    print home_team
    away_team = game.away()
    print away_team
    inputs = shapes[i]
    outcome_prediction = best_net.sactivate(inputs)[0]
    mov = float(best_net.sactivate(inputs)[0])
    total_err = 0
    print "Probability home team wins: " + str(outcome_prediction)
    print "Margin of victory: ", mov
    if (mov > float(0)):
        if (game.result() > 0):
            print "SUCCESS"
            s = s + 1
            tp = tp + 1
            rhw=rhw+1
        if (game.result() < 0):
            fp = fp + 1
            print "FAIL"
        hw=hw+1
    else:
        if (game.result() < 0):
            print "SUCCESS"
            s = s + 1
        if (game.result() > 0):
            fn = fn + 1
            rhw=rhw+1
            print "FAIL"
spred = float(s/(len(games) - pred_start))
print "successful predicted:", spred
print tp,fp,fn
P=float(tp/(tp+fp))
R=float(tp/(tp+fn))
F=2*P*R/(P+R)
print 'precision = ',P
print 'recall = ',R
print 'F-measure = ', F
print 'Home win predicted ',float(hw/(len(games) - pred_start))
print 'Real home wins ', float(rhw/(len(games) - pred_start))