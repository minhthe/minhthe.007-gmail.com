'''
https://leetcode.com/problems/middle-of-the-linked-list/

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        tmp = head
        while(tmp):
            arr.append(tmp.val)
            tmp = tmp.next
        middle = len(arr)//2
        
        def f(head, pos, arr):
             
            dummy = ListNode(arr[pos])
            head = dummy
            for i in range(pos+1, len(arr)):
                dummy.next = ListNode(arr[i])
                dummy = dummy.next
            
            return head
        return f(head, middle, arr)
            