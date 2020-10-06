blacklist = ["", "não", "nao", "n"]

players = []

def print_greetings ():
  lines = [
    "\033[31m",
    "▄▄▄▄·  ▄▄▄·  ▄▄·  ▄▄▄· ▄▄▄   ▄▄▄·",
    "▐█ ▀█▪▐█ ▀█ ▐█ ▌▪▐█ ▀█ ▀▄ █·▐█ ▀█ ",
    "▐█▀▀█▄▄█▀▀█ ██   ▄█▀▀█ ▐▀▀▄ ▄█▀▀█ ",
    "██▄▪▐█▐█ ▪▐▌▐█  █▐█ ▪▐▌▐█•█▌▐█ ▪▐▌",
    "·▀▀▀▀  ▀  ▀ ·▀▀▀  ▀  ▀ .▀  ▀ ▀  ▀ ",
    "\033[0;0m",
    "\033[1mSeja bem vindo(a) ao Bacará!\033[0;0m",
    "Por Luciano Felix",
    "",
    "Insira as informações para começar...",
    "\033[0;0m"
  ]

  print('\n'.join(lines))

def register_player (name, amount):
  players.append(name)
  players.append(amount)

  print(f"\n\033[32m > {name} entrou no jogo com {amount} fichas!\033[0;0m\n")

def register_players ():
  index = 1

  while True:
    name = input(f"Jogador {index}, vai jogar? Qual seu nome? \033[33m")

    if not name in blacklist:
      amount_input = input(f"\033[0;0mQuantas fichas você tem, {name}? \033[33m")
      amount = 0

      if amount_input:
        int_amount = int(amount_input)
        
        if int_amount > 0:
          amount = int_amount
          
      register_player(name, amount)
      index += 1

    else:
      print(f"\033[0;0mJogador {index} não registrado.")
      break

def get_max_len (list):
  max_len = 0
  for item in list:
    max_len = max(max_len, len(str(item)))

  return max_len

def print_stats ():
  playernames = players[::2]
  max_playername_len = max(get_max_len(playernames), 4)

  scores = players[1::2]
  max_scores_len = max(get_max_len(scores), 6)

  divider = "─" * (max_playername_len + 3 + max_scores_len + 2)

  # print("┌" + divider + "┐")

  print(f"┌ NOME { '─' * (max_playername_len - 6 + 3) } FICHAS{ '─' * (max_scores_len - 8) } ┐")

  i = 0
  while i < len(players):
    name = players[i]
    score = players[i + 1]

    playername_length = len(name)
    playername_spacer = " " * (max_playername_len - playername_length + 3)

    score_length = len(str(score))
    score_spacer = " " * (max_scores_len - score_length)

    print(f"│ {name}{playername_spacer}{score}{score_spacer} │")

    i += 2

  print("└" + divider + "┘")

def init ():
  print_greetings()
  register_players()
  if len(players):
    print_stats()

init()
