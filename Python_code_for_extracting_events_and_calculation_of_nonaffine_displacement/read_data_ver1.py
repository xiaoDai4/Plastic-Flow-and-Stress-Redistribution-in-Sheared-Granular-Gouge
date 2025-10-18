# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:48:42 2022

@author: xiaod
"""



#%% import pakages
import zipfile
import pandas as pd
import os
#%%

#%% set parameters

path_ = 'D:\\fault_sensor_data\\PhotoElastic12_sensors\\py_Earthquake2D_PhotoElastic12_P28_V'

# 'D:\\fault_sensor_data\\PhotoElastic12_sensors\\py_Earthquake2D_PhotoElastic12_P28_V'
zipfile_name_ =  'sensor_PhotoElastic12_P28_f15_V01_rst%02d.zip'
print(path_+zipfile_name_)
# 'sensor_PhotoElastic12_P04_f15_Vp5_rst%02d.zip'
start_sensors_ = 0  # minimum is 0
n_sensors_ = 2203
n_rst_ = 20

#%%

#%% initial config
energy_ = pd.DataFrame(columns=['Time', 'KineticEnergy'])

ConSV_BeadMiddleBeadMiddle_ = pd.DataFrame(columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef'])
ConSV_BeadSidesBeadMiddle_ = pd.DataFrame(columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef'])
ConSV_BeadSidesBeadSides_ = pd.DataFrame(columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef'])
ConSV_FoamBeadSides_ = pd.DataFrame(columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef'])
ConSV_FoamPlateBottom_ = pd.DataFrame(columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef'])
ConSV_FoamPlateTop_ = pd.DataFrame(columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef'])
ConSV_PlateBottomBeadMiddle_ = pd.DataFrame(columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef'])
ConSV_PlateBottomBeadSides_ = pd.DataFrame(columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef'])
ConSV_PlateTopBeadMiddle_ = pd.DataFrame(columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef'])
ConSV_PlateTopBeadSides_ = pd.DataFrame(columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef'])

sensors_ = [0 for i_ in range(n_sensors_-start_sensors_) ]
for i_ in range(start_sensors_, n_sensors_):
    sensors_[i_] = pd.DataFrame(columns = ['Time', 'cx', 'cy', 'cz', 'vx', 'vy', 'vz'])
    
#%%

#%% read data
for i_ in range(n_rst_):    
    t_path_ = os.path.join(path_,zipfile_name_ % i_)
    t_zipfile_ = zipfile.ZipFile(t_path_, 'r')
    # display
    print(i_)
    # energy
    energy_file_ = t_zipfile_.open('energy')
    t_energy_ = pd.read_table(energy_file_, delimiter = ',')
    t_energy_.columns = ['Time', 'KineticEnergy']
    energy_ = pd.concat([energy_,t_energy_])
    
    # contact pairs
    ConSV_BeadMiddleBeadMiddle_file_ = t_zipfile_.open('ConSV_BeadMiddleBeadMiddle')
    t_ConSV_BeadMiddleBeadMiddle_ = pd.read_table(ConSV_BeadMiddleBeadMiddle_file_, header= None, delimiter = ',')
    t_ConSV_BeadMiddleBeadMiddle_.columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef']
    ConSV_BeadMiddleBeadMiddle_ = pd.concat([ConSV_BeadMiddleBeadMiddle_,t_ConSV_BeadMiddleBeadMiddle_])
    
    ConSV_BeadSidesBeadMiddle_file_ = t_zipfile_.open('ConSV_BeadSidesBeadMiddle')
    t_ConSV_BeadSidesBeadMiddle_ = pd.read_table(ConSV_BeadSidesBeadMiddle_file_, header= None, delimiter = ',')
    t_ConSV_BeadSidesBeadMiddle_.columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef']
    ConSV_BeadSidesBeadMiddle_ = pd.concat([ConSV_BeadSidesBeadMiddle_,t_ConSV_BeadSidesBeadMiddle_])
    
    ConSV_BeadSidesBeadSides_file_ = t_zipfile_.open('ConSV_BeadSidesBeadSides')
    t_ConSV_BeadSidesBeadSides_ = pd.read_table(ConSV_BeadSidesBeadSides_file_, header= None, delimiter = ',')
    t_ConSV_BeadSidesBeadSides_.columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef']
    ConSV_BeadSidesBeadSides_ = pd.concat([ConSV_BeadSidesBeadSides_,t_ConSV_BeadSidesBeadSides_])
    
    ConSV_FoamBeadSides_file_ = t_zipfile_.open('ConSV_FoamBeadSides')
    t_ConSV_FoamBeadSides_ = pd.read_table(ConSV_FoamBeadSides_file_, header= None, delimiter = ',')
    t_ConSV_FoamBeadSides_.columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef']
    ConSV_FoamBeadSides_ = pd.concat([ConSV_FoamBeadSides_, t_ConSV_FoamBeadSides_])
    
    ConSV_FoamPlateBottom_file_ = t_zipfile_.open('ConSV_FoamPlateBottom')
    t_ConSV_FoamPlateBottom_ = pd.read_table(ConSV_FoamPlateBottom_file_, header= None, delimiter = ',')
    t_ConSV_FoamPlateBottom_.columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef']
    ConSV_FoamPlateBottom_ = pd.concat([ConSV_FoamPlateBottom_, t_ConSV_FoamPlateBottom_])
    
    ConSV_FoamPlateTop_file_ = t_zipfile_.open('ConSV_FoamPlateTop')
    t_ConSV_FoamPlateTop_ = pd.read_table(ConSV_FoamPlateTop_file_, header= None, delimiter = ',')
    t_ConSV_FoamPlateTop_.columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef']
    ConSV_FoamPlateTop_ = pd.concat([ConSV_FoamPlateTop_, t_ConSV_FoamPlateTop_])
    
    ConSV_PlateBottomBeadMiddle_file_ = t_zipfile_.open('ConSV_PlateBottomBeadMiddle')
    t_ConSV_PlateBottomBeadMiddle_ = pd.read_table(ConSV_PlateBottomBeadMiddle_file_, header= None, delimiter = ',')
    t_ConSV_PlateBottomBeadMiddle_.columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef']
    ConSV_PlateBottomBeadMiddle_ = pd.concat([ConSV_PlateBottomBeadMiddle_, t_ConSV_PlateBottomBeadMiddle_])
    
    ConSV_PlateBottomBeadSides_file_ = t_zipfile_.open('ConSV_PlateBottomBeadSides')
    t_ConSV_PlateBottomBeadSides_ = pd.read_table(ConSV_PlateBottomBeadSides_file_, header= None, delimiter = ',')
    t_ConSV_PlateBottomBeadSides_.columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef']
    ConSV_PlateBottomBeadSides_ = pd.concat([ConSV_PlateBottomBeadSides_, t_ConSV_PlateBottomBeadSides_])
    
    ConSV_PlateTopBeadMiddle_file_ = t_zipfile_.open('ConSV_PlateTopBeadMiddle')
    t_ConSV_PlateTopBeadMiddle_ = pd.read_table(ConSV_PlateTopBeadMiddle_file_, header= None, delimiter = ',')
    t_ConSV_PlateTopBeadMiddle_.columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef']
    ConSV_PlateTopBeadMiddle_ = pd.concat([ConSV_PlateTopBeadMiddle_, t_ConSV_PlateTopBeadMiddle_])
    
    ConSV_PlateTopBeadSides_file_ = t_zipfile_.open('ConSV_PlateTopBeadSides')
    t_ConSV_PlateTopBeadSides_ = pd.read_table(ConSV_PlateTopBeadSides_file_, header= None, delimiter = ',')
    t_ConSV_PlateTopBeadSides_.columns = ['Time', 'fx', 'fy', 'fz', 'Es', 'Et', 'Ef']
    ConSV_PlateTopBeadSides_ = pd.concat([ConSV_PlateTopBeadSides_, t_ConSV_PlateTopBeadSides_])
    
    # sensors
    t_sensors_ = [0 for i_ in range(n_sensors_-start_sensors_) ]
    for j_ in range(start_sensors_, n_sensors_):
        t_sensor_file_ = t_zipfile_.open('sensor%04d' % j_)
        t_sensors_[j_] = pd.read_table(t_sensor_file_, header = 1, delimiter = ',')
        t_sensors_[j_].columns = ['Time', 'cx', 'cy', 'cz', 'vx', 'vy', 'vz']
        sensors_[j_] = pd.concat([sensors_[j_], t_sensors_[j_]])
    
#%%

#%% reset index
energy_ = energy_.reset_index()
energy_ = energy_.drop('index', axis = 1)
ConSV_BeadMiddleBeadMiddle_ = ConSV_BeadMiddleBeadMiddle_.reset_index()
ConSV_BeadMiddleBeadMiddle_ = ConSV_BeadMiddleBeadMiddle_.drop('index', axis = 1)
ConSV_BeadSidesBeadMiddle_ = ConSV_BeadSidesBeadMiddle_.reset_index()
ConSV_BeadSidesBeadMiddle_ = ConSV_BeadSidesBeadMiddle_.drop('index', axis = 1)
ConSV_BeadSidesBeadSides_ = ConSV_BeadSidesBeadSides_.reset_index()
ConSV_BeadSidesBeadSides_ = ConSV_BeadSidesBeadSides_.drop('index', axis = 1)
ConSV_FoamBeadSides_ = ConSV_FoamBeadSides_.reset_index()
ConSV_FoamBeadSides_ = ConSV_FoamBeadSides_.drop('index', axis = 1)
ConSV_FoamPlateBottom_ = ConSV_FoamPlateBottom_.reset_index()
ConSV_FoamPlateBottom_ = ConSV_FoamPlateBottom_.drop('index', axis = 1)
ConSV_FoamPlateTop_ = ConSV_FoamPlateTop_.reset_index()
ConSV_FoamPlateTop_ = ConSV_FoamPlateTop_.drop('index', axis = 1)
ConSV_PlateBottomBeadMiddle_ = ConSV_PlateBottomBeadMiddle_.reset_index()
ConSV_PlateBottomBeadMiddle_ = ConSV_PlateBottomBeadMiddle_.drop('index', axis = 1)
ConSV_PlateBottomBeadSides_ = ConSV_PlateBottomBeadSides_.reset_index()
ConSV_PlateBottomBeadSides_ = ConSV_PlateBottomBeadSides_.drop('index', axis = 1)
ConSV_PlateTopBeadMiddle_ = ConSV_PlateTopBeadMiddle_.reset_index()
ConSV_PlateTopBeadMiddle_ = ConSV_PlateTopBeadMiddle_.drop('index', axis = 1)
ConSV_PlateTopBeadSides_ = ConSV_PlateTopBeadSides_.reset_index()
ConSV_PlateTopBeadSides_ = ConSV_PlateTopBeadSides_.drop('index', axis = 1)
for j_ in range(start_sensors_, n_sensors_):
    sensors_[j_] = sensors_[j_].reset_index()
    sensors_[j_] = sensors_[j_].drop('index', axis = 1)

#%%

#%%
print('done')
#%%

