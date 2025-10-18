# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:51:36 2024

@author: daizh
"""
"""
note for sensor data

0 - 285 sensor on the palte 
0, 2, 4, ... for bottom plate
1, 3, 5, ... for top plate  

286 -2202 sensor on the grain
"""
#%% 1 read in pakage
# set work directory
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

#%% 2 read in data
from read_data_ver2 import *  
# notice the version of readdata: without stress tensor ver1, with stress tensor ver2

#%% 3 set parameters
path_time_ = 'data/time_80G.npy'
path_shear_stress_ = 'data/shear_stress_80G.npy'
path_vmx_bottom_ = 'data/vmx_bottom_80G.npy'
path_vmx_top_ = 'data/vmx_top_80G.npy'
path_cmx_bottom_ = 'data/cmx_bottom_80G.npy'
path_cmx_top_ = 'data/cmx_top_80G.npy'

#%% 4 extracte friction and velocity data
# calculate velocity in a period
# bottom
index_ = 0
stop_index_ = sensors_[0].shape[0]
time_step_ = 1
list_vmx_bottom_ = [] # record the mean vx pf bottom
list_vmx_top_ = []   # record the mean vx of top
list_cmx_top_ = []    # record the mean cx of top
list_cmx_bottom_ = []    # record the mean cx of bottom

save_time_ =np.array(ConSV_PlateBottomBeadMiddle_.loc[index_:stop_index_, 'Time'])
save_shear_stress_ = np.array((ConSV_PlateBottomBeadMiddle_.loc[index_:stop_index_,'fx'] - ConSV_PlateTopBeadMiddle_.loc[index_:stop_index_,'fx']) / 2)
# plt.plot(ConSV_PlateBottomBeadMiddle_.loc[5e3:2e4, 'Time'],  \
#          (ConSV_PlateBottomBeadMiddle_.loc[5e3:2e4,'fx'] - ConSV_PlateTopBeadMiddle_.loc[5e3:2e4,'fx'])/ \
#          (ConSV_PlateTopBeadMiddle_.loc[5e3:2e4,'fy'] - ConSV_PlateBottomBeadMiddle_.loc[5e3:2e4,'fy']),\
#          linewidth = 1, color = 'b')


while index_ < stop_index_:
    print(index_)
    individuals_ = [int(2*i_) for i_ in range(143)]
    # bottom
    vmx_bottom_ = 0
    cmx_bottom_ = 0
    for i_ in individuals_:
        vmx_bottom_ += sensors_[i_].loc[index_, 'vx']
        cmx_bottom_ += sensors_[i_].loc[index_, 'cx']
    vmx_bottom_ = vmx_bottom_ / len(individuals_)
    cmx_bottom_ = cmx_bottom_ / len(individuals_)
    
    # top
    individuals_ = [int(2*i_+1) for i_ in range(143)]
    vmx_top_ = 0
    cmx_top_ = 0
    for i_ in individuals_:
        vmx_top_ += sensors_[i_].loc[index_, 'vx']
        cmx_top_ += sensors_[i_].loc[index_, 'cx']   
    vmx_top_ = vmx_top_ / len(individuals_)
    cmx_top_ = cmx_top_ / len(individuals_)

    # grains
    individuals_ = [int(i_) for i_ in range(286,2203)] 
    # not calculate for grains here

    
    list_vmx_bottom_.append(vmx_bottom_)
    list_cmx_bottom_.append(cmx_bottom_)
    list_vmx_top_.append(vmx_top_)
    list_cmx_top_.append(cmx_top_)    
        

    
    index_ += time_step_

save_vmx_bottom_ = np.array(list_vmx_bottom_)
save_cmx_bottom_ = np.array(list_cmx_bottom_)
save_vmx_top_ = np.array(list_vmx_top_)
save_cmx_top_ = np.array(list_cmx_top_)

print('Calculation done!')

#%% 5 save data
np.save(path_time_, save_time_)
np.save(path_shear_stress_, save_shear_stress_)
np.save(path_vmx_bottom_, save_vmx_bottom_)
np.save(path_vmx_top_, save_vmx_top_)
np.save(path_cmx_bottom_, save_cmx_bottom_)
np.save(path_cmx_top_, save_cmx_top_)
print('Save data done!')