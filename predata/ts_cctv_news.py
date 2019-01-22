import  tushare as ts
import logging

fdate='20181216'
pro = ts.pro_api()
df = pro.cctv_news(date=fdate)
df.to_csv(r'D:\python学习\金融数据\news\cctv_news'+fdate+'.csv', sep=',', header=True, index=True,encoding='utf_8_sig')
print(df)