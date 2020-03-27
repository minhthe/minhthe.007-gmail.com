''''
https://leetcode.com/problems/unique-morse-code-words/
'''

class Solution:
	def uniqueMorseRepresentations(self, words: List[str]) -> int:
		morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		mp = {}
		cnt = 0 
		def f(word, morse):
			tmp = ""
			for s in word:
				tmp += morse[(ord(s) - ord('a'))]
			return tmp
			
		for word in words:
			tmp = f(word, morse) 
			if(f(word, morse)  not in mp):
				cnt +=1
				mp[tmp] = True 
		return cnt