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
print(result)

def guess(number):
  A = 0
  B = 0
  for j in range(len(m)):
    if m[j] == number[j]:
      A+=1
    elif m[j] in number:
      B+=1
  return A,B

out=guess(m)
print(out[0],"A")