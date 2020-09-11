'''https://leetcode.com/problems/remove-duplicates-from-sorted-list'''
class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		tmp = head  # 1->1->2->3->3
		while tmp:
			while tmp.next and tmp.next.val == tmp.val:
				tmp.next = tmp.next.next
			
			tmp = tmp.next
		return head