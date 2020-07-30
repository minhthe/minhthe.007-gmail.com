'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''
class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		mp = {}
		tmp = head
		previous = head  # 1->1->2->3->3
		while(tmp):
			if tmp.val in mp:
				previous.next = tmp.next
				
			else:
				mp[tmp.val] = True
				previous = tmp
			tmp= tmp.next
		
		return head