import utils

blacklist = [ "", "não", "nao", "n" ]

players = []


def register_player (name, amount):
  players.append(name)
  players.append(amount)

  print(utils.colored(f"\n§g > {name} entrou no jogo com {amount} fichas!§0\n"))

def register_players ():
  index = 1

  while True:
    name = input(utils.colored(f"Jogador {index}, vai jogar? Qual seu nome? §y"))

    if not name in blacklist:
      amount_input = input(utils.colored(f"§0Quantas fichas você tem, {name}? §y"))
      amount = 0

      if amount_input:
        int_amount = int(amount_input)
        
        if int_amount > 0:
          amount = int_amount
          
      register_player(name, amount)
      index += 1

    else:
      print(utils.colored(f"§0mJogador {index} não registrado.\n"))
      break
