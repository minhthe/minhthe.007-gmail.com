'''
https://www.pramp.com/challenge/wqNo9joKG6IJm67B6z34
'''
def get_shortest_unique_substring(arr, str):
  pass # your code goes here
  
  def check(substring, arr):
    mp = {}
    for c in substring:
      mp[c] = True
    
    for item in arr:
      if item not in mp:
        return False
    return True
    
  n = len(arr)
  fast, slow = 0, n - 1
  ans = ""
  min_v = int(1e9)
  
  # O(n^2)
  while( fast + n <= len(str) ):
  
    substring = str[fast:slow+1]
    if  check(substring, arr):
      if len(substring) < min_v :
      
        ans = substring
        min_v = len(substring)
      fast +=1
    elif slow < len(str):
      slow += 1
    else: 
      fast += 1
      
  return ans

  
  
print(get_shortest_unique_substring(['x', 'y', 'z'], "xyyyxyyz"))