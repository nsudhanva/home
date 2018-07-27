for main_index, main_row in df_home_data_test.iterrows():
    sample_date = main_row['date']
    sample_time = main_row['from_time']

    sample_df = df_home_data_test[(df_home_data_test['date'] == sample_date) & (df_home_data_test['from_time'] == sample_time)]
    sample_total_power = sample_df['power'].sum()

    power = date_time_group[(date_time_group['date'] == sample_date) & (date_time_group['from_time'] == sample_time)]
    condition = sample_total_power > power['power'][power['power'].index[0]]

    # Creates priorities for devices
    priorities = []

    for index, row in sample_df.iterrows():
        priorities.append(df_home_priority[(df_home_priority['device'] == row['device']) 
                               & (df_home_priority['weather_type'] == row['weather_type']) 
                               & (df_home_priority['time'] == row['time'])].values[0][4])

    priorities = pd.Series(priorities)

    sample_df = sample_df.assign(priorities=priorities.values)
    sample_df = sample_df.sort_values(['priorities', 'no_of_people'], ascending=[True,False])
    old_df = sample_df.copy()
    sample_after_power = 10000000

    # Keep looping till all rows are appended created and appended
    while sample_total_power < sample_after_power:
        no_of_people_index = sample_df.iloc[[-2]]['no_of_people'].index[0]

        last_one_room = sample_df.iloc[[-2]]['room'].values[0]
        last_no_of_people = sample_df.iloc[[-1]]['no_of_people'].values[0]
        last_one_no_of_people = sample_df.iloc[[-2]]['no_of_people'].values[0]
        last_room = sample_df.iloc[[-1]]['room'].values[0]
        last_device = sample_df.iloc[[-1]]['device'].values[0]
        
        sample_df.at[no_of_people_index, 'no_of_people'] = last_no_of_people + last_one_no_of_people 
        sample_df_drop = sample_df.drop(sample_df.tail(1).index) 
        sample_after_power = sample_total_power - sample_df_drop['power'].sum()

        # Gives messages to users
        action = 'Turn off ' + last_device + ' in room ' + str(last_room)
        
        if last_no_of_people != 0:
            message = 'Moving ' + str(last_no_of_people) + ' people from room ' + str(last_room) + ' to room ' + str(last_one_room) + ' saves ' + str(sample_after_power) + ' of' + ' electricity, ' + 'power consumption will reduce from ' +  str(sample_total_power) + ' to ' + str(sample_total_power - sample_after_power)
        else:
            message = 'None'
            
        # Appends decided messages
        messages.append(message)
        actions.append(action)
        savings.append(sample_after_power)