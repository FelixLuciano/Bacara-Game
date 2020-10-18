from game import players
from game import bets
from game import cards
import system
import utils

def init ():
  system.print_greetings()

  players_names, players_tokens = players.register_players()

  utils.print_colored("§B§rPlacar Inicial§0\n")
  system.print_stats(players_names, players_tokens)

  round = 1
  while True:
    utils.print_colored(f"\n§B§rRODADA {round}§0\n")

    players_names, players_tokens, round_bets = bets.ask_bets(players_names, players_tokens)

    utils.print_colored("§B§rDANDO AS CARTAS...§0")

    round_cards = cards.draw_cards(players_names)

    cards.print_cards(players_names, round_cards)

    round += 1

init()
