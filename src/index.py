from game import players
from game import bets
from game import cards
import system
import utils

def init ():
  system.print_greetings()

  players_names, players_tokens = players.register_players()

  print(utils.colored("§B§rPlacar Inicial§0\n"))
  system.print_stats(players_names, players_tokens)

  print(utils.colored("\n§B§rRODADA 1§0"))

  round_bets = bets.ask_bets(players_names, players_tokens)
  round_cards = cards.draw_cards(players_names)

  cards.print_cards(players_names, round_cards)

init()
