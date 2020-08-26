class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rst = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                rst.append('FizzBuzz')
            elif i% 5 == 0:
                rst.append('Buzz')
            elif i% 3 == 0:
                rst.append('Fizz')               
            else:
                rst.append(str(i))
        return rst