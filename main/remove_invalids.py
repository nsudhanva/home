# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:02:29 2018

@author: Sudhanva
"""

# Home Appliances Data
import numpy as np
import pandas as pd

# Import Dataset
df = pd.read_csv('../data/home_data.csv')
        
df.loc[df['no_of_people'] == 0, 'time_stayed_mins'] = 0
df.loc[df['time_stayed_mins'] == 0, 'no_of_people'] = 0       
df = df.fillna(000)
df.to_csv('../data/home_data.csv')