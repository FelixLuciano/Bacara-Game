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

def colr (text):
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
