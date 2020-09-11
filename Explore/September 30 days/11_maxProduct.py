class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		repo = []
		tmp = []
		if len(nums)== 1: return nums[0]
		rst = nums[0]
		for item in nums:
		 
			if item != 0:
				tmp.append(item)
			else:
				if item == 0 :rst = 0 
				repo.append(tmp)
				tmp = []
		repo.append(tmp)
		def f(arr):
			ans = 0
			# print('df',arr)
			cnt_negative = 0
			pig = 1
			for item in arr:
				if item < 0: cnt_negative+=1
				pig *= item	
		#	print(cnt_negative)
			if cnt_negative &  1 :
				if len(arr) == 1: return arr[0]
				left, right = 1 , 1 
				## the left part
				i, j = 1 , 0   # -2 -3 5  -5
				while i < cnt_negative:
					left *= arr[j]
					if arr[j] <0 : i+=1 
					j+=1
				while arr[j] > 0:
					left *= arr[j]
					j += 1 
				
			
			
				
				## the RIGHT part [-2, -2, 1, -2]
				i, j = 1 , 0   # -2 -3 5  -5
				arr = arr[::-1]
				# print(arr)
				while i < cnt_negative:
					# print(i,j)
					right *= arr[j]
					if arr[j] < 0 : i+=1
					j+=1
					 
				while arr[j] > 0:
					right *= arr[j]
					j += 1 
				
				
				# print(left, right)
				return max(left , right)
			
				
				
			else:
				# print('df',pig)
				return pig
			
		# print(repo, rst)
		for arr in repo:
			 if len(arr) >0 : rst = max(rst, f(arr))
		return rst
		