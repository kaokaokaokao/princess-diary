list = [1,9,23,45,754,235,35,467]

def sortlist(list):
  list2 = []
  for s in range(len(list)):
    j = s
    while j > 0 and list[s] < list2[j-1]:
      j -= 1
    else:
      list2.insert(j,list[s])
  return list2

result = sortlist(list)
print(result)