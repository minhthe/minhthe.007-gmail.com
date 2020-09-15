a= [2,9,4,7,1,8]
print(a)
def solve():
	
	for i in range(1, len(a)):
		pos = i -1
		current = a[i]
		while pos >=0 and current < a[pos]:
			a[pos+1] = a[pos]
			pos = pos - 1
		a[pos+1]	= current
		print('id', i , a)
	
	
solve()