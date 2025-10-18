# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:29:55 2024

@author: daizh
"""

#%% import pakage
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

#%% work directory
os.chdir(os.path.dirname(sys.argv[0]))

#%% import data

# P
time_P12_ = np.load('data/time_P12.npy')
shear_stress_P12_ = np.load('data/shear_stress_P12.npy')
vmx_bottom_P12_ = np.load('data/vmx_bottom_P12.npy')
vmx_top_P12_ = np.load('data/vmx_top_P12.npy')

time_P20_ = np.load('data/time_P20.npy')
shear_stress_P20_ = np.load('data/shear_stress_P20.npy')
vmx_bottom_P20_ = np.load('data/vmx_bottom_P20.npy')
vmx_top_P20_ = np.load('data/vmx_top_P20.npy')

time_P28_ = np.load('data/time_P28.npy')
shear_stress_P28_ = np.load('data/shear_stress_P28.npy')
vmx_bottom_P28_ = np.load('data/vmx_bottom_P28.npy')
vmx_top_P28_ = np.load('data/vmx_top_P28.npy')

time_P36_ = np.load('data/time_P36.npy')
shear_stress_P36_ = np.load('data/shear_stress_P36.npy')
vmx_bottom_P36_ = np.load('data/vmx_bottom_P36.npy')
vmx_top_P36_ = np.load('data/vmx_top_P36.npy')

time_P44_ = np.load('data/time_P44.npy')
shear_stress_P44_ = np.load('data/shear_stress_P44.npy')
vmx_bottom_P44_ = np.load('data/vmx_bottom_P44.npy')
vmx_top_P44_ = np.load('data/vmx_top_P44.npy')

# V

time_Vp1_ = np.load('data/time_Vp1.npy')
shear_stress_Vp1_ = np.load('data/shear_stress_Vp1.npy')
vmx_bottom_Vp1_ = np.load('data/vmx_bottom_Vp1.npy')
vmx_top_Vp1_ = np.load('data/vmx_top_Vp1.npy')
vmx_bottom_Vp1_ = np.insert(vmx_bottom_Vp1_, 0, 0)
vmx_top_Vp1_ = np.insert(vmx_top_Vp1_, 0, 0)

time_Vp25_ = np.load('data/time_Vp25.npy')
shear_stress_Vp25_ = np.load('data/shear_stress_Vp25.npy')
vmx_bottom_Vp25_ = np.load('data/vmx_bottom_Vp25.npy')
vmx_top_Vp25_ = np.load('data/vmx_top_Vp25.npy')

time_V01_ = np.load('data/time_V01.npy')
shear_stress_V01_ = np.load('data/shear_stress_V01.npy')
vmx_bottom_V01_ = np.load('data/vmx_bottom_V01.npy')
vmx_top_V01_ = np.load('data/vmx_top_V01.npy')

# G

time_2G_ = np.load('data/time_2G.npy')
shear_stress_2G_ = np.load('data/shear_stress_2G.npy')
vmx_bottom_2G_ = np.load('data/vmx_bottom_2G.npy')
vmx_top_2G_ = np.load('data/vmx_top_2G.npy')

time_4G_ = np.load('data/time_4G.npy')
shear_stress_4G_ = np.load('data/shear_stress_4G.npy')
vmx_bottom_4G_ = np.load('data/vmx_bottom_4G.npy')
vmx_top_4G_ = np.load('data/vmx_top_4G.npy')

time_20G_ = np.load('data/time_20G.npy')
shear_stress_20G_ = np.load('data/shear_stress_20G.npy')
vmx_bottom_20G_ = np.load('data/vmx_bottom_20G.npy')
vmx_top_20G_ = np.load('data/vmx_top_20G.npy')

time_80G_ = np.load('data/time_80G.npy')
shear_stress_80G_ = np.load('data/shear_stress_80G.npy')
vmx_bottom_80G_ = np.load('data/vmx_bottom_80G.npy')
vmx_top_80G_ = np.load('data/vmx_top_80G.npy')
vmx_bottom_80G_ = np.insert(vmx_bottom_80G_, 0, 0)
vmx_top_80G_ = np.insert(vmx_top_80G_, 0, 0)

#%% distinguish and slice the events' data
########### define functions
# 1. get the part which large than the threshold
def initial_extract(vmx_top_, vmx_bottom_, thresh_v_):
    '''
    Parameters: 
        vmx_top_--the velocity of top plate
        vmx_bottom_-- the velocity of bottom plate
        thresh_v_--the threshold of velocity to define a slip event
        
    Returns: 
        list_event_slice_--record the start and end index of each event
        
    '''
    list_event_slice_ = []
    t_ = np.full([2, 1], np.nan)
    in_slip_ = False
    for i_ in range(vmx_top_.shape[0]):
        if in_slip_:
            if np.abs((vmx_top_[i_] - vmx_bottom_[i_]) / 2) < thresh_v_:
                t_[1] = i_
                list_event_slice_.append(t_.astype('int'))
                if t_[1] < t_[0]:
                    print('顺序错误')
                in_slip_ = False
        else:
            if np.abs((vmx_top_[i_] - vmx_bottom_[i_]) / 2) > thresh_v_:
                t_[0] = i_
                in_slip_ = True
        
    print('Extract successful!')
    return list_event_slice_

# list_event_slice_test_ = initial_extract(vmx_top_P28_, vmx_bottom_P28_, thresh_v_ = 1e-3)

# plt.plot(np.abs((vmx_top_P28_ - vmx_bottom_P28_) / 2))


# 2. connect the neibor events which are in a certain distance  
def connect_neighbor(time_, vmx_top_, vmx_bottom_, list_event_slice_, thresh_v_):
    '''
    Parameters: 
        time_--time
        vmx_top_--the velocity of top plate
        vmx_bottom_-- the velocity of bottom plate
        list_event_slice_--record the start and end index of each event (get from function initial_extract)
        thresh_v_--the threshold of velocity to define a slip event
    Returns: 
        list_conncted_event_--record the start and end index of connected events
        
    '''
    list_conncted_event_ = []
    
    interval_displacement_ = time_[1] - time_[0]
    plate_velocity_ = np.abs((vmx_top_ - vmx_bottom_) / 2)
    i_events_ = 0
    # find the peak points 
    for start_end_ in list_event_slice_:
        peak_v_ = -1 # record the maximum
        peak_ = 0  # record the position
        for i_ in range(start_end_[0][0], start_end_[1][0]):
            if plate_velocity_[i_] > peak_v_:
                peak_v_ = plate_velocity_[i_]
                peak_ = i_
        
        # extend the index 
        k_1_ = (plate_velocity_[peak_] - plate_velocity_[start_end_[0][0] - 1]) / ((peak_-(start_end_[0][0] - 1)) * interval_displacement_)
        k_2_ = (plate_velocity_[peak_] - plate_velocity_[start_end_[1][0]] + 1) / ((-peak_ + (start_end_[1][0] + 1)) * interval_displacement_)
        list_event_slice_[i_events_][0] -= int(thresh_v_ / k_1_ / interval_displacement_ + 1) 
  
        list_event_slice_[i_events_][1] += int(thresh_v_ / k_2_ / interval_displacement_ + 1)
        i_events_ += 1
    # conect the event
    count_connect_ = 0 # record the connect times
    connect_state_ = False # judge if the connecting is going
    t_ = np.full([2, 1], np.nan)
    for i_ in range(len(list_event_slice_) - 1):
        if connect_state_:
            
            if list_event_slice_[i_][1] >=  list_event_slice_[i_ + 1][0]:
                continue
            else:
                t_[1] = list_event_slice_[i_][1]
                list_conncted_event_.append(t_.astype('int'))
                
                connect_state_ = False
                if t_[1] < t_[0]:
                    print('顺序错误')
        else:
            if list_event_slice_[i_][1] >=  list_event_slice_[i_ + 1][0]:
                t_[0] = list_event_slice_[i_][0]
                count_connect_ += 1
                connect_state_ = True
                
            else:
                t_[0] = list_event_slice_[i_][0]
                t_[1] = list_event_slice_[i_][1]
                list_conncted_event_.append(t_.astype('int'))
                if t_[1] < t_[0]:
                    print('顺序错误')
    if connect_state_:
        t_[1] = list_event_slice_[-1][1]
        list_conncted_event_.append(t_.astype('int'))
    if list_conncted_event_[-1][1] > time_.shape[0] - 1:
        list_conncted_event_[-1][1][0] = int(time_.shape[0] - 1)
    print('Connected successful! %d events have been connected!!!' % count_connect_)

    return list_conncted_event_

# list_event_slice_test_ = initial_extract(vmx_top_P28_, vmx_bottom_P28_, thresh_v_ = 1e-3)
# list_connected_events_test_ = connect_neighbor(time_P28_, vmx_top_P28_, vmx_bottom_P28_, list_event_slice_test_, 1e-3)
# plt.plot(np.abs((vmx_top_P28_[23606:23619] - vmx_bottom_P28_[23606:23619]) / 2))


# 3. find the stable period
def find_stable(time_, list_conncted_event_, thresh_t_):
    '''
    Parameters: 
        time_--the time
        list_conncted_event_--record the start and end index of connected events (get from function connect_neighbor)
        thresh_t_--the threshold of time to define stable period
    Returns: 
        list_stable_event_--record the start and end index of events in stable period
        
    '''
    list_stable_event_ = []
    count_deleted_events_ = 0
    for start_end_ in list_conncted_event_:
        if time_[start_end_[1][0]] < thresh_t_:
            count_deleted_events_ += 1
            continue
        else:
            list_stable_event_.append(start_end_.copy())
    print('Select the events in stable period successful! %d events are deleted!' % count_deleted_events_)
    return list_stable_event_
# list_event_slice_test_ = initial_extract(vmx_top_P28_, vmx_bottom_P28_, thresh_v_ = 1e-3)
# list_connected_events_test_ = connect_neighbor(time_P28_, vmx_top_P28_, vmx_bottom_P28_, list_event_slice_test_, 1e-3)
# list_stable_event_test_ = find_stable(time_P28_, list_connected_events_test_, thresh_t_ = 8000)
# plt.plot(np.abs((vmx_top_P28_[5015:5022] - vmx_bottom_P28_[5015:5022]) / 2))

#%% ######### do the calculation
# P12
list_event_slice_P12_ = initial_extract(vmx_top_P12_, vmx_bottom_P12_, thresh_v_ = 1e-3)
list_connected_events_P12_ = connect_neighbor(time_P12_, vmx_top_P12_, vmx_bottom_P12_, list_event_slice_P12_, thresh_v_ = 1e-3)
list_stable_event_P12_ = find_stable(time_P12_, list_connected_events_P12_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_P12_.pkl', 'wb')
pickle.dump(list_stable_event_P12_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_P12_), filename_))
# P20
list_event_slice_P20_ = initial_extract(vmx_top_P20_, vmx_bottom_P20_, thresh_v_ = 1e-3)
list_connected_events_P20_ = connect_neighbor(time_P20_, vmx_top_P20_, vmx_bottom_P20_, list_event_slice_P20_, thresh_v_ = 1e-3)
list_stable_event_P20_ = find_stable(time_P20_, list_connected_events_P20_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_P20_.pkl', 'wb')
pickle.dump(list_stable_event_P20_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_P20_), filename_))
# P28
list_event_slice_P28_ = initial_extract(vmx_top_P28_, vmx_bottom_P28_, thresh_v_ = 1e-3)
list_connected_events_P28_ = connect_neighbor(time_P28_, vmx_top_P28_, vmx_bottom_P28_, list_event_slice_P28_, thresh_v_ = 1e-3)
list_stable_event_P28_ = find_stable(time_P28_, list_connected_events_P28_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_P28_.pkl', 'wb')
pickle.dump(list_stable_event_P28_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_P28_), filename_))
# P36
list_event_slice_P36_ = initial_extract(vmx_top_P36_, vmx_bottom_P36_, thresh_v_ = 1e-3)
list_connected_events_P36_ = connect_neighbor(time_P36_, vmx_top_P36_, vmx_bottom_P36_, list_event_slice_P36_, thresh_v_ = 1e-3)
list_stable_event_P36_ = find_stable(time_P36_, list_connected_events_P36_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_P36_.pkl', 'wb')
pickle.dump(list_stable_event_P36_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_P36_), filename_))
# P44
list_event_slice_P44_ = initial_extract(vmx_top_P44_, vmx_bottom_P44_, thresh_v_ = 1e-3)
list_connected_events_P44_ = connect_neighbor(time_P44_, vmx_top_P44_, vmx_bottom_P44_, list_event_slice_P44_, thresh_v_ = 1e-3)
list_stable_event_P44_ = find_stable(time_P44_, list_connected_events_P44_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_P44_.pkl', 'wb')
pickle.dump(list_stable_event_P44_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_P44_), filename_))

# Vp25
list_event_slice_Vp25_ = initial_extract(vmx_top_Vp25_, vmx_bottom_Vp25_, thresh_v_ = 1e-3)
list_connected_events_Vp25_ = connect_neighbor(time_Vp25_, vmx_top_Vp25_, vmx_bottom_Vp25_, list_event_slice_Vp25_, thresh_v_ = 1e-3)
list_stable_event_Vp25_ = find_stable(time_Vp25_, list_connected_events_Vp25_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_Vp25_.pkl', 'wb')
pickle.dump(list_stable_event_Vp25_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_Vp25_), filename_))

# V01
list_event_slice_V01_ = initial_extract(vmx_top_V01_, vmx_bottom_V01_, thresh_v_ = 1e-3)
list_connected_events_V01_ = connect_neighbor(time_V01_, vmx_top_V01_, vmx_bottom_V01_, list_event_slice_V01_, thresh_v_ = 1e-3)
list_stable_event_V01_ = find_stable(time_V01_, list_connected_events_V01_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_V01_.pkl', 'wb')
pickle.dump(list_stable_event_V01_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_V01_), filename_))

# 2G
list_event_slice_2G_ = initial_extract(vmx_top_2G_, vmx_bottom_2G_, thresh_v_ = 1e-3)
list_connected_events_2G_ = connect_neighbor(time_2G_, vmx_top_2G_, vmx_bottom_2G_, list_event_slice_2G_, thresh_v_ = 1e-3)
list_stable_event_2G_ = find_stable(time_2G_, list_connected_events_2G_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_2G_.pkl', 'wb')
pickle.dump(list_stable_event_2G_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_2G_), filename_))

# 4G
list_event_slice_4G_ = initial_extract(vmx_top_4G_, vmx_bottom_4G_, thresh_v_ = 1e-3)
list_connected_events_4G_ = connect_neighbor(time_4G_, vmx_top_4G_, vmx_bottom_4G_, list_event_slice_4G_, thresh_v_ = 1e-3)
list_stable_event_4G_ = find_stable(time_4G_, list_connected_events_4G_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_4G_.pkl', 'wb')
pickle.dump(list_stable_event_4G_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_4G_), filename_))

# 20G
list_event_slice_20G_ = initial_extract(vmx_top_20G_, vmx_bottom_20G_, thresh_v_ = 1e-3)
list_connected_events_20G_ = connect_neighbor(time_20G_, vmx_top_20G_, vmx_bottom_20G_, list_event_slice_20G_, thresh_v_ = 1e-3)
list_stable_event_20G_ = find_stable(time_20G_, list_connected_events_20G_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_20G_.pkl', 'wb')
pickle.dump(list_stable_event_20G_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_20G_), filename_))

# 80G
list_event_slice_80G_ = initial_extract(vmx_top_80G_, vmx_bottom_80G_, thresh_v_ = 1e-3)
list_connected_events_80G_ = connect_neighbor(time_80G_, vmx_top_80G_, vmx_bottom_80G_, list_event_slice_80G_, thresh_v_ = 1e-3)
list_stable_event_80G_ = find_stable(time_80G_, list_connected_events_80G_, thresh_t_ = 8000)
filename_ = open('data/events_data/events_80G_.pkl', 'wb')
pickle.dump(list_stable_event_80G_, filename_)
filename_.close()
print('%d events are saved to %s' % (len(list_stable_event_80G_), filename_))



#%% read
# filename_ = open('data/events_data/events_P12_.pkl', 'rb')
# t_ = pickle.load(filename_)
# print(t_)
# filename_.close()