import utils
import sys

game_names = [ "", "não", "nao", "n", "banco" ]
exit_names = game_names[0:4]


def get_real_players (players_list):
  return players_list[:-1]

def has_players (players_list):
  return bool(get_real_players(players_list))

def get_playername (name, player_list):
  for playername in player_list:
    if name.lower() == playername.lower():
      return playername

  return false


def register_players ():
  players = []
  tokens = []

  taken_names = game_names

  index = 1
  while True:
    name = input(utils.colored(f"Jogador {index}, vai jogar? Qual seu nome? §y"))
    name_lower = name.lower()

    if not name_lower in taken_names:
      tokens_input = input(utils.colored(f"§0Quantas fichas você tem, {name}? §g"))
      tokens_amount = 0

      if tokens_input:
        int_tokens = int(tokens_input)
        
        if int_tokens > 0:
          tokens_amount = int_tokens

        else:
          print(utils.colored("§0Não é possível entrar no jogo sem fichas!\n"))
          continue
          
      taken_names.append(name_lower)
      players.append(name)
      tokens.append(tokens_amount)

      print(utils.colored(f"\n§g > {name} entrou no jogo com {tokens_amount} fichas!§0\n"))

      index += 1

    elif name_lower in exit_names:
      print(utils.colored(f"§0Fim da entrada de jogadores."))

      break

    else:
      print(utils.colored(f"§0Não é possível usar esse nome!\n"))

  if has_players(players):
    players.append("Banco")
    tokens.append("∞")

    print(utils.colored(f"\n§g > Banco entrou no jogo com infinitas fichas!§0\n"))

  else:
    print(utils.colored("\n§B§rFim de jogo!§0"))
    sys.exit()

  return (players, tokens)
