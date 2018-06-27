# Home Appliances Data
import numpy as np
import pandas as pd
import pdb
import matplotlib.pyplot as plt
import ast

# Import Dataset
df = pd.read_csv('../data/home_data.csv')

df_devices = df.groupby(['from_time', 'device', 'type']).mean()['power']

from_times = df['from_time'].unique()
devices = df['device'].unique()
types = df['type'].unique()

dd = {}
types_dict = {}
devices_dict = {}
from_times_dict = {} 

num = []

for i in types:
    types_dict[i] = num.copy()

for j in devices:
    devices_dict[j] = types_dict.copy()

for k in from_times:
    from_times_dict[k] = devices_dict.copy()
    
dd = from_times_dict.copy()

mean_list = []
mean_dict = {}

i = -1
for time, app in dd.items():
#     print(time, app)
    for appl, typ in app.items():
#         print(typ)
#         print(typ['indoor'], typ['outdoor'])
        typ['indoor'] = df_devices[i + 1].copy()
        typ['outdoor'] = df_devices[i + 2].copy()
#         print(df_devices[i + 1], df_devices[i + 2], i)
        i += 2
#         print(typ)
    print(dd[time])
    mean_list.append(dd[time].copy())
