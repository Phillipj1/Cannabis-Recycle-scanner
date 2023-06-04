import pandas as pd
import os
import numpy as np
#data counts the compostable/recycled martial
weed = pd.read_csv("weeddata(2).csv",)
df = pd.DataFrame(weed)

start = df['Recycles']
threshold = 4

#print(start)

scanned = True

#If scanned == true, update df
def recycle_scan():
    if (scanned == True):
        recycles = df['Recycles']+1
        df.update(recycles)
        df['Status'] = np.where(df['Recycles'] >= 4, 'compost', 'recycle')
        
        save_csv(df)
#The system offers scalabily, solutions to record where the martrail goes once it brought
def save_csv(final_df):
    os.makedirs('/Users/phillipj/Desktop/cannihack2023', exist_ok=True)  
    final_df.to_csv(index=False) 
    df.to_csv('/Users/phillipj/Desktop/weeddata(2).csv')     

recycle_scan()
#with the scanner I created it provides that Missing standard of not having consistent naming of prouduct categories 
file_path = 'weeddata.csv'

file = open(file_path,'r')

content = file.read()

file.close

print(content)