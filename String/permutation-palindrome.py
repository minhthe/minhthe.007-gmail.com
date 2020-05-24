'''
https://www.hackerearth.com/problem/algorithm/palindrome-check-2-1/description/
'''

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
s = input()
mp = { }
for c in s:
    mp[c] = 1 if c not in mp else mp[c] + 1
even = 0
odd = 0 
for key in mp:
    if mp[key] & 1:
        odd += 1
    else:
        even += 1
if odd == 0:
    print("YES") 
else:
    rst = "YES" if odd % 2 != 0 else "NO"
    print(rst)

