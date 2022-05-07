s = int(input("最小值："))
d = int(input("最大值："))

def prime(s,d):
    list1 = []
    for m in range(s,d+1):
        if m == 2:
            list1.append(m)
            continue
        for n in range(2,m):
            if m%n == 0:
                break
            elif n == m-1:
                list1.append(m)
            else:
                continue
    return list1

print(prime(s,d))