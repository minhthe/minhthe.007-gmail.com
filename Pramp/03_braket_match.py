'''https://www.pramp.com/challenge/xJZA01AxdlfpM2vZ2Wwa'''
def bracket_match(text):
  
  stk_len = 0
  
  count = 0
  
  for letter in text: # ()
    
    if letter == ")":  # (( )
      
      # incese counter and not
      if stk_len > 0 :   #      #“())(”  count_open = 2 | count_close =  2
        stk_len -= 1
      else:
        count+=1
      
      
    else:  # "("
      stk_len += 1
      
      
  
  return count + len(stk)
