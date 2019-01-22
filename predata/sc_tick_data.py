import datetime
import time
import tushare as ts
import pymysql
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=r'D:\log\logging.log',
                    filemode='a')

#TuShare + MySql
#获取指定股票数据行情插入数据表
if __name__ == '__main__':

    # 建立数据库连接,剔除已入库的部分
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='pydb', charset='utf8')
    cursor = db.cursor()

    # 开始日期
    datestart = datetime.datetime.strptime('2018-12-11', '%Y-%m-%d')
    # 截止日期
    dateend = datetime.datetime.strptime('2018-12-14', '%Y-%m-%d')

    num=0 #记录条数
    errnum=0#异常记录

    # 设定需要获取数据的股票池
    stock_pool = ['300377']
    total = len(stock_pool)
    # 循环获取单个股票的日线行情
    for i in range(len(stock_pool)):
        # 循环打印日期
        while datestart < dateend:
            try:
                '''
                获取当前交易日（交易进行中使用）已经产生的分笔明细数据。
                参数说明：
                code：股票代码，即6位数字代码
                retry_count: int, 默认3, 如遇网络等问题重复执行的次数
                pause: int, 默认0, 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
               '''
                fcode=stock_pool[i]
                datestart += datetime.timedelta(days=1)  # 日期加1
                fdate = datestart.strftime('%Y-%m-%d')
                df = ts.get_tick_data(fcode,date=fdate,src='tt' )
                df.head(10)
                df.to_csv(r'D:\python学习\金融数据\get_' + fcode + '_' + fdate + '.csv', sep=',', header=True,index=True, encoding='utf_8_sig')

                # 打印进度
                print('Seq: ' + str(i+1) + ' of ' + str(total) + '   Code: ' + str(fcode)+ '   Date: ' + str(fdate))
                c_len = df.shape[0]
            except Exception as aa:
                print(aa)
                print('No DATA Code: ' + str(i))
                continue


            for j in range(c_len):
                resu0 = list(df.loc[c_len-1-j])
                resu = []
                for k in range(len(resu0)):
                    if str(resu0[k]) == 'nan':
                        resu.append(-1)
                    else:
                        resu.append(resu0[k])
                #state_dt = (datetime.datetime.strptime(resu[1], "%Y%m%d")).strftime('%Y-%m-%d')
                try:
                    sql_insert = "INSERT INTO sc_tick_data(symbol,trade_date,time,price,pchange,pchg,volume,amount,type) " \
                                 "VALUES('%s','%s','%s','%.2f','%.2f','%.2f','%.2f','%.2f','%s') " \
                                 % (fcode,fdate,str(resu[0]), float(resu[1]),float(0.00),float(resu[2]),float(resu[3]),float(resu[4]),str(resu[5]))

                    cursor.execute(sql_insert)
                    db.commit()
                    num = num + 1
                except Exception as err:
                    errnum = errnum + 1
                    print(err)
                    logging.error(sql_insert)
                    continue #插入语句执行不成功跳出，执行下一条

    cursor.close()
    db.close()
    print('errer:', errnum)
    print('All Finished!', num)

