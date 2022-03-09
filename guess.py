#位置对，数字对A
#数字对，位置不对B
import random
m = input("guess the numbers?")

def random_number():
  answer = set()
  while len(answer)<4:
    answer.add(random.randint(0,9))
  return answer
result = random_number()
list1 = []
for i in result:
  list1.append(i)

def guess(number):
  A = 0
  B = 0
  length = len(number)
  for j in range(length):
    comp1 = int(number[j])
    if comp1 == list1[j]:
      A += 1
      result.remove(comp1)
  for k in range(length):
    comp2 = int(number[k])
    if comp2 in result:
      B += 1
  return A,B

out = guess(m)
print(out[0],"A",out[1],"B")