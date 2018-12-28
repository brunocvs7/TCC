# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 21:42:38 2018

@author: Bruno Carlos
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def exe (x,t):
    
    
    y1 = x[0]
    y2 = x[1]
    
    dy1dt = (4 - y1 -y2)**2
    dy2dt = (y1 + y2)**2

    return(dy1dt, dy2dt)


y0 = [1,1]
t = np.linspace(0,5,1000)

x = odeint(exe, y0, t)

y1 = x[:,0]
y2 = x[:,1]


plt.plot(t,y1)



    