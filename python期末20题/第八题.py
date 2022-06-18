x1 = float(input("请输入第一个坐标x:"))
y1 = float(input("请输入第一个坐标y:"))
x2 = float(input("请输入第二个坐标x:"))
y2 = float(input("请输入第二个坐标y:"))
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print('两点之间的距离为:{:.2f}'.format(distance))