'''https://www.pramp.com/challenge/N5LYMbYzyOtbpovQoYPX'''   
def find_pivot(arr):
  
  l, r = 0 , len(arr)- 1
  while l < r:
    
    mid = int(( l + r) // 2)
    if arr[mid - 1] < arr[mid] > arr[mid +1]:
      return mid
    
    if arr[mid - 1] < arr[mid] < arr[mid +1]:
      l = mid + 1
    else:
      r = mid -1
      
  return l
def find_index(arr, l ,r, num):
  while l <= r:
    
    mid = int( (l+r)//2 )
    if arr[mid] == num: return mid
    if arr[mid] < num:  # 1 2 3  4
      l = mid + 1
    else:
      r = mid - 1
     
  return -1
  
  
  
def shifted_arr_search(shiftArr, num):
  # find the pivot
  pivot = find_pivot(shiftArr)
  # 2 subarray ordered:
  l, r = 0, pivot
  p = find_index(shiftArr,l, r,num)
  if p != -1: return p
  l, r = pivot + 1, len(shiftArr) -1
  p = find_index(shiftArr, l, r,num)
  if p != -1: return p
  return -1
