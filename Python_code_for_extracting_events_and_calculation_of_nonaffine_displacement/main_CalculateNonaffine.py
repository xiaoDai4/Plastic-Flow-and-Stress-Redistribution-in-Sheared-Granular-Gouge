# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:27:25 2024

@author: daizh
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
from calculate_distance import *
from assign_neighbor import *
from calculate_nonaffine_displacement import *

#%%  read datas
from read_data_ver2 import *  
# notice the version of readdata: without stress tensor ver1, with stress tensor ver2


#%% set parameters 
file_events_ = open('data/events_data/events_80G_.pkl', 'rb')
events_ = pickle.load(file_events_)
condition_ = '80G'
threshold_ = 2


#%% loop main
print('Start NonAffine in slips!')
i_event_ = 0
for start_end_ in events_:
    print('\n-----------------------------------------------------\n')
    i_event_ += 1
    print("Total number of event is %d" % len(events_) )
    print("Current event index is %d" % i_event_)
    # extract data
    individuals_ = [int(i_) for i_ in range(286,2203)]  # sensors on the grain
    c_former_ = np.full([len(individuals_), 2], np.nan)
    c_later_ = np.full([len(individuals_), 2], np.nan)
    for i_ in individuals_:
        c_former_[i_ - individuals_[0], 0] = sensors_[i_].loc[start_end_[0],'cx']
        c_former_[i_ - individuals_[0], 1] = sensors_[i_].loc[start_end_[0],'cy']
        c_later_[i_ - individuals_[0], 0] = sensors_[i_].loc[start_end_[1],'cx']
        c_later_[i_ - individuals_[0], 1] = sensors_[i_].loc[start_end_[1],'cy']
    print('\n-----------------------------------------------------\n')
    print('\nRead data done!!\n')
    # calculate distance
    print('\n-----------------------------------------------------\n')
    distance_ = calculate_distance(c_former_)
    # assign neighbor
    print('\n-----------------------------------------------------\n')
    neighbor_ = assign_neighbor(distance_, threshold_)
    # calculate non-affine displacement
    print('\n-----------------------------------------------------\n')
    nonaffine_ = calculate_nonaffine(c_former_, c_later_, neighbor_) # a vector that store the nonaffine displacement
    # save data
    print('\n-----------------------------------------------------\n')
    np.save('data/coordinate_data/c_former_of_%s_from_%d_to_%d' % \
            (condition_ + '_slip', start_end_[0], start_end_[1]), c_former_)
    np.save('data/nonaffine_data/nonaffine_of_%s_from_%d_to_%d' % \
            (condition_ + '_slip', start_end_[0], start_end_[1]), nonaffine_)
    print('Save data done')
print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
print('NonAffine saved. SLIP ALL DONE.')

#%% loop main
# get the sticks
sticks_ = []
t_ = np.full([2, 1], np.nan)
for i_ in range(len(events_)):
    if i_ == len(events_) - 1:
        break
    t_[0] = events_[i_][1]
    t_[1] = events_[i_ + 1 ][0]
    sticks_.append(t_.astype('int'))

print('Start NonAffine in sticks!')
i_event_ = 0
for start_end_ in sticks_:
    print('\n-----------------------------------------------------\n')
    i_event_ += 1
    print("Total number of sticks is %d" % len(events_) )
    print("Current sticks index is %d" % i_event_)
    # extract data
    individuals_ = [int(i_) for i_ in range(286,2203)]  # sensors on the grain
    c_former_ = np.full([len(individuals_), 2], np.nan)
    c_later_ = np.full([len(individuals_), 2], np.nan)
    for i_ in individuals_:
        c_former_[i_ - individuals_[0], 0] = sensors_[i_].loc[start_end_[0],'cx']
        c_former_[i_ - individuals_[0], 1] = sensors_[i_].loc[start_end_[0],'cy']
        c_later_[i_ - individuals_[0], 0] = sensors_[i_].loc[start_end_[1],'cx']
        c_later_[i_ - individuals_[0], 1] = sensors_[i_].loc[start_end_[1],'cy']
    print('\n-----------------------------------------------------\n')
    print('\nRead data done!!\n')
    # calculate distance
    print('\n-----------------------------------------------------\n')
    distance_ = calculate_distance(c_former_)
    # assign neighbor
    print('\n-----------------------------------------------------\n')
    neighbor_ = assign_neighbor(distance_, threshold_)
    # calculate non-affine displacement
    print('\n-----------------------------------------------------\n')
    nonaffine_ = calculate_nonaffine(c_former_, c_later_, neighbor_) # a vector that store the nonaffine displacement
    # save data
    print('\n-----------------------------------------------------\n')
    np.save('data/coordinate_data/c_former_of_%s_from_%d_to_%d' % \
            (condition_ + '_stick', start_end_[0], start_end_[1]), c_former_)
    np.save('data/nonaffine_data/nonaffine_of_%s_from_%d_to_%d' % \
            (condition_ + '_stick', start_end_[0], start_end_[1]), nonaffine_)
    print('Save data done')
print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
print('NonAffine saved. STICK ALL DONE.')


#%% loop main
# get the long term
start_end_ = np.array([events_[0][0], events_[-1][-1]])
print('\n-----------------------------------------------------\n')
print('\nLong term!!\n')
# extract data
individuals_ = [int(i_) for i_ in range(286,2203)]  # sensors on the grain
c_former_ = np.full([len(individuals_), 2], np.nan)
c_later_ = np.full([len(individuals_), 2], np.nan)
for i_ in individuals_:
    c_former_[i_ - individuals_[0], 0] = sensors_[i_].loc[start_end_[0],'cx']
    c_former_[i_ - individuals_[0], 1] = sensors_[i_].loc[start_end_[0],'cy']
    c_later_[i_ - individuals_[0], 0] = sensors_[i_].loc[start_end_[1],'cx']
    c_later_[i_ - individuals_[0], 1] = sensors_[i_].loc[start_end_[1],'cy']
print('\n-----------------------------------------------------\n')
print('\nRead data done!!\n')
# calculate distance
print('\n-----------------------------------------------------\n')
distance_ = calculate_distance(c_former_)
# assign neighbor
print('\n-----------------------------------------------------\n')
neighbor_ = assign_neighbor(distance_, threshold_)
# calculate non-affine displacement
print('\n-----------------------------------------------------\n')
nonaffine_ = calculate_nonaffine(c_former_, c_later_, neighbor_) # a vector that store the nonaffine displacement
# save data
print('\n-----------------------------------------------------\n')
np.save('data/coordinate_data/c_former_of_%s_from_%d_to_%d' % \
        (condition_ + '_long_term', start_end_[0], start_end_[1]), c_former_)
np.save('data/nonaffine_data/nonaffine_of_%s_from_%d_to_%d' % \
        (condition_ + '_long_term', start_end_[0], start_end_[1]), nonaffine_)
print('Save data done')
print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
print('NonAffine saved. STICK ALL DONE.')
