bank_account = 20000
import time
while True:
  request = int(input("查询余额请按1, 存款请按2, 取款请按3, 退出请按0 \n"))
  if request == 1:
    pass
  if request == 2:
    deposit = int(input("存款金额："))
    bank_account += deposit
    print("存款成功")
  if request == 3:
    withdraw = int(input("取款金额："))
    if withdraw > bank_account:
      print("余额不足")
    else:
      bank_account -= withdraw
      print("取款成功")
  if request == 0:
    comment = input("请为我的服务评价(1-10分): \n")
    print("感谢您的评价，祝您生活愉快！")
    break
  time.sleep(1)
  print(f"\n您的余额为: {bank_account} \n")