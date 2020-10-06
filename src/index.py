from system import *
from game import *

def init ():
  print_greetings()
  register_players()
  if len(players):
    print_stats(players)

init()
