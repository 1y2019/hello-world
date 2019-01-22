import  tushare as ts
import logging
import selenium

fname='300377'
fdate='2018-12-13'

#df = ts.get_tick_data(fname,date='2018-12-12',src='tt' )
#df.head(10)

#当日历史分笔
df = ts.get_today_ticks(fname)
df.head(10)
df.to_csv(r'D:\python学习\金融数据\get_today_ticks'+fname+'_'+fdate+'.csv', sep=',', header=True, index=True,encoding='utf_8_sig')

df = ts.get_realtime_quotes(fname)
df.to_csv(r'D:\python学习\金融数据\get_realtime_quotes'+fname+'_'+fdate+'.csv', sep=',', header=True, index=True,encoding='utf_8_sig')
print(df)
