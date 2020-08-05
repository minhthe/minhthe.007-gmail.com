'''
https://www.pramp.com/challenge/BrLMj8M2dVUoY95A9x3X
'''
def calc_drone_min_energy(route):
  return max(list(item[2] for item in route)) - route[0][2]