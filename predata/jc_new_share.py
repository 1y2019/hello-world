import datetime
import tushare as ts
import pymysql

#TuShare + MySql
#获取指定股票数据行情插入数据表
if __name__ == '__main__':

    # 设置tushare pro的token并获取连接,第一次是需要设置
    #ts.set_token('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    pro = ts.pro_api()
    # 设定获取日线行情的初始日期和终止日期，其中终止日期设定为昨天。
    # 建立数据库连接,剔除已入库的部分
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='pydb', charset='utf8')
    cursor = db.cursor()
    # 循环获取单个股票的日线行情
    try:
        #获取股票行情数据
        #df = pro.daily(ts_code=stock_pool[i], start_date=start_dt, end_date=end_dt)
        df = pro.new_share(start_date='20150101', end_date='20151231')
        c_len = df.shape[0]
    except Exception as aa:
        print(aa)
    for j in range(c_len):
        resu0 = list(df.loc[c_len-1-j])
        resu = []
        for k in range(len(resu0)):
            if str(resu0[k]) == 'nan':
                resu.append(-1)
            else:
                resu.append(resu0[k])
        try:
            sql_insert = "INSERT INTO jc_new_share(ts_code,sub_code,name,ipo_date,issue_date,amount,market_amount,price,pe,limit_amount,funds,ballot) VALUES ('%s', '%s', '%s', '%s', '%s', '%.2f', '%.2f', '%.2f', '%.2f', '%.2f', '%.2f', '%.2f') " % (str(resu[0]), str(resu[1]), str(resu[2]), str(resu[3]), str(resu[4]), float(resu[5]), float(resu[6]),float(resu[7]), float(resu[8]), float(resu[9]), float(resu[10]), float(resu[11]))
            cursor.execute(sql_insert)
            db.commit()
        except Exception as err:
            continue #插入语句执行不成功跳出，执行下一条
    cursor.close()
    db.close()
    print('All Finished!')




