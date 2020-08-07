'''
https://www.pramp.com/challenge/MW75pP53wAtzNPVLPG0d
'''
import collections
def shortestWordEditPath(source, target, words):

  def diff_one_letter(s,t):
    rst = [[0 for i in range(len(t)+1)] for j in range(len(t)+1) ]
    for i in range(1, len(s)+1):
      for j in range(1, len(t)+1):
        if s[i-1] == t[j-1]:
          rst[i][j] = rst[i-1][j-1] + 1
        else:
          rst[i][j] = max(rst[i-1][j], rst[i][j-1])
    print(s,t , rst)
    return rst[len(s)][len(t)]
   
  def buildGraph(words):
    if source not in words: words.append(source)
    for i in range(len(words) -1):
      for j in range(i + 1, len(words)):
        current_node = words[i]
        #print(current_node, words[i])
        if len(current_node) == len(words[j]) and diff_one_letter(current_node, words[j]) == len(current_node) -1:
          graph[current_node].append(words[j])
          graph[words[j]].append(current_node)
   # print(graph)
    return graph

  graph = collections.defaultdict(list)
  
  graph = buildGraph(words)
  print(graph)
  que = [(source, 0)]
  visisted = {}
  
  
  
  while que:
    u,l = que.pop(0)
    print(u)
    visisted[u] = True
    for neighbour in graph[u]:
      if neighbour not in visisted: 
        visisted[neighbour] = True
        que.append(  ( neighbour, l + 1 ) )
        if neighbour == target:
          return l + 1
  return -1

source, target = "abc", "ab"
words=["abc","ab"]
print(  shortestWordEditPath(source, target, words) )






