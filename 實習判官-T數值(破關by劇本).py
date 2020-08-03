import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

####import json檔案

data="https://judicial-intern.dmmt.design/api/v1/group_story_ships?fbclid=IwAR0YSAzg_DpezpZSe-cp59oSHuC_yNtKLl-PetnwlLvHqx0p01_IudUrO_I"
raw_df= pd.read_json(data)


####計算各個劇本破關率##########

#計算Story1的破關率
df1= raw_df.loc[raw_df.story_id ==1]
df2=df1.loc[raw_df.solve ==True]

#count Total T, 破關 
story1_all=df1["solve"].count
story1_True=df2["solve"].count

number_of_rows_df1 = len(df1)
number_of_rows_df2 = len(df2)

#print(number_of_rows_df2/number_of_rows_df1)

#計算Story2的破關率
df3=raw_df.loc[raw_df.story_id ==2]
df4=df3.loc[raw_df.solve ==True]

#count Total T, 破關 
story2_all=df3["solve"].count
story2_True=df4["solve"].count

number_of_rows_df3 = len(df3)
number_of_rows_df4 = len(df4)

#print(number_of_rows_df4/number_of_rows_df3)

#計算Story3的破關率
df5=raw_df.loc[raw_df.story_id ==3]
df6=df5.loc[raw_df.solve ==True]

#count Total T, 破關 
story3_all=df5["solve"].count
story3_True=df6["solve"].count

number_of_rows_df5 = len(df5)
number_of_rows_df6 = len(df6)

#print(number_of_rows_df6/number_of_rows_df5)

#計算Story6的破關率
df7=raw_df.loc[raw_df.story_id ==6]
df8=df7.loc[raw_df.solve ==True]

#count Total T, 破關 
story6_all=df7["solve"].count
story6_True=df8["solve"].count

number_of_rows_df7 = len(df7)
number_of_rows_df8 = len(df8)

#print(number_of_rows_df8/number_of_rows_df7)

#print(df2)

date= df1.loc[:,"created_at"]


#################整理 破關率dataframe by 劇本,時間,每日破關百分比##########################

# Create new dataframe used to calculate 破關率
df=raw_df.loc[:,["story_id","created_at","solve"]]

# Transfer "solve" column from boolean to value
df.loc[:,"solve"] =df.loc[:,"solve"].astype(int)


#Convert datetime to date 
df.loc[:,"created_at"]= df.loc[:,"created_at"].dt.week


#Seperate story data
story1 = df[df.loc[:,"story_id"]==1]
story2 = df[df.loc[:,"story_id"]==2]
story3 = df[df.loc[:,"story_id"]==3]
story6 = df[df.loc[:,"story_id"]==6]
story7 = df[df.loc[:,"story_id"]==7]


#Group data by created_at by date
df_yall=df.groupby(["created_at"]).mean()
df_yall= df_yall.loc[:,["solve"]]

df_y1=story1.groupby(["created_at"]).mean()
df_y1= df_y1.loc[:,["solve"]]
df_y2=story2.groupby(["created_at"]).mean()    
df_y2= df_y2.loc[:,["solve"]]
df_y3=story3.groupby(["created_at"]).mean() 
df_y3= df_y3.loc[:,["solve"]]
df_y6=story6.groupby(["created_at"]).mean()   
df_y6= df_y6.loc[:,["solve"]]
df_y7=story7.groupby(["created_at"]).mean()   
df_y7= df_y7.loc[:,["solve"]]

df_xall=df_yall.index
df_x1=df_y1.index
df_x2=df_y2.index
df_x3=df_y3.index
df_x6=df_y6.index
df_x7=df_y7.index
#################繪製破關率折線圖 by 劇本,時間,每日破關率 ##########################


plt.plot(df_x1,df_y1,color="r",label="Story 1")
plt.plot(df_x2,df_y2,"b",label="Story 2")
plt.plot(df_x3,df_y3,"g",label="Story 3")
plt.plot(df_x6,df_y6,"y",label="Story 6")
plt.plot(df_x7,df_y7,"orange",label="Story 7")
plt.plot(df_xall,df_yall,"ko",label="Story all")    

plt.ylabel('solve rate')
plt.xlabel('created_at/ week')
plt.title('solve rate by story')

plt.legend()
plt.show()



