import random
import utils

taken_names = [ "", "não", "nao", "n", "banco" ]
exit_names = taken_names[0:4]

players = []

deck_amount = 1
deck_suits = 4
suit_values = 13
deck_size = suit_values * deck_suits
card_amount = deck_size * deck_amount


def register_player (name, amount):
  players.append(name)
  players.append(amount)

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


def sum_cards (cards):
  sum = 0

  for card in cards:
    card_value = card[4]
    sum += card_value

  return sum


def get_card ():
  card_id = random.randint(0, card_amount)

  deck = int(card_id / deck_size)
  suit = int((card_id - deck * deck_size) / suit_values)
  number = card_id % suit_values
  value = number + 1

  if value >= 10:
    value = 0

  return (card_id, deck, suit, number, value)


def get_new_card (cards_list):
  cards = []

  for player_cards in cards_list:
    for card in player_cards:
      cards.append(card)

  while True:
    new_card = get_card()

    if not new_card in cards:
      break

  return new_card


def draw_cards ():
  playernames = players[::2]
  cards = []

  while len(cards) < len(playernames):
    player_cards = []
    cards_sum = 0

    while len(player_cards) < 2 or cards_sum <= 5 and len(player_cards) < 3:
      card = get_new_card(cards)

      card_value = card[4]
      cards_sum += card_value

      player_cards.append(card)

    cards.append(player_cards)

  return cards
