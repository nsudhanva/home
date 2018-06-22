# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:25:59 2018

@author: Sudhanva
"""

dicto = {('AC', 'indoor'): 1362.2142857142858,
  ('AC', 'outdoor'): 3470.705882352941,
  ('Computer', 'indoor'): 399.0,
  ('Computer', 'outdoor'): 412.4,
  ('Heater', 'indoor'): 2258.375,
  ('Heater', 'outdoor'): 2274.6666666666665,
  ('Lights', 'indoor'): 1535.0,
  ('Lights', 'outdoor'): 3475.4736842105262,
  ('Microwave', 'indoor'): 1420.0,
  ('Microwave', 'outdoor'): 1489.9333333333334,
  ('Refridgerator', 'indoor'): 192.38888888888889,
  ('Refridgerator', 'outdoor'): 195.07692307692307,
  ('Television', 'indoor'): 243.66666666666666,
  ('Television', 'outdoor'): 261.5}

df_dict = {}
df_type = {}

for key, value in dicto.items():
    print(key, value)
    df_type[key[1]] = value
    df_dict[key[0]] = df_type.copy()
    