'''https://leetcode.com/problems/unique-email-addresses/'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        arr = []        
        for e in emails:
            x, y  = e.index("+"), e.index("@")
            arr.append(  e[: x].replace(".", "") + e[y :  ] )
        return len(set(arr))
        