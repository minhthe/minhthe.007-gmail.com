'''https://www.pramp.com/challenge/15oxrQx6LjtQj9JK9XlA'''
import bisect
def find_duplicates(arr1, arr2):
	rst = []
	for item in arr1:
		pos = bisect.bisect_left(arr2, item)
		if pos < len(arr2) and arr2[pos] == item: rst.append(item)
	return rst
a,b = [1,2,3,4],[3,4,5]
print(find_duplicates(a,b))