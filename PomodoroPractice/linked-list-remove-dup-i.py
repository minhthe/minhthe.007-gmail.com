
'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = head
        if head is None: return None
        while(tmp.next):
            if tmp.next.val == tmp.val:
                tmp.next = tmp.next.next
            if tmp.next and tmp.next.val != tmp.val: tmp = tmp.next
        return head