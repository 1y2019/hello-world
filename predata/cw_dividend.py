import datetime
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

    # 设置tushare pro的token并获取连接,第一次是需要设置
    #ts.set_token('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    pro = ts.pro_api()

    # 建立数据库连接,剔除已入库的部分
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='pydb', charset='utf8')
    cursor = db.cursor()

    # 设定需要获取数据的股票池
    #stocklist = pro.stock_basic(exchange='', list_status='L',fields='ts_code')
    #stock_pool =stocklist['ts_code'].tolist()
    stock_pool =['000088.SZ']

    #print(stock_pool)

    total = len(stock_pool)
    # 循环获取单个股票的停牌信息
    for i in range(len(stock_pool)):
        try:
            # 获取分红送股数据
            df = pro.dividend(ts_code=stock_pool[i], fields='ts_code,end_date,ann_date,div_proc,stk_div,stk_bo_rate,stk_co_rate,cash_div,cash_div_tax,record_date,ex_date,pay_date,div_listdate,imp_ann_date')
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
                sql_insert = "INSERT INTO cw_dividend(ts_code,end_date,ann_date,div_proc,stk_div,stk_bo_rate,stk_co_rate,cash_div,cash_div_tax,record_date,ex_date,pay_date,div_listdate,imp_ann_date) " \
                             "VALUES('%s','%s','%s','%s','%.2f','%.2f','%.2f','%.2f','%.2f','%s','%s','%s','%s','%s') " \
                             % (str(resu[0]), str(resu[1]), str(resu[2]), str(resu[3]), float(resu[4]), float(resu[5]), float(resu[6]), float(resu[7]), float(resu[8]),str(resu[9]), str(resu[10]), str(resu[11]), str(resu[12]), str(resu[13]))
                cursor.execute(sql_insert)
                db.commit()
            except Exception as err:
                print(err)
                #logging.error(err)
                continue #插入语句执行不成功跳出，执行下一条
    cursor.close()
    db.close()
    print('All Finished!')