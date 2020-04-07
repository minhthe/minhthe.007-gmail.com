'''
https://leetcode.com/problems/shortest-palindrome/

***explanation:
https://leetcode.com/problems/shortest-palindrome/discuss/60099/AC-in-288-ms-simple-brute-force

Example: s = dedcba. Then r = abcded and I try these overlays (the part in (...) is the prefix I cut off, I just include it in the display for better understanding):

  s          dedcba
  r[0:]      abcded    Nope...
  r[1:]   (a)bcded     Nope...
  r[2:]  (ab)cded      Nope...
  r[3:] (abc)ded       Yes! Return abc + dedcba
  
'''
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        for i in range(len(r)):
            if(s.startswith(r[i:])):
                return r[:i] + s
        return r + s