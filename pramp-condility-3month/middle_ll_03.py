class Solution:
	def middleNode(self, head: ListNode) -> ListNode:
		first = head
		second = head
		while second and second.next:
			first = first.next
			if second and second.next : second = second.next.next 
		return first