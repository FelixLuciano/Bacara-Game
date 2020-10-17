from game import players
from game import tokens
import utils

def print_greetings ():
  lines = [
    "§r",
    "▄▄▄▄·  ▄▄▄·  ▄▄·  ▄▄▄· ▄▄▄   ▄▄▄·",
    "▐█ ▀█▪▐█ ▀█ ▐█ ▌▪▐█ ▀█ ▀▄ █·▐█ ▀█ ",
    "▐█▀▀█▄▄█▀▀█ ██   ▄█▀▀█ ▐▀▀▄ ▄█▀▀█ ",
    "██▄▪▐█▐█ ▪▐▌▐█  █▐█ ▪▐▌▐█•█▌▐█ ▪▐▌",
    "·▀▀▀▀  ▀  ▀ ·▀▀▀  ▀  ▀ .▀  ▀ ▀  ▀ ",
    "",
    "§B§gSeja bem vindo(a) ao Bacará!§0",
    "Por Luciano Felix",
    "",
    "Insira as informações para começar...",
    ""
  ]

  print(utils.colored('\n'.join(lines)))

def print_stats ():
  header = ("NOME", "FICHAS")

  max_names_len = max(utils.get_max_len(players.get_players()), len(header[0]))
  max_tokens_len = max(utils.get_max_len(tokens.get_tokens()), len(header[1]))

  print(f"┌ {header[0]} { '─' * (max_names_len - 6 + 3) } {header[1]} { '─' * (max_tokens_len - 6) }┐")

  for player in players.get_players_info():
    name, player_tokens, cards = player

    name_length = len(name)
    name_spacer = " " * (max_names_len - name_length + 3)

    tokens_length = len(str(player_tokens))
    tokens_spacer = " " * (max_tokens_len - tokens_length)

    print(utils.colored(f"│ §y{name}{name_spacer}§g{player_tokens}{tokens_spacer} §0│"))

  print("└" + "─" * (max_names_len + 3 + max_tokens_len + 2) + "┘")
