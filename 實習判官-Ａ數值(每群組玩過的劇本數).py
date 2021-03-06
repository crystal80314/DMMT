import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

####import json檔案

data="https://judicial-intern.dmmt.design/api/v1/group_story_ships?fbclid=IwAR0YSAzg_DpezpZSe-cp59oSHuC_yNtKLl-PetnwlLvHqx0p01_IudUrO_I"
raw_df= pd.read_json(data)

df= raw_df.loc[:,["group_id","story_id","created_at"]]

count_story_id= []
count_max_group_id=[]
count=0
line=len(df.index)-1

#A數值分子：計算story_id總數(每行)
while count<= line:  
    count_story_id.append(count)
    count += 1
    
      
#A數值分母：計算group_id總數(每行)

count2=0      
while count2<= line:  
    count_max_group_id.append(df.loc[0:count2,"group_id"].nunique()) 
    count2 += 1  
    



#計算每行的A值

df.loc[:,"count_story_id"]= count_story_id
df.loc[:,"count_max_group_id"]= count_max_group_id


# add array in df
df.loc[:,"num_of_story_per_group"]= df.loc[:,"count_story_id"]/df.loc[:,"count_max_group_id"]
df= df.loc[:,["created_at","num_of_story_per_group"]]

#### 繪圖 A值

x = df.loc[:,"created_at"].dt.date
y = df.loc[:,"num_of_story_per_group"]

plt.plot(x,y,color="r",label="num_of_story_per_group")
plt.ylabel('num_of_story_per_group')
plt.xlabel('created_at')
plt.title('num of story per group')

plt.show()
