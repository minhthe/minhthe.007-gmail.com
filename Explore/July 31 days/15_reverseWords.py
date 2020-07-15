'''
https://leetcode.com/problems/reverse-words-in-a-string/
'''
class Solution:
	def reverseWords(self, s: str) -> str:
		tmp =list(x for x in s.split(" ") if len(x) > 0)
		i, j = 0, len(tmp)  -1
		while i < j:
			tmp[i], tmp[j] = tmp[j], tmp[i]
			i += 1
			j -= 1
			
		return " ".join(tmp)