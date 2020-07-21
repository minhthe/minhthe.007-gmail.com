'''
https://leetcode.com/problems/reverse-linked-list-ii/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        l = n  - m + 1
        
        if  m == 1: 
            # cur = ListNode(-1)
            # cur.next = head
            cur = None
            start = head
        else:
            cur = head
            pos = 1 
            while pos + 1 != m:
                cur = cur.next
                pos +=1
            
            start = cur.next
        reverse = None
        while l:
            l-=1
            # print(l)
            next = start.next
            start.next = reverse
            reverse = start
            start = next
        if cur:
            cur.next.next = start
            cur.next = reverse
            return head
        else:
            head.next = start
            return reverse