# Using Machine Learning/Deep Learning to identify home appliances consuming excessive power

# Overview

This Machine Learning model is helpful in aiding home automation and home appliaances when there is limited supply of power. Typical home appliances are considered and power consumption of these devices are noted down based on properties like type of device, time (hourly basis), power consumption, number of people and time they have used the appliances in an hour.

# Dependencies

1.	Python 3.x 
2.	Numpy, Scipy, Pandas, Matplotlib 
3.	TensorFlow 1.x+, Keras 2.x+
4.  NVIDIA CUDA 9.x, cuDNN 7.x (Only if using Tensorflow-GPU)
5.	Sci-kit learn


# Important Files and Folders

```
home
│   README.md   
│
└───data
│      sample - contains sample dataset
│      trial_x - all types of different datasets
│
└───regression
│      *.ipynb - Regression ML/DL algorithms
│   
└───model
│      regression models saved
│
└───docs
│      documentation and reports
│
└───main
       visualization - data analysis
       data generation - generate data and cleaning
       experiment - results and custom algorithms
```

# Usage

1.	```main/data generation/generate_home_data.py``` - generates ```home_data.csv```
    * Generates dataset with all columns
    * This dataset will be used to build machine learning model

2.	```main/data generation/generate_home_data_test.py``` - generates ```home_data_test.csv```
    * Generates dataset with all columns
    * This dataset will be used to predict power values

3.	```main/visualization/total_power_consumption.ipynb``` - creates ```date_time_group.csv```
    * This is the final output which will be used to visualise and compare machine learning algorithms

4.	```main/visualization/total_power_consumption_final.ipynb``` - creates ```final_output_group.csv```
    * This is the final output which will be used to visualise and compare machine learning algorithms

5.	```regression/<*>.ipynb```
    * Machine learning algorithms used on ```home_data.csv``` to build models in ```/model/```

6.	```predict/<*>.ipynb```
    * Machine learning algorithms used on ```home_data_test.csv``` to predict and generate new datasets
    * ```home_data_predict_x``` are dataset generated with prediction values

5.	```main/experiment/trail_x/trail_x_x.py```
    * Custom algorithm to give messages to users - generates ```final_output_x.csv``` in ```data/trail_x```

6.	```main/experiment/trail_x/results_x_x.py```
    * Visualising all algorithms and performances
    * Graphs plotted to identify power consumption before machine learning and after using machine learning and custom algorithm

# Results

Available in ```main/experiment/trail_x/results_x_x``` where 'x' can be either sequence or a machine learning algorithm

# Credits

[Vinod Agrawal](https://in.linkedin.com/in/vinod-agrawal-8020488)

CTO, Faststream Technologies

# License

Copyright(c) 2018, [Faststream Technologies](https://www.faststreamtech.com)

Authors: 

* [Sudhanva Narayana](https://www.sudhanva.in)
* [Shreyas S](https://www.shreyas.im)