'''https://www.pramp.com/challenge/L3wQBnQYAEh5K97W9ONK'''
def get_indices_of_item_wights(arr, limit):
  
  rst= []
  mp = {}
  
  for i, v in enumerate(arr):
    if limit - v in mp:
      rst = [ i, mp[limit - v]]
      return rst
    mp[v] = i
    
    
  return rst


