'''https://leetcode.com/problems/reverse-linked-list'''
class Solution:
	def reverseList(self, head: ListNode) -> ListNode:

		prev = None 
		tmp = head
		while head:
			next = head.next
			head.next = prev
			prev = head
			head = next
		return prev