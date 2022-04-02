nums = input("numbers?")
target = input("target?")

a = nums.split(",")
arr = []
for n in a:
  arr.append(int(n))

def sumUp(inp, out):
  length = len(inp)
  temp = int(out)
  for i in range(length):
    for j in range(i + 1, length): 
      if inp[i] + inp[j] == temp:
        return i,j

res = sumUp(arr, target)
print(res)