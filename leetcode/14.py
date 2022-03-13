strs = ["flower", "flow", "flowght"]

result = ""
index = 0
length = len(strs[0])
while(index >= 0):
	temp = ""
	for i in range(len(strs)):
		if index == 0 and length > len(strs[i]):
			length = len(strs[i])
		if (i == 0): 
			temp = strs[i][index]
		if length > index and strs[i][index] == temp:
			if (i == len(strs) - 1): 
				index += 1
				result += temp
			continue
		else:
			index = -1
			break

print(result)