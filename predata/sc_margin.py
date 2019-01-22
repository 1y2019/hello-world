import datetime
import tushare as ts
import pymysql
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=r'D:\log\logging.log',
                    filemode='a')

#TuShare + MySql
#获取指定股票数据行情插入数据表
if __name__ == '__main__':

    # 设置tushare pro的token并获取连接,第一次是需要设置
    #ts.set_token('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    pro = ts.pro_api()

    # 建立数据库连接,剔除已入库的部分
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='pydb', charset='utf8')
    cursor = db.cursor()

    # 开始日期
    datestart = datetime.datetime.strptime('2010-12-31', '%Y-%m-%d')
    # 截止日期
    dateend = datetime.datetime.strptime('2013-12-31', '%Y-%m-%d')

    num=0 #记录条数
    errnum=0#异常记录
    # 循环打印日期
    while datestart < dateend:
        try:
            datestart += datetime.timedelta(days=1)  # 日期加1
            fdate=datestart.strftime('%Y%m%d')
            time.sleep(1)  # 暂停 1 秒
            df = pro.margin(trade_date=str(fdate), fields='trade_date,exchange_id,rzye,rzmre,rzche,rqye,rqmcl,rzrqye')
            # 打印进度
            print('Date: ', fdate)
            c_len = df.shape[0]
        except Exception as aa:
            print(aa)
            print('No DATA Code: ' + datestart)
            continue
        for j in range(c_len):
            resu0 = list(df.loc[c_len-1-j])
            resu = []
            for k in range(len(resu0)):
                if str(resu0[k]) == 'nan':
                    resu.append(-1)
                else:
                    resu.append(resu0[k])
            try:
                sql_insert = "INSERT INTO sc_margin(trade_date,exchange_id,rzye,rzmre,rzche,rqye,rqmcl,rzrqye) " \
                             "VALUES('%s','%s','%.2f','%.2f','%.2f','%.2f','%.2f','%.2f') " \
                             % (str(resu[0]), str(resu[1]),float(resu[2]),float(resu[3]),float(resu[4]),float(resu[5]),float(resu[6]),float(resu[7]))
                cursor.execute(sql_insert)
                db.commit()
                num=num+1
            except Exception as err:
                print(err)
                errnum=errnum+1
                logging.error(err+sql_insert)
                continue #插入语句执行不成功跳出，执行下一条
    cursor.close()
    db.close()
    print('errer:', errnum)
    print('All Finished!',num)


