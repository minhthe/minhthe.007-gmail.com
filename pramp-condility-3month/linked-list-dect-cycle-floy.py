class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		slow , quick = head, head
		while quick and quick.next and quick.next.next  :
			slow = slow.next
			quick = quick.next.next
			if slow == quick: return True
		return False