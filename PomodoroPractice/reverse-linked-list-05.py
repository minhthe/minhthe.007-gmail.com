'''
https://leetcode.com/problems/reverse-linked-list/
'''
class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		# 1 2 3 4 5 
		previous = None
		while(head):
			next = head.next
			head.next = previous
			previous = head
			head = next
		return previous