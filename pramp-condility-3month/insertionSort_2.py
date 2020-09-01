if __name__ == '__main__':
	a = [3,8,2,4,7,90,34,456]
	def insertionSort(a):
		
		for i in range(1,len(a)):
			current = a[i]
			j =  i 
			while(j>0 and  a[j-1] > a[j] ):
				a[j-1],a[j] = a[j], a[j-1]
				j = j - 1
			a[j] = current
		return a 
	
	insertionSort(a)
	print(a)
	