'''
https://leetcode.com/problems/reverse-linked-list/
''''
class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		
		
		rev = None
		while(head):
			next = head.next 
			head.next = rev
			rev = head 
			head = next 
		return rev