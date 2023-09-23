# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:23:01 2023

@author: DELL
"""
import os 
import pandas as pd
import numpy as np
path=os.chdir('E:\python\python for data sci')
busnes_data=pd.read_csv("test.csv")
busnes_data=pd.read_csv("test.csv",index_col=5)
#copy
busnes_data1=busnes_data.copy(deep=False)

#get column
COL=busnes_data1.columns
print(COL)

#size of data frem
size=busnes_data1.size
print(size)

#shape of dataframe
frame=busnes_data1.shape
print(frame)

#memory usage
use=busnes_data1.memory_usage()
print(use)
print("--------------------------")

#Array dimensions
dimensions=busnes_data1.ndim
print(dimensions);

#head first five column 
head=busnes_data1.head(6)
print(head);

#last 5 rows
teil=busnes_data1.tail()
print(teil);

#gain value using index number and colummn name
#gain=busnes_data1.at['H01',"year"];
#print(gain);

#gain value using row number and column number
#num=busnes_data1.iat[4,4];

# crette grup
#num1=busnes_data1.loc[:,'year']
#print(num1);

#find each colum
dtype=busnes_data1.dtypes
print(dtype)

#grip use of datatype
#gdt=busnes_data1.get_dtype_counts()
#print(gdt)

#Pint csv file
print(busnes_data1)

#select the data acoding to datatype
#dt=busnes_data1.select_dtype(exclude=[object])

#info aboutb datafrem
name=busnes_data1.info();
print(name);

#gain unique value
uniq=np.unique(busnes_data1['year'])
print(uniq);
