'''
https://leetcode.com/problems/minimum-window-substring
'''
class Solution:
	def minWindow(self, s: str, t: str) -> str:
		# t = ''.join(set(list(t)))
		# print(t)
		n = len(t)
		nn = len(s)
		i, j = 0, n - 1
		
		rst = ""
		mn = int(1e9)
		
		
		
		def check(ss):
			mp = {}
			for c in ss:
				mp[c] = mp[c] + 1 if c in mp else 1
			mp2 = {}
			# print(mp)
			for c in t:
				if c not in mp: return False
				mp2[c] = mp2[c]  +1 if c in mp2 else 1
			# print(mp2)
			for c in t:  # mp is string ,, mp2 is tempalte
				if mp[c] < mp2[c]:return False
				
			return True
			
		while i + n <= nn :
			# print((s[i:j+1]), check(s[i:j+1])  )
			if check(s[i:j+1])  :
				# print(s[i:j+1])
				if len(s[i:j+1]) < mn:
					rst = s[i:j+1]
					mn = len(rst)
				i += 1				
				
			elif j < nn:
				j += 1
			else:
				i+=1
		return rst