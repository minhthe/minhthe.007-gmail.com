'''

'''
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        tmp = [x + 1 for x in arr]
        cnt = 0
        for item in tmp:
            for e in arr:
                if(item == e):
                    cnt += 1
                    break
        return cnt