import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from dynamic import *
from control import *

mission = Mission.from_csv('mission.csv')
print (mission)