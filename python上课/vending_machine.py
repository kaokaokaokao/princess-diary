stock = ["农夫山泉","可口可乐","水溶c100","东方树叶","尖叫"]
actual_stock = ["农夫山泉","可口可乐","水溶c100","东方树叶","尖叫"]
price = [2,5,6,5,4]
while True:
  customer = input("请输入您要购买的物品的编号(1-5) 输入“清单”可以查询物品清单 输入“退出”可以结束购物 \n")
  if customer == "清单":
    print(f"当前贩卖机售卖的物品为: {stock} \n")
  elif customer == "结束":
    print("谢谢光临！")
    break
  else:
    customer = int(customer) - 1
      print(f"{stock[customer]}的价格是: {price[customer]}")
      confirm = input("您确定要购买吗")
      if confirm == "是":
        del actual_stock[customer]
      elif confirm == "否":
        pass
    else:
      print("当前物品已售罄")
