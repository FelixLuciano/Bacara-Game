from . import players
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

      if bet_bid <= 0 or bet_bid > player_tokens:
        print(utils.colored("§0Não é possível apostar essa quantia!"))

      else:
        return bet_bid
        break

    else:
      print(utils.colored("§0É necessário que seja dado um valor!"))
  

def ask_bets (playernames, tokens):
  playernames_tokens = list(zip(playernames, tokens))
  player_bets = []

  for playername_tokens in players.get_real_players(playernames_tokens):
    playername, tokens = playername_tokens

    player_bet = []

    while True:
      bet_what = input(utils.colored(f"§0Jogador, banco ou empate. Qual a sua aposta, {playername}? §b"))
      bet_what_lower = bet_what.lower()

      if bet_what_lower in ["jogador", "j"]:
        player_bet.append("p")

        while True:
          bet_who = input(utils.colored(f"§0Em qual jogador você aposta, {playername}? §y"))

          bet_player = players.get_playername(bet_who, playernames)

          if bet_player and bet_who.lower() !=  playername.lower():
            bet_bid = ask_bet_bid(f"§0quanto você aposta em {bet_player}, {playername}? §y", tokens)

            player_bet.append(bet_bid)
            player_bet.append(bet_player)
            print(utils.colored(f"\n§g > {playername} apostou {bet_bid} em {bet_player}!§0\n"))
            break

          else:
            print(utils.colored("§0Não é possível apostar nesse jogador!"))

        break

      elif bet_what_lower in ["banco", "b"]:
        bet_bid = ask_bet_bid(f"§0quanto você aposta no Banco, {playername}? §g", tokens)

        player_bet.append("b")
        player_bet.append(bet_bid)
        print(utils.colored(f"\n§g > {playername} apostou {bet_bid} no Banco!§0\n"))
        break

      elif bet_what_lower in ["empate", "e"]:
        bet_bid = ask_bet_bid(f"§0quanto você aposta por um empate no jogo, {playername}? §g", tokens)
        
        player_bet.append("t")
        player_bet.append(bet_bid)
        print(utils.colored(f"\n§g > {playername} apostou {bet_bid} por um empate no jogo!§0\n"))
        break

      else:
        print(utils.colored("§0Não é possível realizar esse tipo de aposta!"))

    player_bets.append(player_bet)

  return player_bets
