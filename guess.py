#位置对，数字对A
#数字对，位置不对B
import random
M = input("guess the numbers?")

def random_number():
  answer = []
  for i in range(4):
    answer.append(random.randint(0,9))
    i+=1
  return answer
result = random_number()
print(result)

def guess(answer):
  for j in range(int(M)):
    A = 0
    B = 0
    j = 0
    if M[j] == answer[j]:
      A+=1
      j+=1
    else:
      B+=1
  return A,B

guess(M)
print(guess(M)[0],"A")