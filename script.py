import netCDF4                        
import xarray as xr                                           
import os
import numpy as np
import matplotlib.pyplot as plt

parent_dir = os.getcwd()
file_path = os.path.join(parent_dir, 'filepath/data/')
files = [item for item in os.listdir(file_path) if not item.startswith('.')]
datasets = [xr.open_dataset('/filepath/data/' + file) for file in files]
print(files)
print("processing to csv")
for i in range(len(datasets)):
    variableName = datasets[i]['ColName'] 
    variableName.to_pandas().to_csv('filepath/csv' + datasets[i].attrs['time_coverage_start'][:7] + '-fileName.csv') 

#Example for multiple Chlorophyll files:
# for i in range(len(datasets)):
#     chlor = datasets[i]['chlor_a'] 
#     chlor.to_pandas().to_csv('filepath/csv' + datasets[i].attrs['time_coverage_start'][:7] + '-fileName.csv') 