def insertion_sort(a):
	for i in range(1, len(a)):  # [7,2,4,1,5,3] -> [2,7,4,1,5,3]
		
		key = a[i]     # 2
		j = i - 1       # 0  
		while j >=0 and a[j] > key:
			a[j+1] = a[j] 
			j -= 1
		a[j+1] = key
	return a


if __name__ == "__main__":
	a = [7,2,4,1,5,3]
	print('before', a)
	a = insertion_sort(a)
	print('after', a)