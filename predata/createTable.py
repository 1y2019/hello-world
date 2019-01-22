import mysql.connector
#创建数据库连接
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="pydb"
)
#创建游标
mycursor = mydb.cursor()
#删除表
#mycursor.execute("drop TABLE IF EXISTS stock_all ")


#################################################基础数据################################################################
# 创建数据表语句,创建索引
sql = """CREATE TABLE jc_stock_basic (
         ts_code VARCHAR(20) comment 'TS代码' , 
         symbol VARCHAR(20) comment '股票代码', 
         name VARCHAR (50) comment '股票名称' , 
         area VARCHAR(50) comment '所在地域', 
         industry VARCHAR(50) comment '所属行业' , 
         fullname VARCHAR(50) comment '股票全称', 
         enname VARCHAR(50) comment '英文全称' , 
         market VARCHAR(20) comment '市场类型 （主板/中小板/创业板）', 
         exchange VARCHAR(20) comment '交易所代码', 
         curr_type VARCHAR(20) comment '交易货币', 
         list_status VARCHAR(10) comment '上市状态： L上市 D退市 P暂停上市' , 
         list_date VARCHAR(20) comment '上市日期' , 
         delist_date VARCHAR(20) comment '退市日期', 
         is_hs VARCHAR(10) comment '是否沪深港通标的，N否 H沪股通 S深股通',  
         PRIMARY KEY (ts_code,symbol) 
         ) comment '股票基础信息' """
mycursor.execute(sql)#执行创建语句

# 创建数据表语句,创建索引
sql = """CREATE TABLE jc_trade_cal (
         exchange VARCHAR(20) comment '交易所 SSE上交所 SZSE深交所' , 
         cal_date VARCHAR(20) comment '日历日期', 
         is_open int (5) comment '是否交易 0休市 1交易' , 
         pretrade_date VARCHAR(20) comment '上一个交易日', 
         PRIMARY KEY (exchange,cal_date,is_open) 
         ) comment '交易日历' """
mycursor.execute(sql)#执行创建语句

# 创建数据表语句,创建索引
sql = """CREATE TABLE jc_hs_const (
         ts_code VARCHAR(20) comment 'TS代码' , 
         hs_type VARCHAR(20) comment '沪深港通类型SH沪SZ深', 
         in_date VARCHAR (20) comment '纳入日期' , 
         out_date VARCHAR(20) comment '剔除日期', 
         is_new VARCHAR(5) comment '是否最新 1是0否', 
         PRIMARY KEY (ts_code,hs_type) 
         ) comment '沪深股通成份股' """
mycursor.execute(sql)#执行创建语句


# 创建数据表语句,创建索引
sql = """CREATE TABLE jc_stock_company (
         ts_code VARCHAR(20) comment '股票代码' , 
         exchange VARCHAR(10) comment '交易所代码 ，SSE上交所 SZSE深交所', 
         chairman VARCHAR (20) comment '法人代表' , 
         manager VARCHAR(20) comment '总经理', 
         secretary VARCHAR(20) comment '董秘' , 
         reg_capital decimal (20,4)  comment '注册资本', 
         setup_date VARCHAR(20) comment '注册日期' , 
         province VARCHAR(20) comment '所在省份', 
         city VARCHAR(20) comment '所在城市', 
         introduction VARCHAR(2000) comment '公司介绍', 
         website VARCHAR(50) comment '公司主页' , 
         email VARCHAR(100) comment '电子邮件' , 
         office VARCHAR(200) comment '办公室', 
         employees int(10) comment '员工人数',  
         main_business VARCHAR(2000) comment '主要业务及产品', 
         business_scope VARCHAR(2000) comment '经营范围',  
         PRIMARY KEY (ts_code,exchange) 
         ) comment '上市公司基本信息' """
mycursor.execute(sql)#执行创建语句




