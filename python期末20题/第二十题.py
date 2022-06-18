info = input()
with open('/Users/hukeer/python/python期末20题/hebei.txt','r',encoding='utf-8') as Uname:
    ls = Uname.readlines()
    if info == ls[0].split(' ')[0]:
        print(ls[0].split(' ')[1].split(','))
    for i in ls[1:]:
        if i.split(' ')[0] == info:
            print(i.split(' ')[1].split(','))
            break
        if info in i.split(' ')[1]:
            print(i.split(' ')[0])
            break
