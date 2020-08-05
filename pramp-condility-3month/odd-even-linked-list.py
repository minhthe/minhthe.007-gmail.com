'''
https://leetcode.com/problems/odd-even-linked-list/
'''
class Solution:
	def oddEvenList(self, head: ListNode) -> ListNode:
		if head is None: return head
		odd = head
		even = None
		if head.next: even = head.next
		fix_even = even
		while odd and even:
			if odd.next:
				odd.next = odd.next.next
				if odd.next: odd = odd.next
			# if odd is None: break
			if even :
				if even.next: even.next = even.next.next
				even = even.next
			if even is None: break
		
		if even is not None: even.next= None
		odd.next = fix_even
		
		return head