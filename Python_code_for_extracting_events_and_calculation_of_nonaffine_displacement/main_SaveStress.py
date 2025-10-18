# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:53:32 2024

@author: daizh
"""

"""
note for sensor data

0 - 285 sensor on the palte 
0, 2, 4, ... for bottom plate
1, 3, 5, ... for top plate  

286 -2202 sensor on the grain
"""
#%% import package
import pandas as pd
import numpy as np
import os
import sys
import math
import pickle

#%% set work directory and import functions
# change current directory
os.chdir(os.path.dirname(sys.argv[0]))


#%%  read datas
from read_data_ver2 import *  
# notice the version of readdata: without stress tensor ver1, with stress tensor ver2


#%% set parameters 
file_events_ = open('data/events_data/events_Vp25_.pkl', 'rb')
events_ = pickle.load(file_events_)
condition_ = 'Vp25'

#%% loop main
print('Start output stresses!')
i_event_ = 0
for start_end_ in events_:
    print('\n-----------------------------------------------------\n')
    i_event_ += 1
    print("Total number of event is %d" % len(events_) )
    print("Current event index is %d" % i_event_)
    # extract data
    individuals_ = [int(i_) for i_ in range(286,2203)]  # sensors on the grain
    stresses_start_ = np.full([len(individuals_), 3], np.nan)
    stresses_end_ = np.full([len(individuals_), 3], np.nan)
    for i_ in individuals_:
        stresses_start_[i_ - individuals_[0], 0] = sensors_[i_].loc[start_end_[0],'Cxx']
        stresses_start_[i_ - individuals_[0], 1] = sensors_[i_].loc[start_end_[0],'Cyy']
        stresses_start_[i_ - individuals_[0], 2] = sensors_[i_].loc[start_end_[0],'Cxy']
        stresses_end_[i_ - individuals_[0], 0] = sensors_[i_].loc[start_end_[1],'Cxx']
        stresses_end_[i_ - individuals_[0], 1] = sensors_[i_].loc[start_end_[1],'Cyy']
        stresses_end_[i_ - individuals_[0], 2] = sensors_[i_].loc[start_end_[1],'Cxy']
    print('\n-----------------------------------------------------\n')
    print('\nRead data done!!\n')
    
    # save data
    print('\n-----------------------------------------------------\n')
    np.save('data/stress_data/stresses_at_%d_%s' % \
            (start_end_[0], condition_), stresses_start_)
    np.save('data/stress_data/stresses_at_%d_%s' % \
            (start_end_[1], condition_), stresses_end_)
    print('Save data done')
print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
print('Stresses saved. DONE.')




