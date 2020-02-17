# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
test= "testtesttest123213"

import pandas as pd 
src_dir = "C:\\Users\\arthu\\OneDrive\\桌面\\python\\100年 北部空品區\\"
src_file_nm = "\\100年中壢站_20120409.csv"
f = open( src_dir+ src_file_nm )
date = pd.read_csv(f)

date['測項']=='PM2.5' #選測項中的2.5數值
PM25 = date.loc[date['測項']=='PM2.5']  #挑出
copyPM25 = PM25.copy() #製作表格

#date.loc[0:15,'1':'2']

temp = copyPM25 .iloc[:,3:27]#檢視多少行列
stackedPM25 = temp.stack(dropna = False)#校正空值


#接 下來要轉為字串，並把 *等數值去掉
stackedPM25 =stackedPM25.astype(str).copy() 
stackedPM25 = stackedPM25.str.replace('x', '')
stackedPM25 = stackedPM25.str.replace('*', '')
stackedPM25 = stackedPM25.str.replace('#', '')                              
stackedPM25.astype(float).plot() 