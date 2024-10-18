import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt


def from_csv(file_name):
        mission = pd.read_csv(file_name)
        #reference = mission['reference']
        #cave_height = mission['cave_height']
        #cave_depth = mission['cave_depth']
        return mission

        
    
#mission = from_csv('mission.csv')
#print (mission)

#file = pd.read_csv('mission.csv')
#reference = file['reference']
#print (reference)