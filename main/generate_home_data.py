import numpy as np 
import pandas as pd 
import random

labels = ['device',	'building',	'floor', 'room', 'type', 'power', 'date', 'from_time', 'to_time', 'no_of_people', 'time_stayed_mins']
devices = ['AC', 'Lights', 'Television', 'Refridgerator', 'Heater', 'Microwave', 'Computer']
buildings = np.random.randint(1, 4, 744)
floors = np.random.randint(1, 11, 744)
types = ['indoor', 'outdoor']
date_range = pd.date_range(start='1/1/2018', end='2/1/2018', freq='H')
from_range = date_range[:-1]
to_range = date_range[1:]
df = pd.DataFrame(columns=labels)
no_of_people = np.random.randint(0, 11, 744)
time_stayed_mins = np.random.randint(0, 31, 744)

df['building'] = buildings
df['floor'] = floors
df['date'] = date_range.date[:-1]
df['from_time'] = from_range.time
df['to_time'] = to_range.time
df['time_stayed_mins'] = time_stayed_mins
df['no_of_people'] = no_of_people
df['type'] = [random.choice(types) for i in range(744)]
df['device'] = [random.choice(devices) for i in range(744)]
type_bools = df['type'] == 'outdoor'

rooms = []
for index, value in enumerate(type_bools):
    if value:
        rooms.append(np.NaN)        
    else:
        rooms.append((floors[index] * 100) + random.randint(1, 7))
        
df['room'] = rooms

ac_indoor = np.arange(1000, 2000)
ac_outdoor = np.arange(2000, 5000)

light_indoor = np.arange(1000, 2000)
light_outdoor = np.arange(2000, 5000)

power = []

for dev, typ in zip(df['device'], df['type']):
    if dev == 'AC' and typ == 'indoor':
        
    





