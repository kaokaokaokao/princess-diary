#位置对，数字对A
#数字对，位置不对B
import random
def random_number():
  answer = set()
  while len(answer)<4:
    answer.add(random.randint(0,9))
  return answer
result = random_number()
list1 = []
for i in result:
  list1.append(i)

def guess():
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