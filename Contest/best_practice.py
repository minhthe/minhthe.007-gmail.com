'''

# bit manipulation:
'{0:08b}'.format(number) =  bin(number)[2:].zfill(8) 
**the max length of one number in bit : 
from math import log
l = int(log(num,2) + 1) if num > 0 else 1


# heap max not maintain the heap property when get the item out of the curernt heap
-> so using the min head (multuiple (-1) if needed) 

# formular: using queu in leetcode
from queue import Queue
q = Queue()
q.put((headID, informTime[headID]))  | q.get  | while(q.empty() is False):



# linked list:
tmp = head
tmp = tmp.next
-> head will follow 

heap = tmp
tmp = tmp.next
-> head still stand on the first place


# clone object of matrix 2D:
new_matrix = list(map(list, old_matrix))


### set the maxiumn when find minimun( base on perimeter ) -> not the value constrain. 
https://app.codility.com/demo/results/trainingTWTH8T-98Q/


'''