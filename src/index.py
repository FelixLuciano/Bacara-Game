from game import players
from game import cards
import system
import utils

def init ():
  system.print_greetings()

  players.register_players()

  if len(players.get_real_players()):
    print(utils.colored("§B§rPlacar Inicial§0\n"))
    system.print_stats()
    print("")

    print(utils.colored("§B§rRODADA 1§0"))
    round_cards = cards.draw_cards()
    cards.print_cards()

init()
