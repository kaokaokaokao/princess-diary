input = input("give me some numbers\n")

def cpr(input):
  list = []
  input = input.strip()
  flag = False
  for m in range(len(input)):
    char = input[m]
    if char == "-" or char == "+" and flag == False:
      list.append(char)
      flag = True
    elif char.isnumeric():
      list.append(char)
    else:
      break
  if flag and len(list) == 1:
    list.clear()
  s = ''.join(list)
  return s

print(cpr(input))