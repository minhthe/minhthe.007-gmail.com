'''
https://leetcode.com/problems/linked-list-cycle-ii
'''
class Solution:
	def detectCycle(self, head: ListNode) -> ListNode:
		
		slow, quick = head, head
		
		while quick and quick.next and quick.next.next:
			
			slow = slow.next
			quick = quick.next.next
			if slow == quick: 
				while(head!= slow):
					slow = slow.next
					head = head.next
				return head				
						
		return None