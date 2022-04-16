numbers = [2,7,4,9,1,3,10]

max = numbers[0]
for number in numbers:
  if max < number:
    max = number
print(max)