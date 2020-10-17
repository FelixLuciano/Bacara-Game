from . import tokens
from . import cards
import utils

taken_names = [ "", "não", "nao", "n", "banco" ]
exit_names = taken_names[0:4]

players = []


def get_players ():
  return players

def get_real_players ():
  return get_players()[:-1]

def get_players_info ():
  return zip(players, tokens.tokens, cards.cards)


def register_player (name, amount):
  players.append(name)
  tokens.tokens.append(amount)
  cards.cards.append([])

  if amount == "∞":
    amount = "infinitas"

  print(utils.colored(f"\n§g > {name} entrou no jogo com {amount} fichas!§0\n"))


def register_players ():
  index = 1

  while True:
    name = input(utils.colored(f"Jogador {index}, vai jogar? Qual seu nome? §y"))
    name_lower = name.lower()

    if not name_lower in taken_names:
      amount_input = input(utils.colored(f"§0Quantas fichas você tem, {name}? §y"))
      amount = 0

      if amount_input:
        int_amount = int(amount_input)
        
        if int_amount >= 0:
          amount = int_amount

        else:
          print(utils.colored("§0Não é possível entrar no jogo devendo!\n"))
          continue
          
      taken_names.append(name.lower())
      register_player(name, amount)

      index += 1

    elif name_lower in exit_names:
      print(utils.colored(f"§0Fim da entrada de jogadores."))

      break

    else:
      print(utils.colored(f"§0Não é possível usar esse nome!\n"))

  register_player("Banco", "∞")
