import datetime
import tushare as ts
import pymysql

#TuShare + MySql
#获取指定股票数据行情插入数据表
if __name__ == '__main__':

    # 设置tushare pro的token并获取连接,第一次是需要设置
    #ts.set_token('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    pro = ts.pro_api()
    # 建立数据库连接,剔除已入库的部分
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='pydb', charset='utf8')
    cursor = db.cursor()
    # 设定需要获取数据的市场池
    stock_pool = ['SSE']#交易所 SSE上交所 SZSE深交所
    total = len(stock_pool)
    # 循环获取单个股票的日线行情
    for i in range(len(stock_pool)):
        try:
            # 获取各大交易所交易日历数据,默认提取的是上交所
            df=pro.trade_cal(exchange='', start_date='20190101', end_date='20191231')
            # 打印进度
            print('Seq: ' + str(i+1) + ' of ' + str(total) + '   Code: ' + str(stock_pool[i]))
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
            try:
                sql_insert = "INSERT INTO jc_trade_cal(exchange,cal_date,is_open) VALUES('%s', '%s', '%i') " % (str(resu[0]), str(resu[1]), int(resu[2]))
                cursor.execute(sql_insert)
                db.commit()
            except Exception as err:
                continue #插入语句执行不成功跳出，执行下一条
    cursor.close()
    db.close()
    print('All Finished!')








