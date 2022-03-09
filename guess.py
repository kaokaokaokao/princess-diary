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
print(list1)

def guess(number):
  A = 0
  B = 0
  for j in range(len(number)):
    print(number[j],list1[j])
    if number[j] == list1[j]:
      A += 1
      result.remove(number[j])
    elif int(number[j]) in result:
      B += 1
  return A,B

out = guess(m)
print(out[0],"A",out[1],"B")