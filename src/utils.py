colors = {
  'r': "31",
  'g': "32",
  'b': "34",
  'c': "36",
  'y': "33",
  'm': "35",
  'w': "37",
  'k': "30",
  
  'br': "41",
  'bg': "42",
  'bb': "44",
  'bc': "46",
  'by': "43",
  'bm': "45",
  'bw': "47",
  'bk': "40",

  'B': "1",
  'R': "2",
  '0': "0;0",
}

def colored (text):
  for key in colors:
    find = "§" + key
    code = f"\033[{ colors[key] }m"

    text = text.replace(find, code)

  return text


def get_max_len (list):
  max_len = 0
  for item in list:
    max_len = max(max_len, len(str(item)))

  return max_len


def card_description (card):
  card_id, deck, suit, number, value = card

  suits_names = ["Paus", "Copas", "Espadas", "Ouros"]
  cards_names = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valete", "Rainha", "Rei"]

  description = f"{cards_names[number]} de {suits_names[suit]} do {deck + 1}º baralho ({value} pontos)"

  return description

def print_player_cards (playername, cards):
  score = 0

  print(colored(f"\n§BCartas de §y{playername}§0:"))

  for card in cards:
    print(f" - {card_description(card)}")

    score += card[4]
  
  print(colored(f"\n§g > {playername} marcou {score} pontos!§0"))


def print_cards (players, cards):
  playernames = players[::2]

  for i in range(0, len(playernames)):
    playername = playernames[i]
    player_cards = cards[i]

    print_player_cards(playername, player_cards)
