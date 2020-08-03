import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

#import json檔案
data="https://judicial-intern.dmmt.design/api/v1/group_story_ships?fbclid=IwAR0YSAzg_DpezpZSe-cp59oSHuC_yNtKLl-PetnwlLvHqx0p01_IudUrO_I"
raw_df= pd.read_json(data)

#### 計算證人率,證物率

df=raw_df.loc[:,["created_at","story_id","related_ids","exhibit_ids"]]

#計算related_ids每行個數

n=0
related_count=[]
exhibit_count=[]
line=len(df.index)-1

while n<= line:
    count=len(df.loc[n,"related_ids"])-len(df.loc[n,"related_ids"].replace(",",""))+1
    count2=len(df.loc[n,"exhibit_ids"])-len(df.loc[n,"exhibit_ids"].replace(",",""))+1
    related_count.append(count)
    exhibit_count.append(count2)
    n += 1
           
# add array in df
df.loc[:,"related_count"]=related_count
df.loc[:,"exhibit_count"]=exhibit_count


#新增劇本related_rate/exhibit_rate

m=0
related_rate=[]
exhibit_rate=[]

# 證物證人總數 by劇本
related_all=[6,3,5,5,4]
exhibit_all=[13,7,21,28,18]


while m <= line :
    if df.loc[m,"story_id"]== 1:
        rate = df.loc[m,"related_count"]/related_all[0]
        rate2 = df.loc[m,"exhibit_count"]/exhibit_all[0]
        related_rate.append(rate)
        exhibit_rate.append(rate2)
        m += 1
    elif df.loc[m,"story_id"]== 2:
        rate = df.loc[m,"related_count"]/related_all[1]
        rate2 = df.loc[m,"exhibit_count"]/exhibit_all[1]
        related_rate.append(rate)
        exhibit_rate.append(rate2)
        m += 1 
    elif df.loc[m,"story_id"]== 3:
        rate = df.loc[m,"related_count"]/related_all[2]
        rate2 = df.loc[m,"exhibit_count"]/exhibit_all[2]
        related_rate.append(rate)
        exhibit_rate.append(rate2)
        m += 1 
    elif df.loc[m,"story_id"]== 6:
        rate = df.loc[m,"related_count"]/related_all[3]
        rate2 = df.loc[m,"exhibit_count"]/exhibit_all[3]
        related_rate.append(rate)
        exhibit_rate.append(rate2)
        m += 1 
    elif df.loc[m,"story_id"]== 7:
        rate = df.loc[m,"related_count"]/related_all[4]
        rate2 = df.loc[m,"exhibit_count"]/exhibit_all[4]
        related_rate.append(rate)
        exhibit_rate.append(rate2)
        m += 1     
    else:
        break        

# add array in df
df.loc[:,"related_rate"]= related_rate
df.loc[:,"exhibit_rate"]= exhibit_rate




# 整理df資料
df = df.loc[:,["created_at","story_id","related_rate","exhibit_rate"]]

#Convert datetime to date 
df.loc[:,"created_at"]= df.loc[:,"created_at"].dt.week


#### 計算 by劇本

story1 = df[df.loc[:,"story_id"]==1]
story2 = df[df.loc[:,"story_id"]==2]
story3 = df[df.loc[:,"story_id"]==3]
story6 = df[df.loc[:,"story_id"]==6]
story7 = df[df.loc[:,"story_id"]==7]

#Group data by created_at by date

df_yall=df.groupby(["created_at"]).mean()
df_yall= df_yall.loc[:,["related_rate"]]

df_y1=story1.groupby(["created_at"]).mean()
df_y1= df_y1.loc[:,["related_rate"]]
df_y2=story2.groupby(["created_at"]).mean()    
df_y2= df_y2.loc[:,["related_rate"]]
df_y3=story3.groupby(["created_at"]).mean() 
df_y3= df_y3.loc[:,["related_rate"]]
df_y6=story6.groupby(["created_at"]).mean()   
df_y6= df_y6.loc[:,["related_rate"]]
df_y7=story7.groupby(["created_at"]).mean()   
df_y7= df_y7.loc[:,["related_rate"]]

df_xall=df_yall.index
df_x1=df_y1.index
df_x2=df_y2.index
df_x3=df_y3.index
df_x6=df_y6.index
df_x7=df_y7.index

####### 處理data成每週累計資料 ##########



#################繪製證人率折線圖 ##########################


plt.plot(df_x1,df_y1,color="r",label="Story 1")
plt.plot(df_x2,df_y2,"b",label="Story 2")
plt.plot(df_x3,df_y3,"g",label="Story 3")
plt.plot(df_x6,df_y6,"y",label="Story 6")
plt.plot(df_x7,df_y7,"orange",label="Story 7")
plt.plot(df_xall,df_yall,"ko",label="Story all")    

plt.ylabel('related rate')
plt.xlabel('created_at/ week')
plt.title('related rate by story')

plt.legend()
plt.show()


#################繪製證物率折線圖 ##########################



df_yall=df.groupby(["created_at"]).mean()
df_y1=story1.groupby(["created_at"]).mean()
df_y2=story2.groupby(["created_at"]).mean()    
df_y3=story3.groupby(["created_at"]).mean() 
df_y6=story6.groupby(["created_at"]).mean()
df_y7=story7.groupby(["created_at"]).mean()


df_yall= df_yall.loc[:,["exhibit_rate"]]
df_y1= df_y1.loc[:,["exhibit_rate"]]   
df_y2= df_y2.loc[:,["exhibit_rate"]] 
df_y3= df_y3.loc[:,["exhibit_rate"]] 
df_y6= df_y6.loc[:,["exhibit_rate"]]
df_y7= df_y7.loc[:,["exhibit_rate"]]

plt.plot(df_x1,df_y1,color="r",label="Story 1")
plt.plot(df_x2,df_y2,"b",label="Story 2")
plt.plot(df_x3,df_y3,"g",label="Story 3")
plt.plot(df_x6,df_y6,"y",label="Story 6")
plt.plot(df_x7,df_y7,"orange",label="Story 7")
plt.plot(df_xall,df_yall,"ko",label="Story all")    

plt.ylabel('exhibit rate')
plt.xlabel('created_at/ week')
plt.title('exhibit rate by story')

plt.legend()
plt.show()
