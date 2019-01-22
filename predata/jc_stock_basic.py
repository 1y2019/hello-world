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
        df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
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
            sql_insert = "INSERT INTO jc_stock_basic(ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % ( str(resu[0]), str(resu[1]), str(resu[2]), str(resu[3]), str(resu[4]), str(resu[5]), str(resu[6]),str(resu[7]), str(resu[8]), str(resu[9]), str(resu[10]), str(resu[11]), str(resu[12]), str(resu[13]))

            cursor.execute(sql_insert)
            db.commit()
        except Exception as err:
            continue #插入语句执行不成功跳出，执行下一条
    cursor.close()
    db.close()
    print('All Finished!')




