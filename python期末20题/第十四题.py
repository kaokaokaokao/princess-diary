a = float(input())
b = float(input())
sign = input()
dic = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}
if sign in dic:
    if sign == '/' and b == 0:
        print('除数为0错误')
# 以下为题目给出部分       
    else:
        print('两数运算结果为',dic[sign])
else:
    print('符号输入错误')