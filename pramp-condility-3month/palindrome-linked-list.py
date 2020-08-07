'''https://leetcode.com/problems/palindrome-linked-list/'''
class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		
		def reverse(p):
			
			# 1 2 2 1 - > 1 2 -?> 1->  2-> null
			dummy = head
			previous = None
			# 1 2 1 -> 2
			while(dummy):
				if(dummy.next == p):
					while(p):
						next = p.next
						p.next = previous
						previous = p
						p = next
					dummy.next = previous
					return previous
				dummy = dummy.next
			
				# 1 2 ->  3 -> 4 -> null  
			
				
			# 1 2 3 4 -> null : 
			
		slow, quick = head, head
		while(quick and quick.next):
			quick = quick.next.next
			slow = slow.next
		tmp = reverse(slow)
		# print(head)
		tmp2 = tmp
		# print(tmp2)
		while(tmp != head and tmp) :
			if head.val != tmp2.val: return False
			tmp2 = tmp2.next
			head = head.next
		return True