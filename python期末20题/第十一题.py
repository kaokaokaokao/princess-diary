# 中文和英文写法一致
f = open('/Users/hukeer/python/python期末20题/file1.txt', 'r',encoding='utf-8') # 可以换成file2.txt
text = f.read()
f.close()
characters = 0
lines = 0
for i in text:
    if i == '\n':
        lines += 1
    elif i.isalpha():
        characters += 1
print(f"文件中有{lines}行，{characters}个字符")