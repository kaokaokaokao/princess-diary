input = input("give me some numbers\n")

a = input.split(",")
input = []
for n in a:
  input.append(int(n))

def quick_sort(input):
  if len(input) >= 2:
    ref = input[0]
    left = []
    right = []
    input.remove(input[0])
    for n in input:
      if n <= ref:
        left.append(n)
      else:
        right.append(n)
    return quick_sort(left) + [ref] + quick_sort(right)
  else : 
    return input

print(quick_sort(input))