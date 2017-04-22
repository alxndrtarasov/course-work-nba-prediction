from scraper import Scraper

stats_scraper = Scraper()
games = stats_scraper.get_games()
print games[0].home()
print games[0].away()
print stats_scraper.get_teams_rest(0)