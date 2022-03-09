#位置对，数字对A
#数字对，位置不对B
import random
M = input("guess the numbers?")

def random_number():
  answer = set()
  while len(answer)<4:
    answer.add(random.randint(0,9))
  return answer
result = random_number()
print(result)

def guess(result):
    A = 0
    B = 0
  for j in range(M):
    if M[j] == result[j]:
      A+=1
    elif M[j] in result:
      B+=1
  return A,B

guess(M)
print(guess(M)[0],"A")