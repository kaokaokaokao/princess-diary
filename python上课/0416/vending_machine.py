stock = ["农夫山泉","可口可乐","水溶c100","东方树叶","尖叫"]
actual_stock = stock[:]
price = [2,5,6,5,4]
total_price = 0
print(stock)
while True:
  customer = input("请输入您要购买的物品的名称 输入“清单”可以查询物品清单 输入“退出”可以结束购物 \n")
  if customer == "清单":
    print(f"当前贩卖机售卖的物品为: {stock} \n")
  elif customer == "退出":
    print(f"您的购物总金额是: {total_price}, 谢谢光临！")
    break
  else:
    if customer in actual_stock:
      index = stock.index(customer)
      print(f"{stock[index]}的价格是: {price[index]}")
      confirm = input("您确定要购买吗  ")
      if confirm == "是":
        total_price += price[index]
        actual_stock.remove(customer)
      elif confirm == "否":
        pass
    elif customer not in actual_stock and customer in stock:
      print("非常抱歉，该物品已售罄")
    else:
      print("请重新输入")