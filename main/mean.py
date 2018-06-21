# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 16:35:29 2018

@author: Sudhanva
"""

# Home Appliances Data
import numpy as np
import pandas as pd
import pdb
import matplotlib.pyplot as plt
import ast

df = pd.read_csv('../data/home_data.csv')

df_devices = df.groupby(['from_time', 'device', 'type']).mean()['power']

from_times = df['from_time'].unique()
devices = df['device'].unique()
types = df['type'].unique()

dd = {}
types_dict = {}
devices_dict = {}
from_times_dict = {} 

for i in types:
    types_dict[i] = 0

for j in devices:
    devices_dict[j] = types_dict

for k in from_times:
    from_times_dict[k] = devices_dict
    
dd = from_times_dict

i = -1

for time, app in dd.items():
    for appl, inout in app.items():
        pdb.set_trace()
        inout["indoor"] = df_devices[i+1]
        inout["outdoor"] = df_devices[i+2]
        i += 1
