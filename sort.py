list = [1,9,23,45,754,235,35,467]
n = len(list)
print(list)
list2 = []
list2.append(list[0])

def sortlist(list):
  for s in range(1,n,1):
    j = s-1
    while list[s] < list2[j] and j >= 0:
      j -= 1
    else:
      list2.insert(j+1,list[s])
  return list2

sortlist(list)
print(list2)