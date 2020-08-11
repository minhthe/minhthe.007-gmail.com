''''
https://leetcode.com/problems/middle-of-the-linked-list
''''
class Solution:
	def middleNode(self, head: ListNode) -> ListNode:
		slow = head
		quick = head
		while(quick and quick.next):
			slow = slow.next
			if quick.next: quick = quick.next.next   # 1  null
		#if quick: return slow
		return slow