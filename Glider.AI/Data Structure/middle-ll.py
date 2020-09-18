'''https://app.glider.ai/practice/problem/data-structures/find-the-middle-of-a-linked-list/problem'''
class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    def __init__(self):
        self.head = None
 
    # Reverse the linked list
    def findMiddle(self):
        # Write your code here
        k = n//2 
        tmp = self.head
        while k>0 :
            tmp = tmp.next 
            k -= 1 
        print(tmp.data)
         
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


def solve(llist):
    llist.findMiddle()

llist = LinkedList()
n = int(input())
array = list(map(int, input().strip().split(' ')))
for i in range(n):
    llist.push(array[i])

solve(llist)
