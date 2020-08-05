'''
https://www.pramp.com/challenge/BrLMj8M2dVUoY95A9x3X
'''
def calc_drone_min_energy(route):
	rst = 0
	s = 0 
	for i in range(len(route) - 1):
		if route[i][2] < route[i+1][2] :
			s -= abs(route[i][2] - route[i+1][2])
		
		else:
			s += abs(route[i][2] - route[i+1][2])
		rst = min(rst, s)
	return rst*(-1)

route = [[0,2,10],[10,10,8]]
print( calc_drone_min_energy(route)	)