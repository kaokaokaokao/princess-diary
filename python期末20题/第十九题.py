dic = {'0','1','2','3','4','5','6','7','8','9'}
for i in range(10,100):
    a = str(i ** 3) + str(i ** 4)  
    if  len(set(a)) == len(dic):
        print(i)
        break