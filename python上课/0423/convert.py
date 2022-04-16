numbers = input('numbers you want to convert: ')
dic1= {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
output = ''
for number in numbers:
  output += dic1[number]+' '
print(output)
