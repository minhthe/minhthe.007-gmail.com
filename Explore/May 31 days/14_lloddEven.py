'''
https://leetcode.com/problems/odd-even-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None: return head
        p_odd = head
        p_even = head.next
        even = p_even
        while( p_even and p_even.next):
            p_odd.next = p_even.next
            p_odd = p_odd.next
            p_even.next= p_odd.next
            p_even = p_even.next
            
        p_odd.next = even
        return head