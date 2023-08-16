#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:12:06 2019

@author: javiermedina
"""

import pandas as pd

def header(msg):
    print ('-' * 45)
    print ('[ ' + msg + ' ]')
    
# 2. Load CSV data into df


header("2. load csv dagta into a df")
filename = 'my_data_source.csv'
df = pd.read_csv(filename)
#print(df)


# 3. Load CSV data into df
header("3. load csv data into a df - Head")
#filename = 'source_data.txt'
#df = pd.read_csv(filename)
print (df.head())


# 5. Load CSV data into df
header("5. load csv data into a df - Tail")
#filename = 'source_data.txt'
#df = pd.read_csv(filename)
print (df.tail())

# 6. Load CSV data into df
header("6. load csv data into a df - dtypes")
#filename = 'source_data.txt'
#df = pd.read_csv(filename)
print (df.dtypes)

# 7. Load CSV data into df
header("7. load csv data into a df - index")
#filename = 'source_data.txt'
#df = pd.read_csv(filename)
print (df.index)

# 8. Load CSV data into df
header("8. load csv data into a df - columns")
#filename = 'source_data.txt'
#df = pd.read_csv(filename)
print (df.columns)

# 10. Load CSV data into df
header('10. load csv data into a df - Slice')
#filename = 'source_data.txt'
#df = pd.read_csv(filename)
print (df.iloc[1:5,[1,4,10,11,12,13,14]])

# 11. Load CSV data into df
header('11. load csv data into a df - Slice')
#filename = 'source_data.txt'
#df = pd.read_csv(filename)
#df = df.head(1000)
#df.to_csv('my_data_source.csv')



