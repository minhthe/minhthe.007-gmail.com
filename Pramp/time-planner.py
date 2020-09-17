''''https://www.pramp.com/challenge/3QnxW6xoPLTNl5jX5Lg1'''
def meeting_planner(slotsA, slotsB, dur):
  i, j = 0 , 0 
  na , nb = len(slotsA), len(slotsB)
  while i < na and j < nb:
    xa, ya = slotsA[i]
    xb, yb = slotsB[j]
    
    
    x , y  = max(xa, xb), min(ya, yb )
    if x + dur <= y:
      return [x, x + dur ]
    
    # checking the skip base on your hint draw  -> decide which increase -> 
    #  i    j  ------yb have more change      # vietnam dubai
    if ya < yb:
      i += 1 
    else:
      j +=1
  return []