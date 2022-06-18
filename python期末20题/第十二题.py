def multiplication(a):
    if a == 1:
        return 1
    else:
        return a * multiplication(a-1)

print(multiplication(5))