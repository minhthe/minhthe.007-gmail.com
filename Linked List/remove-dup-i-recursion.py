'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None: return head
        
        cur = head
        
        if cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
            self.deleteDuplicates(cur)
        else:
            self.deleteDuplicates(cur.next)
            
        return head