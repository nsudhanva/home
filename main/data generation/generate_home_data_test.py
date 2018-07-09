# Import necessary libraries
import numpy as np 
import pandas as pd 
import random
import datetime

# Columns of the dataset
labels = ['device', 'room', 'weather_type', 'date', 'from_time', 'to_time', 'no_of_people', 'time_stayed_mins']

# Devices or Home Appliances
devices = ['AC', 'Lights', 'Television', 'Refridgerator', 'Heater', 'Microwave', 'Computer']

# Weather types and conditions
weather_types = ['low cold', 'cold', 'very cold', 'low hot', 'hot', 'very hot']

# Date range with frequency of 1 hour from 1/1/18 to 2/1/18
date_range = pd.date_range(start='1/1/2018', end='2/1/2018', freq='H')

# Date ranges for every devices
devices = [[i] * int(len(date_range) - 1) for i in devices]

# Lists of columns of dataframe
devices_list = []
no_of_people = []
time_stayed_mins = []
from_range = []
to_range = []
rooms = []

people_num = 16
max_time = 60
room_num_start = 100
room_num_end = 120

df = pd.DataFrame(columns=labels)

# Flatten lists of lists into list
flatten = lambda l: [item for sublist in l for item in sublist]

# Generating other datasets
for device in devices:
    no_of_people.append(np.random.randint(0, people_num, len(date_range) - 1))
    time_stayed_mins.append(np.random.randint(0, max_time, len(date_range) - 1))
    from_range.append(date_range[:-1])  
    to_range.append(date_range[1:])    
    devices_list += device
    rooms.append(np.random.randint(room_num_start, room_num_end, len(date_range) - 1))

no_of_people = flatten(no_of_people)
time_stayed_mins = flatten(time_stayed_mins)
from_range = flatten(from_range)
from_range = [i.time() for i in from_range]
to_range = flatten(to_range)
to_range = [i.time() for i in to_range]
rooms = flatten(rooms)  

date_range = np.repeat(date_range[:-1], len(devices))
times = []

for i in from_range:
    if i >= datetime.datetime.strptime('04:00:00', '%H:%M:%S').time() and i < datetime.datetime.strptime('07:00:00', '%H:%M:%S').time():
        times.append('early morning')
    elif i >= datetime.datetime.strptime('07:00:00', '%H:%M:%S').time() and i < datetime.datetime.strptime('12:00:00', '%H:%M:%S').time():
        times.append('morning')
    elif i >= datetime.datetime.strptime('12:00:00', '%H:%M:%S').time() and i < datetime.datetime.strptime('16:00:00', '%H:%M:%S').time():
        times.append('afternoon')
    elif i >= datetime.datetime.strptime('16:00:00', '%H:%M:%S').time() and i < datetime.datetime.strptime('19:00:00', '%H:%M:%S').time():
        times.append('evening')
    elif i >= datetime.datetime.strptime('19:00:00', '%H:%M:%S').time() and i < datetime.datetime.strptime('23:00:00', '%H:%M:%S').time():
        times.append('night')
    else:
        times.append('midnight')

# Create dataframe
df['date'] = date_range.date
df['from_time'] = from_range
df['to_time'] = to_range
df['time_stayed_mins'] = time_stayed_mins
df['no_of_people'] = no_of_people
df['weather_type'] = [random.choice(weather_types) for i in range(len(date_range))]
df['device'] = devices_list
df['time'] = times        
df['room'] = rooms

# Creating random ranges of appliances and their power consumptions
ac = np.arange(1000, 2000)
light = np.arange(1000, 2000)
tv = np.arange(200, 300)
ref = np.arange(100, 300)
heater = np.arange(1500, 3000)
mw = np.arange(1000, 2000)
comp = np.arange(300, 500)

df = df.sort_values(by=['room', 'device', 'date', 'from_time']).reset_index().drop(columns=['index'])
df = df[['device', 'room', 'weather_type', 'date',
       'from_time', 'to_time', 'time', 'no_of_people', 'time_stayed_mins']]

# Remove invalids
weather_types = ['low cold', 'cold', 'very cold', 'low hot', 'hot', 'very hot']

df.loc[df['no_of_people'] == 0, 'time_stayed_mins'] = 0
df.loc[df['time_stayed_mins'] == 0, 'no_of_people'] = 0

# Remove invalid data and NaNs
df = df.fillna(0)

# Converting dataframe into CSV
df.to_csv('../../data/trial_1/home_data_test.csv', index=False)



