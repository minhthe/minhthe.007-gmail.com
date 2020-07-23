'''
https://www.pramp.com/challenge/BrLMj8M2dVUoY95A9x3X
'''
def calc_drone_min_energy(route):
  z = []
  for item in route:
    z.append(item[2])
  
  rst = int(1e9)
  
  first_v = 0
  for i in range(0, len(z) -1 ): # 1 2 3 4 5 6  
    tmp = z[i+1] - z[i]  
    if tmp < 0 :  # go down
      first_v += tmp*(-1) 
    else:  # go up
      first_v += tmp*(-1)
    if first_v < 0 :
      rst = min(rst, first_v)
  if rst < 0 : return rst*(-1)
  return 0
#route =  [ [0,   2, 10],  [3,   5,  0], [9,  20,  6],[10, 12, 15],[10, 10,  8] ]
route  = [[0,1,19]]
print(calc_drone_min_energy(route))
# 10 0 6 15 8
#  10(10) -6 (4) -9 (-5)
