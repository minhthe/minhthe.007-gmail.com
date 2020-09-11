'''https://app.glider.ai/practice/problem/algorithms/generate-all-permutations-of-a-string/problem'''
# Note: Proper indentation is required 
# Click HELP above to see examples of handling input/debug/output 
# INPUT: n = input() 
# DEBUG: print(n) 
# OUTPUT: print(result) 

# Write the code to solve the problem below,  
# format the "result" as specified in the problem statement 
# and finally, write the result to stdout 
# IMPORTANT: Remove all debug statements for final submission 
n = input()

n = list(n)
arr = []
def f(pos):
    if pos == len(n):
        arr.append(''.join(n))
    for i in range(pos, len(n)):
        n[i], n[pos] =  n[pos], n[i]
        f(pos + 1)
        n[i], n[pos] = n[pos], n[i]
    return arr
f(0)

arr.sort()
rst = ' '.join(arr)
print(rst)