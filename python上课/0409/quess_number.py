number = 9
i = 0
while i < 3:
  guess = int(input("guess:"))
  i += 1
  if guess == number:
    print("闯关成功！",end = " ")
    break
else:
  print("闯关失败！",end=" ")

print("游戏结束")