# 创建数据表语句,创建索引
sql = """CREATE TABLE jc_namechange (
         ts_code VARCHAR(20) comment 'TS代码' , 
         name VARCHAR(50) comment '证券名称', 
         start_date VARCHAR (20) comment '开始日期' , 
         end_date VARCHAR(20) comment '结束日期', 
         ann_date VARCHAR(20) comment '公告日期', 
         change_reason VARCHAR(200) comment '变更原因', 
         PRIMARY KEY (ts_code) 
         ) comment '股票曾用名' """
mycursor.execute(sql)#执行创建语句


# 创建数据表语句,创建索引
sql = """CREATE TABLE jc_new_share (
         ts_code VARCHAR(20) comment 'TS股票代码' , 
         sub_code VARCHAR(20) comment '申购代码', 
         name VARCHAR (50) comment '名称' , 
         ipo_date VARCHAR(20) comment '上网发行日期', 
         issue_date VARCHAR(20) comment '上市日期' , 
         amount decimal (20,4)  comment '发行总量（万股）', 
         market_amount decimal (20,4)  comment '上网发行总量（万股）' , 
         price decimal (20,4)  comment '发行价格', 
         pe decimal (20,4)  comment '市盈率', 
         limit_amount decimal (20,4)  comment '个人申购上限（万股）', 
         funds decimal (20,4)  comment '募集资金（亿元）' , 
         ballot decimal (20,4)  comment '中签率' , 
         PRIMARY KEY (ts_code,sub_code) 
         ) comment 'IPO新股列表' """
mycursor.execute(sql)#执行创建语句



######################################行情数据####################################################
# 创建数据表语句,创建索引
sql = """CREATE TABLE hq_stock_all (
         ts_code VARCHAR(20) comment '股票代码' , 
         trade_date VARCHAR(20) comment '交易日期', 
         open decimal (20,4) comment '开盘价' , 
         high decimal(20,4) comment '最高价', 
         low decimal(20,4) comment '最高价' , 
         close decimal(20,4) comment '收盘价', 
         pre_close decimal(20,4) comment '昨收价' , 
         pct_change decimal(20,4) comment '涨跌额', 
         pct_chg decimal(20,4) comment '涨跌幅', 
         vol int(30) comment '成交量 （手）', 
         amount decimal(20,4) comment '成交额 （千元）' , 
         PRIMARY KEY (ts_code,trade_date) 
         ) comment '股票行情数据' """
mycursor.execute(sql)#执行创建语句

# 创建数据表语句,创建索引
sql = """CREATE TABLE hq_stock_weekly (
         ts_code VARCHAR(20) comment '股票代码' , 
         trade_date VARCHAR(20) comment '交易日期', 
         open decimal (20,4) comment '周开盘价' , 
         high decimal(20,4) comment '周最高价', 
         low decimal(20,4) comment '周最低价' , 
         close decimal(20,4) comment '周收盘价', 
         pre_close decimal(20,4) comment '上一周收盘价' , 
         pct_change decimal(20,4) comment '周涨跌额', 
         pct_chg decimal(20,4) comment '周涨跌幅', 
         vol int(30) comment '周成交量', 
         amount decimal(20,4) comment '周成交额' , 
         PRIMARY KEY (ts_code,trade_date) 
         ) comment '周线行情' """
mycursor.execute(sql)#执行创建语句


# 创建数据表语句,创建索引
sql = """CREATE TABLE hq_stock_monthly (
         ts_code VARCHAR(20) comment '股票代码' , 
         trade_date VARCHAR(20) comment '交易日期', 
         open decimal (20,4) comment '月开盘价' , 
         high decimal(20,4) comment '月最高价', 
         low decimal(20,4) comment '月最低价' , 
         close decimal(20,4) comment '月收盘价', 
         pre_close decimal(20,4) comment '上一月收盘价' , 
         pct_change decimal(20,4) comment '月涨跌额', 
         pct_chg decimal(20,4) comment '月涨跌幅', 
         vol int(30) comment '月成交量', 
         amount decimal(20,2) comment '月成交额' , 
         PRIMARY KEY (ts_code,trade_date) 
         ) comment '月线行情' """
