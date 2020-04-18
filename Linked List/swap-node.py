'''
https://leetcode.com/problems/swap-nodes-in-pairs/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmp = []
        if head is None: return None
        while(head):
            tmp.append(head.val)
            head = head.next        
        
        def f(arr):
            
            rst = None
            for i in range(0, len(arr)-1, 2):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                if rst is None: 
                    
                    rst = ListNode(arr[i])
                    head = rst
                    rst.next = ListNode(arr[i+1])
                    rst = rst.next
                else:
                    rst.next = ListNode(arr[i])
                    rst = rst.next
                    
                    rst.next = ListNode(arr[i+1])
                    rst= rst.next
            if(len(arr)&1):
                
                if rst is None:
                    rst = ListNode(arr[-1]) 
                    head = rst
                else:
                    rst.next = ListNode(arr[-1])
            return head
        tmp = f(tmp)
        return tmp
        
            
            