if __name__ == '__main__':
		nums = [-2,1]
		max_end = nums[0]
		s = 0 
		start , end = 0 , 0
		for i, v in enumerate(nums):
			s += v
			if s > max_end:
				max_end = s
				end = i
			if s <= 0 :
				s = 0 
				start = i + 1
		print(max_end) 
		print('the subarray', nums[start : end + 1])