mycursor.execute(sql)#执行创建语句


# 创建数据表语句,创建索引
sql = """CREATE TABLE hq_stock_daily_basic (
         ts_code VARCHAR(20) comment 'TS股票代码' , 
         trade_date VARCHAR(20) comment '交易日期', 
         close  decimal (20,4) comment '当日收盘价' , 
         turnover_rate  decimal (20,4) comment '换手率', 
         turnover_rate_f  decimal (20,4) comment '换手率（自由流通股）' , 
         volume_ratio decimal (20,4)  comment '量比', 
         pe  decimal (20,4) comment '市盈率（总市值/净利润）' , 
         pe_ttm decimal (20,4) comment '市盈率（TTM）', 
         pb  decimal (20,4) comment '市净率（总市值/净资产）', 
         ps  decimal (20,4) comment '市销率', 
         ps_ttm  decimal (20,2) comment '市销率（TTM）' , 
         total_share decimal (20,4) comment '总股本 （万）' , 
         float_share decimal (20,4) comment '流通股本 （万）', 
         free_share decimal (20,4) comment '自由流通股本 （万）',  
         total_mv decimal (20,4) comment '总市值 （万元）', 
         circ_mv decimal (20,4) comment '流通市值（万元）',  
         PRIMARY KEY (ts_code,trade_date) 
         ) comment '每日指标' """
mycursor.execute(sql)#执行创建语句



# 创建数据表语句,创建索引
sql = """CREATE TABLE hq_suspend (
         ts_code VARCHAR(20) comment '股票代码' , 
         suspend_date VARCHAR(20) comment '停牌日期', 
         resume_date VARCHAR (20) comment '复牌日期' , 
         ann_date VARCHAR(20) comment '公告日期', 
         suspend_reason VARCHAR(200) comment '停牌原因', 
         reason_type VARCHAR(100) comment '停牌原因类别', 
         PRIMARY KEY (ts_code,suspend_date) 
         ) comment '停复牌信息' """
mycursor.execute(sql)#执行创建语句


# 创建数据表语句,创建索引
sql = """CREATE TABLE hq_adj_factor (
         ts_code VARCHAR(20) comment '股票代码' , 
         trade_date VARCHAR(20) comment '交易日期', 
         adj_factor  decimal (20,4)  comment '复权因子' , 
         start_date VARCHAR(20) comment '开始日期', 
         end_date VARCHAR(200) comment '结束日期', 
         PRIMARY KEY (ts_code) 
         ) comment '复权因子' """
mycursor.execute(sql)#执行创建语句


##########################################财务数据#############################################
# 创建数据表语句,创建索引
sql = """CREATE TABLE cw_forecast (
         ts_code VARCHAR(20) comment 'TS股票代码' , 
         ann_date VARCHAR(20) comment '公告日期', 
         end_date  VARCHAR(20) comment '报告期' , 
         type  VARCHAR(20) comment '业绩预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减)', 
         p_change_min  decimal (20,4) comment '预告净利润变动幅度下限（%）' , 
         p_change_max decimal (20,4)  comment '预告净利润变动幅度上限（%）', 
         net_profit_min  decimal (20,4) comment '预告净利润下限（万元）' , 
         net_profit_max decimal (20,4) comment '预告净利润上限（万元）', 
         last_parent_net  decimal (20,4) comment '上年同期归属母公司净利润', 
         first_ann_date  VARCHAR(20) comment '首次公告日', 
         summary  VARCHAR(20) comment '业绩预告摘要' , 
         change_reason VARCHAR(20) comment '业绩变动原因' , 
         PRIMARY KEY (ts_code,ann_date) 
         ) comment '业绩预告' """
mycursor.execute(sql)#执行创建语句


