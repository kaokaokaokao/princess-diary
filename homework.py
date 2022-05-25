def number_generator(major):
    if major == 'computer':
        x = 61
    elif major == 'japanese':
        x = 56
    major_number = []
    for i in range(1,x+1):
        number = ''
        A = B = 0
        number += '20220902'
        if i in range(1,10):
            number += '00' + str(i)
        else:
            number += '0' + str(i)
        for k in number:
            A += int(k)
        while A not in range(1,10):
            temp1 = 0
            for m in str(A):
                temp1 += int(m) 
            A = temp1  
        B = number[-1] + number[-2] + number[-3]
        while B not in range(1,10):
            temp2 = 0
            for n in str(B):
                temp2 += int(n)
            B = temp2
        number += str(A%B)
        major_number.append(number)
    return major_number

print(f'计算机专业学号: {number_generator("computer")} \n日语专业学号: {number_generator("japanese")}')