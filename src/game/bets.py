from . import players
import system
import utils

bets = []


def get_bets ():
  return bets

def get_players_bets ():
  return bets[:-1]


def ask_bet_bid (input_message, player_tokens):
  while True:
    bet_bid_input = input(utils.colored(input_message))

    if bet_bid_input:
      bet_bid = int(bet_bid_input)

      if bet_bid < 0 or bet_bid > player_tokens:
        utils.print_colored("§0Não é possível apostar essa quantia!")

      else:
        return bet_bid
        break

    else:
      return False
  

def get_betting_players (players_list, tokens, bets):
  betting_players = []
  betting_tokens = []
  betting_bet = []

  for i in range(0, len(players_list)):
    player_name = players_list[i]

    if bets[i] or player_name == "Banco":
      betting_players.append(player_name)
      betting_tokens.append(tokens[i])
      betting_bet.append(bets[i])

  return (betting_players, betting_tokens, betting_bet)


def ask_bets (players_names, players_tokens):
  players_names_tokens = list(zip(players_names, players_tokens))
  players_bets = []

  for player_name_tokens in players.get_real_players(players_names_tokens):
    playername, tokens = player_name_tokens

    player_bet = []

    bet_bid = ask_bet_bid(f"§0Quanto você aposta nesta rodada, {playername}? (Ou saia sem apostar) §g", tokens)

    if bet_bid:
      player_bet.append(bet_bid)

      while True:
        bet_what = input(utils.colored(f"§0Jogador, banco ou empate. Em que você aposta {bet_bid} fichas, {playername}? §b"))
        bet_what_lower = bet_what.lower()

        if bet_what_lower in ["jogador", "j"]:
          player_bet.append("p")

          while True:
            bet_who = input(utils.colored(f"§0Em qual jogador você aposta {bet_bid} fichas, {playername}? §y"))

            bet_player = players.get_playername(bet_who, players_names)

            if bet_player and bet_who.lower() != playername.lower():
              player_bet.append(bet_player)
              utils.print_success(f"{playername} apostou {bet_bid} fichas em {bet_player}!")
              break

            else:
              utils.print_colored("§0Não é possível apostar nesse jogador!")

          break

        elif bet_what_lower in ["banco", "b"]:
          player_bet.append("b")
          utils.print_success(f"{playername} apostou {bet_bid} fichas no Banco!")
          break

        elif bet_what_lower in ["empate", "e"]:
          player_bet.append("t")
          utils.print_success(f"{playername} apostou {bet_bid} fichas por um empate no jogo!")
          break

        else:
          utils.print_colored("§0Não é possível realizar esse tipo de aposta!")

    else:
      utils.print_info(f"{playername} saiu do jogo com {tokens} fichas!")

    players_bets.append(player_bet)

  # Bank bet
  players_bets.append([])

  # Update players, removing who didn't bet
  players_names, players_tokens, players_bets = get_betting_players(players_names, players_tokens, players_bets)

  if not players.has_players(players_names):
    system.game_over()

  return (players_names, players_tokens, players_bets)
