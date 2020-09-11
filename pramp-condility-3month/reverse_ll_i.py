'''https://leetcode.com/problems/reverse-linked-list'''
class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		# head 1 2 3 4 -> null
		#  null<-1<-2<-3<-4 -< head
		# head -> 1 -> 2 -> none
		tmp = None
		while head:
			next_point = head.next   # None
			head.next = tmp    #-> None 2-> 1-> NOne 
			tmp = head         # tmp = 2
			head = next_point  # None
		return tmp