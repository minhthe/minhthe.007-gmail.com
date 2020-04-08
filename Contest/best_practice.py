'''

# bit manipulation:
'{0:08b}'.format(number) =  bin(number)[2:].zfill(8) 



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

'''