# 创建数据表语句,创建索引
sql = """CREATE TABLE cw_dividend (
         ts_code VARCHAR(20) comment 'TS代码' , 
         end_date VARCHAR(20) comment '分红年度', 
         ann_date  VARCHAR(20) comment '预案公告日' , 
         div_proc  VARCHAR(20) comment '实施进度', 
         stk_div  decimal (20,4) comment '每股送转' , 
         stk_bo_rate decimal (20,4)  comment '每股送股比例', 
         stk_co_rate  decimal (20,4) comment '每股转增比例' , 
         cash_div decimal (20,4) comment '每股分红（税后）', 
         cash_div_tax  decimal (20,4) comment '每股分红（税前）', 
         record_date  VARCHAR(20) comment '股权登记日', 
         ex_date  VARCHAR(20) comment '除权除息日' , 
         pay_date VARCHAR(20) comment '派息日' , 
         div_listdate VARCHAR(20) comment '红股上市日' , 
         imp_ann_date VARCHAR(20) comment '实施公告日' , 
         base_date VARCHAR(20) comment '基准日' , 
         base_share  decimal (20,4) comment '基准股本（万）' , 
         PRIMARY KEY (ts_code,ann_date) 
         ) comment '分红送股' """
mycursor.execute(sql)#执行创建语句


# 创建数据表语句,创建索引
sql = """CREATE TABLE cw_fina_audit (
         ts_code VARCHAR(20) comment 'TS股票代码' , 
         ann_date VARCHAR(20) comment '公告日期', 
         end_date VARCHAR(20) comment '报告期' , 
         audit_result VARCHAR(200) comment '审计结果', 
         audit_fees decimal (20,4) default 0 comment '审计总费用（元）', 
         audit_agency  VARCHAR(100)  comment '会计事务所' , 
         audit_sign VARCHAR(20) comment '签字会计师', 
         PRIMARY KEY (ts_code,ann_date,end_date) 
         ) comment '财务审计意见' """
mycursor.execute(sql)#执行创建语句

# 创建数据表语句,创建索引
sql = """CREATE TABLE cw_fina_mainbz (
         ts_code VARCHAR(20) comment 'TS代码' , 
         end_date VARCHAR(20) comment '报告期', 
         bz_item VARCHAR(20) comment '主营业务来源' , 
         bz_sales decimal (20,4)  comment '主营业务收入(元)', 
         bz_profit decimal (20,4) default 0 comment '主营业务利润(元)', 
         bz_cost  decimal (20,4)  comment '主营业务成本(元)' , 
         curr_type VARCHAR(10) comment '货币代码', 
         update_flag VARCHAR(10) comment '是否更新',          
         PRIMARY KEY (ts_code,end_date,bz_item) 
         ) comment '主营业务构成' """
mycursor.execute(sql)#执行创建语句


#########################市场参考数据############################
# 创建数据表语句,创建索引
sql = """CREATE TABLE sc_moneyflow_hsgt (
         trade_date VARCHAR(20) comment '交易日期' , 
         ggt_ss decimal (20,4) comment '港股通（上海）', 
         ggt_sz decimal (20,4) comment '港股通（深圳）' , 
         hgt decimal (20,4)  comment '沪股通（百万元）', 
         sgt decimal (20,4) default 0 comment '深股通（百万元）', 
         north_money decimal (20,4)  comment '北向资金（百万元）' , 
         south_money decimal (20,4) comment '南向资金（百万元）',       
         PRIMARY KEY (trade_date) 
         ) comment '沪深港通资金流向' """
mycursor.execute(sql)#执行创建语句


# 创建数据表语句,创建索引
sql = """CREATE TABLE sc_repurchase (
         ts_code VARCHAR(20) comment 'TS代码' , 
         ann_date VARCHAR(20) comment '公告日期', 
         end_date VARCHAR(20) comment '截止日期' , 
         proc  VARCHAR(20) comment '进度', 
         exp_date  VARCHAR(20)  comment '过期日期', 
         vol decimal (20,4)  comment '回购数量' , 
         amount decimal (20,4) comment '回购金额',     
         high_limit decimal (20,4) default 0 comment '回购最高价', 
         low_limit decimal (20,4)  comment '回购最低价' ,    
         PRIMARY KEY (ts_code,ann_date,end_date) 
         ) comment '股票回购' """
