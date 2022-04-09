wishlist = ["想去迪士尼","想去看海","想去看一次演唱会","想买一个相机"]
print(wishlist)
while True:
  accomplished = int(input())
  del wishlist[accomplished-1]
  if wishlist == []:
    print("愿望全部完成！")
    break
  print(wishlist)