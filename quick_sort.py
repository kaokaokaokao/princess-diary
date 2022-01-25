ysh = input("give me some numbers")

a = ysh.split(",")
douche = []
for n in a:
  douche.append(int(n))
  print (n)

def quick_sort(asshole):
  if len(asshole) >= 2:
    ref = asshole[0]
    left = []
    right = []
    asshole.remove(ref)
    for n in asshole:
      if n <= ref:
        left.append(n)
      else:
        right.append(n)
    return quick_sort(left) + [ref] + quick_sort(right)
  else : 
    return asshole

print(quick_sort(douche))