import time, random
import pandas as pd
import requests
from lxml import etree

header = {
    'Content-Type': 'text/html; charset=utf-8',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)''AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3''Safari/605.1.15',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate, br',这一行加了会报错
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Cache-Control': 'must-revalidate, no-cache, private',
    'Connection': 'keep-alive',
    'Host': 'movie.douban.com',
    # 'Referer': 'https://movie.douban.com/subject/1889243/comments?start=0&limit=20&status=P&sort=new_score',
    'Cookie':'__utma=30149280.183796112.1653286052.1653315892.1653317735.6; __utmb=30149280.0.10.1653317735; __utmc=30149280; __utmv=30149280.25349; __utmz=30149280.1653286052.1.1.utmcsr=search.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/movie/subject_search; push_doumail_num=0; push_noty_num=0; __utma=223695111.693229332.1653286052.1653315892.1653317735.6; __utmb=223695111.0.10.1653317735; __utmc=223695111; __utmz=223695111.1653286052.1.1.utmcsr=search.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/movie/subject_search; _pk_id.100001.4cf6=ce9de800d8df86ed.1653285977.6.1653317746.1653315896.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1653317735%2C%22https%3A%2F%2Fbaidu.com%2F%22%5D; _vwo_uuid_v2=D6EC9C4BF327FCD9F097D5548B97F94F5|a7b30b1a2db2201bbe8fc70d06c08f82; __yadk_uid=sEABMS41D4oymZnnoBcmrH3Zqc9TSsnH; ck=QUYI; dbcl2="253498861:vo5XznNIC2k"; bid=mImVwX99J7Q; ll="118172"'
}

name_list = []
star_list = []
time_list = []
like_list = []
text_list = []

try:
    for i in range(0,200,20):
        url = 'https://movie.douban.com/subject/3649049/comments?start={0}&limit=20&status=P&sort=new_score'.format(i)
        # url = f'https://movie.douban.com/subject/1889243/comments?status=P'
        response = requests.get(url, headers=header)
        print(response)
        response.encoding = response.apparent_encoding
        dom = etree.HTML(response.text)
        print(dom)
        name = dom.xpath('//div[@class = "comment"]/h3/span[@class = "comment-info"]/a/text()')
        star = dom.xpath('//div[@class = "comment"]/h3/span[@class = "comment-info"]/span[2]/@title')
        time_ = dom.xpath('//div[@class = "comment"]/h3/span[@class = "comment-info"]/span[@class="comment-time "]/text()')
        like = dom.xpath('//div[@class = "comment"]/h3/span[@class = "comment-vote"]/span[@class = "votes vote-count"]/text()')
        txt = dom.xpath('//p[@class = " comment-content"]/span')
        txt = [j.text for j in txt]
        name_list.extend(name)
        for rating in star:
            if str(rating) in ['力荐','推荐','还行','较差','很差']:
                star_list.append(str(rating))
            else:
                star_list.append('Null')
        time_list.extend(time_)
        like_list.extend(like)
        text_list.extend(txt)
        print(f'已经完成第{i//20+1}页爬取')
        print(len(name_list))
        print(len(star_list))
        print(len(time_list))
        print(len(like_list))
        print(len(text_list)) 
        time.sleep(random.randint(10,20))
except Exception as f:
    print(f)
    pass
finally:
    dic = {
        'Name' : name_list,
        'Star' : star_list,
        'Time' : time_list,
        'Like' : like_list,
        'Review' : text_list
    }
    df = pd.DataFrame.from_dict(dic,orient='index').T #这边如果不加from_dict和orient会报错，加T只是因为我觉得竖着比较好看
    print(df)
    df.to_csv("/Users/hukeer/Desktop/影评.csv",encoding='utf-8-sig') #写入csv时一定要写encoding='utf-8-sig'语句