class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        root = list('123456789')
        str_low, str_high = str(low), str(high)
        start, end = len(str_low), len(str_high)       
        rst = []
        # print(root, start, end)
        for l in range(start, end+1):
            for i in range(0, 10 - l ):
                tmp =int(''.join(root[i: i+l])) 
                # print(tmp)
                if tmp > high:
                    return rst
                if tmp >= low: rst.append(tmp)
        
        
        
        return rst
