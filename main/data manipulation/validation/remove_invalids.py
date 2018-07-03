# Home Appliances Data
import numpy as np
import pandas as pd
import random

# Import Dataset
df = pd.read_csv('../../data/home_data.csv')
weather_types = ['low cold', 'cold', 'very cold', 'low hot', 'hot', 'very hot']

df.loc[df['no_of_people'] == 0, 'time_stayed_mins'] = 0
df.loc[df['time_stayed_mins'] == 0, 'no_of_people'] = 0

for i in range(1, 11):    
    df.loc[df['building'] == i, 'weather_type'] = random.choice(weather_types)

# Remove invalid data and NaNs
df = df.fillna(0)
df.to_csv('../../data/home_data.csv', index=False)