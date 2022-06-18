def drawpic(x):
  y = x
  for i in range(1,2*x+1,2):
      print(' '*y,'*'*i,' '*y)
      y -= 1
drawpic(5) 