'''https://app.glider.ai/practice/problem/data-structures/insertion-in-a-singly-linked-list'''
class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    def __init__(self):
        self.head = None
 
    
 
    def insert(self, k):
        # Write your code here
        pass
        dummy = Node(None)
        dummy.next = self.head 
        cur = self.head
        flag = True
        while cur and cur.data < k: 
            flag = False
            dummy = cur
            cur = cur.next 
        if flag:
            tmp = self.head
            kk =Node(k)
            self.head = kk 
            kk.next = tmp 
        else:
            tmp = dummy.next
            kk = Node(k)
            dummy.next = kk 
            kk.next = tmp

        
         
    def push(self, new_data):
        if(self.head == None):
            self.head = Node(new_data)
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = Node(new_data)
        
 
    def printList(self):
        temp = self.head
        result = "";
        while(temp):
            result += str(temp.data) + " "
            temp = temp.next
        print(result)



def solve(llist, k):
    llist.insert(k)
    llist.printList()
    

llist = LinkedList()
n, k = map(int, input().strip().split())
array = list(map(int, input().strip().split(' ')))

for i in range(n):
    llist.push(array[i])

solve(llist, k)