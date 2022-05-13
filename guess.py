#位置对，数字对A
#数字对，位置不对B
import random

def guess():
  result = set()
  while len(result)<4:
    result.add(random.randint(0,9))
  list1 = []
  for i in result:
    list1.append(i)
  while True:
    A = 0
    B = 0
    number = input("guess the numbers?")
    length = len(number)
    for j in range(length):
      comp1 = int(number[j])
      for k in range(length):
        if comp1 == list1[k]:
          if j == k:
            A += 1
          else:
            B += 1
    print(A,"A",B,"B")
    if A == 4:
      break

guess()