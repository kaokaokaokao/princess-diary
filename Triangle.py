input = int(input("how many rows?\n"))

def form(input):
  list1 = []
  list2 = []
  list3 = []
  for n in range(input):
    list1.append(1)
    if n == 0:
      list2 = list1[:]
      list3.append(list2)
    elif n == 1:
      list2 = list1[:]
      list1.clear()
      list3.append(list2)
    elif n > 1:
      for m in range(n-1):
        i = list2[m]+list2[m+1]
        list1.append(i)
      list1.append(1)
      list2 = list1[:]
      list1.clear()
      list3.append(list2)
  return list3

print(form(input))