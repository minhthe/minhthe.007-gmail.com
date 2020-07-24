'''
https://www.pramp.com/challenge/BrLMj8M2dVUoY95A9x3X
'''
def calc_drone_min_energy(route):
  
  rst = 0 
  s = 0 
  for i in range(0, len(route) -1 ): # 1 2 3 4 5 6  
    s +=   (route[i][2]  - route[i+1][2]  )
    rst = min(rst, s)
  return rst * (-1