''''
https://leetcode.com/problems/maximum-performance-of-a-team/
***from this explanation:
https://leetcode.com/problems/maximum-performance-of-a-team/discuss/542193/Python3-Share-my-heapq-implementation
'''
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        s, e = speed, efficiency
        ens = list(zip(s,e))
        ens.sort(key = lambda x: -x[1])
        rst = 0 
        priorityQueue =[]
        heapq.heapify(priorityQueue)
        good_sum = 0
        for en in ens:
            if(len(priorityQueue) == k):
                if(priorityQueue[0] < en[0] ):  # if there's an engineer with higher speed, there's a good chance to get higher performance
                    bad = heapq.heappop(priorityQueue)# fire the guy with the lowest speed
                    heapq.heappush(priorityQueue,en[0])
                    good_sum = good_sum + en[0] - bad
            else:
                heapq.heappush(priorityQueue,en[0])
                good_sum += en[0]
            rst = max(rst, en[1] * good_sum)
        return rst%(1000000000 + 7)
        
        