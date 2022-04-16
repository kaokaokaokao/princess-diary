list1 = [2,4,1,5,5,2,1,4,7,5,9]
list2 = []
for item in list1:
  if item not in list2:
    list2.append(item)
print(list2)