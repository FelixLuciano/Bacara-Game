tokens = []
# tokens = [100, 100, 999999, "∞"]


def get_tokens ():
  return tokens

def get_players_tokens ():
  return tokens[:-1]

def get_bank_tokens ():
  return tokens[-1]

def add_player_tokens (player_id, amount):
  tokens[player_id] += amount
