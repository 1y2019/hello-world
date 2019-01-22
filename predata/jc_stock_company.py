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
    # 设定需要获取数据的股票池
    stock_pool = ['SSE','SZSE']#SSE上交所 SZSE深交所
    total = len(stock_pool)
    # 循环获取单个股票的日线行情
    for i in range(len(stock_pool)):
        try:
            #获取股票行情数据
            #df = pro.daily(ts_code=stock_pool[i], start_date=start_dt, end_date=end_dt)
            df = pro.stock_company(exchange=stock_pool[i],   fields = 'ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope')
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
                sql_insert = "INSERT INTO jc_stock_company(ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope) VALUES('%s', '%s', '%s', '%s', '%s', '%.2f', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%i', '%s', '%s') " %(str(resu[0]), str(resu[1]), str(resu[2]), str(resu[3]), str(resu[4]), float(resu[5]), str(resu[6]),str(resu[7]), str(resu[8]), str(resu[9]), str(resu[10]),str(resu[11]), str(resu[12]), float(resu[13]), str(resu[14]), str(resu[15]))
                cursor.execute(sql_insert)
                db.commit()
            except Exception as err:
                continue #插入语句执行不成功跳出，执行下一条
    cursor.close()
    db.close()
    print('All Finished!')




