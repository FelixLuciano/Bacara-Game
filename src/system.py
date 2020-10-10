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

def print_stats (players):
  playernames = players[::2]
  max_playername_len = max(utils.get_max_len(playernames), 4)

  scores = players[1::2]
  max_scores_len = max(utils.get_max_len(scores), 6)

  print(f"┌ NOME { '─' * (max_playername_len - 6 + 3) } FICHAS { '─' * (max_scores_len - 6) }┐")

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

  print("└" + "─" * (max_playername_len + 3 + max_scores_len + 2) + "┘")
