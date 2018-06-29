# Import necessary libraries

import numpy as np 
import pandas as pd 
import random

# Columns of the dataset
labels = ['device',	'building',	'floor', 'room', 'weather_type', 'power', 'date', 'from_time', 'to_time', 'no_of_people', 'time_stayed_mins']
devices = ['AC', 'Lights', 'Television', 'Refridgerator', 'Heater', 'Microwave', 'Computer']
weather_types = ['low cold', 'cold', 'very cold', 'low hot', 'hot', 'very hot']
date_range = pd.date_range(start='1/1/2018', end='2/1/2018', freq='H')
devices = [[i] * int(len(date_range) - 1) for i in devices]

# Lists of columns of dataframe
devices_list = []
no_of_people = []
time_stayed_mins = []
buildings = []
floors = []
from_range = []
to_range = []

df = pd.DataFrame(columns=labels)

# Flatten lists of lists into list
flatten = lambda l: [item for sublist in l for item in sublist]

for device in devices:
    no_of_people.append(np.random.randint(0, 11, len(date_range) - 1))
    time_stayed_mins.append(np.random.randint(0, 31, len(date_range) - 1))
    buildings.append(np.random.randint(1, 4, len(date_range) - 1))
    floors.append(np.random.randint(1, 11, len(date_range) - 1))
    from_range.append(date_range[:-1])
    to_range.append(date_range[1:])
    
for i in devices:
    devices_list += i

no_of_people = flatten(no_of_people)
time_stayed_mins = flatten(time_stayed_mins)
buildings = flatten(buildings)
floors = flatten(floors)
from_range = flatten(from_range)
from_range = [i.time() for i in from_range]
to_range = flatten(to_range)
to_range = [i.time() for i in to_range]
  
date_range = np.repeat(date_range[:-1], len(devices))

# Create dataframe
df['building'] = buildings
df['floor'] = floors
df['date'] = date_range.date
df['from_time'] = from_range
df['to_time'] = to_range
df['time_stayed_mins'] = time_stayed_mins
df['no_of_people'] = no_of_people
df['weather_type'] = [random.choice(weather_types) for i in range(len(date_range))]
df['device'] = devices_list

rooms = []
for index, value in enumerate(floors):
    rooms.append((floors[index] * 100) + random.randint(1, 7))
        
df['room'] = rooms

# Creating random ranges of appliances and their power consumptions
ac = np.arange(1000, 2000)
light = np.arange(1000, 2000)
tv = np.arange(200, 300)
ref = np.arange(100, 300)
heater = np.arange(1500, 3000)
mw = np.arange(1000, 2000)
comp = np.arange(300, 500)

# Creating power consumption data 
powers = []

for dev, typ in zip(df['device'], df['weather_type']):
    if dev == 'AC':
        powers.append(random.choice(ac))
    elif dev == 'Lights':
        powers.append(random.choice(light))
    elif dev == 'Television':
        powers.append(random.choice(tv))    
    elif dev == 'Refridgerator':
        powers.append(random.choice(ref))    
    elif dev == 'Heater':
        powers.append(random.choice(heater))    
    elif dev == 'Microwave':
        powers.append(random.choice(mw))    
    elif dev == 'Computer':
        powers.append(random.choice(comp))    

df['power'] = powers
df = df.sort_values(by=['building', 'floor', 'room', 'device', 'date', 'from_time']).reset_index().drop(columns=['index'])

# Converting dataframe into CSV
df.to_csv('../data/home_data.csv', index=False)



