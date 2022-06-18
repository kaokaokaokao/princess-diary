f = open('/Users/hukeer/python/python期末20题/car_data.txt','r',encoding='utf-8')
data = f.read().split('\n')
f.close()
print('在该区间出现的车辆为:')
for i in range(len(data)):
    data[i] = data[i].split(',')
    if (121.45 < float(data[i][-1]) < 121.55) and (31.2222 < float(data[i][-2]) < 31.2333):
        print('时间:{}  车牌:{} 北纬:{} 东经:{}'.format(data[i][0],data[i][1],data[i][-2],data[i][-1]))