mycursor.execute(sql)#执行创建语句


# 创建数据表语句,创建索引
sql = """CREATE TABLE sc_margin (
         trade_date VARCHAR(20) comment '交易日期' , 
         exchange_id VARCHAR(20) comment '交易所代码（SSE上交所SZSE深交所）', 
         rzye decimal (20,4)  comment '融资余额(元)' , 
         rzmre decimal (20,4)  comment '融资买入额(元)', 
         rzche decimal (20,4)  comment '融资偿还额(元)', 
         rqye decimal (20,4)  comment '融券余额(元)' , 
         rqmcl decimal (20,4) comment '融券卖出量(股,份,手)',     
         rzrqye decimal (20,4) default 0 comment '融资融券余额(元)', 
         PRIMARY KEY (trade_date,exchange_id) 
         ) comment '融资融券交易汇总' """
mycursor.execute(sql)#执行创建语句

# 创建数据表语句,创建索引
sql = """CREATE TABLE sc_margin_detail (
         trade_date VARCHAR(20) comment '交易日期' , 
         ts_code VARCHAR(20) comment 'TS股票代码', 
         rzye decimal (20,4)  comment '融资余额(元)' , 
         rqye decimal (20,4)  comment '融券余额(元)', 
         rzmre decimal (20,4)  comment '融资买入额(元)', 
         rqyl decimal (20,4)  comment '融券余量（手）' , 
         rzche decimal (20,4) comment '融资偿还额(元)',     
         rqchl decimal (20,4) default 0 comment '融券偿还量(手)', 
         rqmcl decimal (20,4) comment '融券卖出量(股,份,手)',     
         rzrqye decimal (20,4) default 0 comment '融资融券余额(元)', 
         PRIMARY KEY (trade_date,ts_code) 
         ) comment '融资融券交易明细' """
mycursor.execute(sql)#执行创建语句


# 创建数据表语句,创建索引
sql = """CREATE TABLE sc_today_ticks (
         symbol VARCHAR(20) comment '股票代码', 
         trade_date VARCHAR(20) comment '交易日期' , 
         time VARCHAR(20) comment '时间' , 
         price decimal (20,4)  comment '当前价格', 
         pchange decimal (20,4)  comment '涨跌幅' , 
         pchg decimal (20,4)  comment '价格变动', 
         volume decimal (20,4)  comment '成交手', 
         amount decimal (20,4)  comment '成交金额(元)' , 
         type VARCHAR(10)  comment '买卖类型【买盘、卖盘、中性盘】',     
         PRIMARY KEY (symbol,trade_date,time) 
         ) comment '当日历史分笔' """
mycursor.execute(sql)#执行创建语句

# 创建数据表语句,创建索引
sql = """CREATE TABLE sc_tick_data (
         symbol VARCHAR(20) comment '股票代码', 
         trade_date VARCHAR(20) comment '交易日期' , 
         time VARCHAR(20) comment '时间' , 
         price decimal (20,4)  comment '当前价格', 
         pchange decimal (20,4)  comment '涨跌幅' , 
         pchg decimal (20,4)  comment '价格变动', 
         volume decimal (20,4)  comment '成交手', 
         amount decimal (20,4)  comment '成交金额(元)' , 
         type VARCHAR(10)  comment '买卖类型【买盘、卖盘、中性盘】',     
         PRIMARY KEY (symbol,trade_date,time) 
         ) comment '获取个股以往交易历史的分笔数据明细' """
mycursor.execute(sql)#执行创建语句

#关闭游标
mycursor.close()
#关闭数据库连接
mydb.close




