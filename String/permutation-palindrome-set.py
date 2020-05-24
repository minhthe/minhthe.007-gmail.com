# Write your code here
s = input()
m = set()
for c in s:
    if c in m:
        m.remove(c)
    else:
        m.add(c)
ans = 'YES' if len(m) <= 1 else 'NO'
print(ans)