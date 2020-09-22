'''https://www.pramp.com/challenge/VKdqbrq6B1S5XAyGAOn4'''
def reverse_words(arr):
  def reverse(l,r):
    i, j = l , r
    while i<j:
      arr[i], arr[j] = arr[j], arr[i]
      i, j =  i+1, j-1
  reverse(0, len(arr) - 1)
  start = 0 
  for i in range(len(arr)):
    if not(len(arr[i])== 1 and  ord('a') <= ord(arr[i]) <= ord('z')) :
      reverse(start, i - 1)
      start = i + 1
  reverse(start, len(arr) -1)
  return arr
arr = ['p', 'e', 'r', 'f', 'e', 'c', 't','  ','m', 'a', 'k', 'e','s','  ','p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
arr= ['a','b']
arr=["a","","","c"]
print(reverse_words(arr))
  