counter = 0
for i in range(1, 1000):
    if i % 3 == 0 and i % 7 == 0:
        counter += 1

print(f'同时能够被3和7整除的数字个数为:{counter}。')