'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''
class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		dummy = ListNode(None)
		dummy.next= head
		curr = dummy
		mp =  {}
		
		while(curr.next):
			mp[curr.val] = True
			if curr.next.val not in mp:
				curr = curr.next
			else:
				curr.next = curr.next.next
		return dummy.next