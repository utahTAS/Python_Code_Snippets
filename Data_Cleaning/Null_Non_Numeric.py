#############################################################
## This code force strip all non-numeric data and replaces ##
## them with null (np.NaN) values. This code uses an       ##
## example fielfd saved on the 'U:' drive.                 ##
#############################################################


#First, here is short version of the essential code
#-------------------------------------------------------------------------
float_cols=['a','b','c']  #some column names that are in your df

#loop through each column and coerce numeric data. 
#Also fill nan's with zeros
for cols in float_cols:
    df[cols]=df[cols].apply(pd.to_numeric, errors='coerce').fillna(0)



#Full Example
#-----------------------------------------------------------------------------
import pandas as pd
import numpy as np

#this is the file name used in the example
filename='U:/PLAN/BCUBRICH/Python/TestFiles/drop_non_numeric.csv'


#will use these params when we import the df
col_names=['a','b','c']                  #column names to use on imported file
usecols=[1,2,3]                          #columns to use data from
converters={'a':str,'b':int,'c':float}   #data type we ultimately want columns in 
skiprows=1                               #if there is a header line, skip it here, for example.

#read in the df
df=pd.read_csv(filename,names=col_names,usecols=usecols, skiprows=skiprows, dtype=str)

#just want this so we can see what happened to df after we change it
before_df=pd.read_csv(filename,names=col_names,usecols=usecols, skiprows=skiprows, dtype=str)

#column names we need to make sure are floats
#In this case I used all columns, but can be a subset.
float_cols=['a','b','c']  

#loop through each column and coerce numeric data. Also fill nan's with zeros
for cols in float_cols:
    df[cols]=df[cols].apply(pd.to_numeric, errors='coerce').fillna(0)


#If you need other dtypes you can use a dict to do broadcast them like so  
dtype_df=df.astype(dtype=converters)

