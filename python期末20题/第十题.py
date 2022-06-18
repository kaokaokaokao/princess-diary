number = int(input("请输入一个不大于10的整数:"))
factorial_number = 1
for i in range(1, number + 1):
    factorial_number *= i
print(f"{number}的阶乘是{factorial_number}")