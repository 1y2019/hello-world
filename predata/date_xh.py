import datetime
#开始日期
datestart = datetime.datetime.strptime('2018-12-5', '%Y-%m-%d')
#截止日期
dateend = datetime.datetime.strptime('2018-12-6', '%Y-%m-%d')

#循环打印日期
while datestart < dateend:
    datestart += datetime.timedelta(days=1)#日期加1
    print(datestart.strftime('%Y%m%d'))#日期格式化
