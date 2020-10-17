from . import players
from utils import colored
from random import randint


cards = []

def get_cards ():
  return cards

def get_players_cards ():
  return cards[:-1]

def get_bank_cards ():
  return cards[-1]

def set_cards (new_cards):
  for i in range(0, len(new_cards)):
    player_cards = new_cards[i]
    cards[i] = player_cards


suits_names = ["Paus", "Copas", "Espadas", "Ouros"]
deck_suits = len(suits_names)

cards_names = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Rainha", "Rei"]
suit_values = len(cards_names)

deck_amount = 4

deck_size = suit_values * deck_suits
card_amount = deck_size * deck_amount


def get_random_card ():
  card_id = randint(0, card_amount - 1)

  return card_id


def get_card_info (card_id):
  deck = int(card_id / deck_size)
  suit = int((card_id - deck * deck_size) / suit_values)
  number = card_id % suit_values
  value = number + 1

  if value >= 10:
    value = 0

  return (card_id, deck, suit, number, value)


def get_new_random_card (cards_list):
  players_cards = [ card for player_cards in cards_list for card in player_cards ]

  while True:
    new_card = get_random_card()

    if not new_card in players_cards:
      break

  return new_card


def sum_cards_values (cards):
  sum = 0

  for card in cards:
    card_value = get_card_info(card)[4]
    sum += card_value

  return sum


def draw_cards ():
  players_cards = []

  # Draw 2 cards
  for player in players.get_players():
    player_cards = []

    while len(player_cards) < 2:
      card = get_new_random_card(players_cards)

      player_cards.append(card)

    players_cards.append(player_cards)

  # Draw 3dr card
  for i in range(0, len(players_cards)):
    player_cards = players_cards[i]
    value_sum = sum_cards_values(player_cards)

    if value_sum <= 5:
      card = get_new_random_card(players_cards)

      players_cards[i].append(card)

  set_cards(players_cards)


def card_description (card_info):
  card_id, deck, suit, number, value = card_info

  description = f"{cards_names[number]} de {suits_names[suit]}"

  if deck_amount > 1:
    description += f" do {deck + 1}º baralho"

  description += f" ({value} pontos)"

  return description

def print_player_cards (playername, cards):
  player_tokens = 0

  print(colored(f"\n§BCartas de §y{playername}§0:"))

  for card in cards:
    card_info = get_card_info(card)
    card_id, deck, suit, number, value = card_info
    
    player_tokens += value

    print(f" - {card_description(card_info)}")
  
  print(colored(f"\n§g > {playername} marcou {player_tokens} pontos!§0"))


def print_cards ():
  for player_info in players.get_players_info():
    playername, player_tokens, cards = player_info

    print_player_cards(playername, cards)
