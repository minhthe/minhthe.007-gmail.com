'''https://www.pramp.com/challenge/W5EJq2Jld3t2ny9jyZXG'''
def word_count_engine(document):
  pass # your code goes here
  def convert(s):
    
    tmp = ""
    for c in s:
      if ord('a') <= ord(c) <= ord('z'): tmp+=c
    return tmp
     
  words = document.split(" ")
  mp = {}
  max_v = 0
  setences = []
  for i, word in enumerate(words):
    if len(word) > 0 :
      word = convert(word.lower())
      setences.append(word)
      if word not in mp:
        max_v += 1
        mp[word] = [1, i]

      else:
        mp[word][0] += 1

  arr = [[] for _ in range(max_v + 1)]
  visisted = {}
  for i, word in enumerate(setences):
    if word not in visisted:
      visisted[word] = True
      arr[ mp[word][0] ].append(  [ word,    str(mp[word][0])]     )
  rst = []
  for item in arr[::-1]:
    if len(item):
       for e in item:
          rst.append(e)
  return rst

document ="Practice makes perfect. you'll only get Perfect by practice. just practice!"
document ="Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. "
print(word_count_engine(document))   
                           
                           
  
    
  