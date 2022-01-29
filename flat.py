arr = [1,2,[1,3,[2,[2,3,3],[2,5]]],[6,3]]

def flat(m):
  list1 = []
  for n in m:
    if isinstance(n,list) == False:
      list1.append(n)
    else:
      i = flat(n)
      list1 = list1 + i
  return list1

print(flat(arr))