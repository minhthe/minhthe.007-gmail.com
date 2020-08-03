class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		mp = {}
		while head:
			if head in mp: return True
			mp[head] = True
			head = head.next
		return False
