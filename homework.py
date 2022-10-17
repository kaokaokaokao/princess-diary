import jieba
with open('/Users/hukeer/Downloads/Python模拟演练/荷塘月色.txt',encoding='gbk') as file1, open('/Users/hukeer/Downloads/Python模拟演练/中文虚词列表.txt',encoding='gbk') as file2:
    article = jieba.lcut(file1.read())
    stopwords = jieba.lcut(file2.read())
    dic = {}
    for word in article:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    for word in stopwords:
        if word in dic:
            del dic[word]
    for key in dic:
        print(key,dic[key])