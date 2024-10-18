import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


Kp = 0.15
Kd = 0.6
error0 = 0

def controller( t, reference, observation_t, error0, Kp, Kd):
    
    #observation_t = self.plant.get_depth()
    
    error1 = reference[t] - observation_t
    actions = Kp * error1 + Kd * (error1 - error0)
    error0 = error1
    return actions, error0
    
    