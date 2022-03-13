strings = ["flower", "flow", "flight"]

def findCommonStr(strs):
	str1 = strs[0]
	result = ""
	for i in range(len(str1)):
		for j in range(len(strs)):
			if i >= len(strs[j]):
				return result
			if str1[i] == strs[j][i]:
				if j == len(strs) - 1:
					result = result + str1[i]
			else:
				break
	return result

print(findCommonStr(strings))