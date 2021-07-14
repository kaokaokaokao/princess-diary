s = int(input("最小值："))
d = int(input("最大值："))

def prime(s,d):
  list = []
  for m in range(s,d+1,1):
    i = m//2+1
    for n in range(2,i):
      if m%n == 0:
        break
      elif n == i-1:
        list.append(m)
      else:
        continue
  return list

print(prime(s,d))