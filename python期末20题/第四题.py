import random
key = random.randint(1, 100)
guess = int(input())
if guess == key:
    print("恭喜您猜对了")
elif guess > key:
    print("您的猜测太大")
else:
    print("您的猜测太小")