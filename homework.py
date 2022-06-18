import random
f = open("/Users/hukeer/Desktop/stu2.txt",encoding="utf-8")
stu = f.read()
stu = stu.split("\n")
f.close()
print(random.choices(stu, k=5))

f2 = open("/Users/hukeer/Desktop/scores.txt",encoding="utf-8")
scores = f2.read()
scores = scores.split("\n")
f2.close()
f3 = open("/Users/hukeer/Desktop/scored.txt",'w',encoding="utf-8")
A ,B ,C ,D ,E ,total = 0,0,0,0,0,0
for score in scores:
    temp = score.split("\t")
    grade = int(temp[1])*.4 + int(temp[2])*.6
    score = temp[0] + '\t' + str(grade)
    total += grade
    f3.write(score+"\n")
    if grade >= 90:
        A += 1
    elif grade >= 80:
        B += 1
    elif grade >= 70:
        C += 1
    elif grade >= 60:
        D += 1
    else:
        E += 1
f3.close()
member = len(scores)
aver = total/member
print(f'学生总人数为:{member}\n90分以上人数为:{A}\n80至89分人数为:{B}\n70至79分人数为:{C}\n60至69分人数为:{D}\n60分以下人数为:{E}\n平均分为:{aver:.2f}')

