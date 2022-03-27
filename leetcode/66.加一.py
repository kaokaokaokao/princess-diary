digits = list(input("number?"))
list1 = []
for i in digits:
  list1.append(int(i))

def plus_one(list1):
	length = len(list1)
	result = 0
	j = length-1
	true_result = []
	for i in range(length):
		result = result + list1[i]*(10**j)
		j -= 1
	result+=1
	list2 = list(str(result))
	for k in list2:
		true_result.append(int(k))
	return true_result
print(plus_one(list1))