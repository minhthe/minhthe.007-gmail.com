'''
https://www.hackerearth.com/problem/algorithm/palindrome-check-2-1/description/
'''
'''

# Write your code here
s = input()
mp =  {}
t = ord(s[0])
for i in range(1,len(s)):
    t ^= ord(s[i])
if t == 0:
    print('YES')
    exit()

for c in s:
    mp[c] = 1 if c not in mp else mp[c] + 1
# print(mp)
for key in mp:
    if mp[key] & 1 and key == chr(t):
        print('YES')
        exit() 
print('NO')
exit() 

