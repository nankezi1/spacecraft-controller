
import pandas as pd
import numpy as np

df = pd.read_csv('Positions.csv', header=None)

t = np.array(df[0])
x1 = np.array(df[1])
x2 = np.array(df[2])
x3 = np.zeros(np.size(x2))
x = np.array([x1, x2, x3])
x = x - x[:,0].reshape((3,1))
v = np.diff(x)
trajectory = {'xd' : x, 
             'xdotd' : v,
             't' : t}

