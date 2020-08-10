'''https://leetcode.com/problems/merge-two-sorted-lists'''
class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		tmp = ListNode(None)
		rst = tmp
		first = l1
		second = l2
		while first and second:
			if first.val < second.val:
				rst.next = ListNode(first.val)
				first = first.next
				
			else:
				rst.next = ListNode(second.val)
				second = second.next 
			rst = rst.next
		rst.next = second if second else first
		# print('tes', tmp)
		# print('tes',rst)
		return tmp.next