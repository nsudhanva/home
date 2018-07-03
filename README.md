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
│      home_data.csv - data without labels
|      home_final.csv - final data with labels
│   
└───classification
│      *.ipynb - Classification ML/DL algorithms
│      results.ipynb - Final results and graphs
│
└───regression
│      *.ipynb - Regression ML/DL algorithms
│   
└───model
│      regression models
│
└───docs
│      documentation and reports
│
└───main
       visualization - data analysis
       data generation - generate data and cleaning
```

# Usage

* ```generate_home_data.py``` - Generate data - with power consumption
* ```generate_home_data_test.py``` - Generate unseen data - with no power consumption

# Results

| No |  Algorithms	                    | Accuracy (%)  |
| ---|:--------------------------------:| -------------:|
| 1	 |  K Nearest Neighbours	        | 56%           |
| 2	 |  Decision Tree Classification	| 93.5%         |
| 3	 |  Kernel Support Vector Machines	| 62%           |
| 4	 |  Logistic Regression	            | 66.66%        |
| 5	 |  Artifical Neural Networks       | 74%           |
| 6	 |  Random Forest Classification	| 91.1%         |
| 7	 |  Support Vector Machines	        | 64.9%         |


# Credits

[Vinod Agrawal](https://in.linkedin.com/in/vinod-agrawal-8020488)

CTO, Faststream Technologies

# License

Copyright(c) 2018, [Faststream Technologies](https://www.faststreamtech.com)

![Faststream Logo](https://netmyjob.com/uploads/employer/1518498102-FaststreamTechnologiesPrivatelimitedlogo.png "Faststream Tech")

Author: [Sudhanva Narayana](https://www.sudhanva.in)