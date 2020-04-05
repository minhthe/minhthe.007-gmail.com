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

