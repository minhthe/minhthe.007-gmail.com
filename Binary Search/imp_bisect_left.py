if __name__ == '__main__':

	
	a = [2, 5, 6, 13, 14, 25, 33 ,33,33,33,33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97]
	n = len(a)
	x = 33
	def f(a,x, l, r):
		pos = r
		while(l<r):
			mid = int( (r-l)/2 + l   )
			if(a[mid] >= x):
				pos =  mid 
				r = mid
			else:
				l = mid + 1 
		return pos
	print(f(a,x,0,n -1))