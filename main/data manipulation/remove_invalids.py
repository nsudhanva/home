# Home Appliances Data
import numpy as np
import pandas as pd

# Import Dataset
df = pd.read_csv('../../data/home_data.csv')
        
df.loc[df['no_of_people'] == 0, 'time_stayed_mins'] = 0
df.loc[df['time_stayed_mins'] == 0, 'no_of_people'] = 0       

# Remove invalid data and NaNs
df = df.fillna(0)
df.to_csv('../../data/home_data.csv', index=False)