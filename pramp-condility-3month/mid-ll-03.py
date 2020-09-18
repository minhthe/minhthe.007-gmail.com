'''https://leetcode.com/problems/middle-of-the-linked-list/'''
class Solution:
	def middleNode(self, head: ListNode) -> ListNode:
		slow = head
		fast = head
		while slow.next :
			slow = slow.next
			fast = fast.next.next
			if not fast or not fast.next: return slow
		return slow