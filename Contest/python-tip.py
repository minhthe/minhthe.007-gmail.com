####### EXAMPLE USING MAP, FILTER, REDUCE ###########
from functools import reduce
numbers = [1,2,3,4,67,34,76,8,34]

def square(x):
    return x**2 

def even(x):
    return x & 1 == 0

def mutiply(x, y):
    return x * y

###### NOT use LAMBDA ########

u, v = map(int ,input().split())
print(u,v)
print('###### NOT use LAMBDA ########')
squares = list( map ( square, numbers ) )

print(squares)

evens = list(x for x in numbers if even(x))
print(evens)

evens = list(filter(even, numbers))  # return these list that FILTER
print(evens)

print("####map vs filter: map return the SAME AMOUNT with orginal list that already tranformed####")

evens = list(map(even, numbers))     # return the orginal list which is transformed
print(evens)

product = reduce(mutiply, numbers)
print(product)


######  USING LAMBDA ########
print("######  USING LAMBDA ########")
print(list(map(  lambda x : x**2 , numbers )))
print(list(filter(  lambda x : x & 1 ==0 , numbers ) ))
print(( reduce( lambda x, y : x *y, numbers ) ))

##### usign deque#####
import collections as col
#Insert some elements into the queue at first
my_deque = col.deque('124dfre')
print('Dequeue: ' + str(my_deque))
#insert x at right and B at left
my_deque.append('x')
my_deque.appendleft('B')
print('Dequeue after appending: ' + str(my_deque))

import collections as col
#Insert some elements into the queue at first
my_deque = col.deque('124dfre')
print('Dequeue: ' + str(my_deque))
#delete item from right and left
item = my_deque.pop()
print('Popped Item: ' + str(item))
item = my_deque.popleft()
print('Popped Item: ' + str(item))
print('Dequeue after pop operations: ' + str(my_deque))