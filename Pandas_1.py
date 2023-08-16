#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:29:20 2019

@author: javiermedina
"""

#import numpy as np
import pandas as pd

def header(msg):
    print ('-' * 25)
    print ('[ ' + msg + ' ]')
# Load HardCoded data into df
header("1. load hard-coded dagta into a df")  
  
df = pd.DataFrame(
        [['Jan', 58,42,74,22,2.95],
         ['Feb', 61,45,78,26,3.02],
         ['Mar', 65,41,76,21,4.06]],
    index = [0,1,2],
    columns = ['month','avg_high', 'avg_low','record_hihg', 'record_low'
               ,'avg_precip'])
    
print(df)
    