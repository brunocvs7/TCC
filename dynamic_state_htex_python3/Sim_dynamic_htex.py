# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 21:50:02 2018

@author: Bruno Carlos
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


def dhtex (y,t):
    
    Tf1 = 280
    Tq1 = 375
    U = 250
    A = 1.61
    Tf = y0[0]
    Tq = y0[1]
    pf = 1000
    pq = 800
    Ff = 0.201/pf
    Fq =0.5/pq
    
    
    dTfdt = Ff*Tf - Ff*Tf1 + (U*A*((Tq - Tf1) - (Tq1 - Tf)))/math.log((Tq - Tf1)/(Tq1 - Tf))
    dTqdt = Fq*Tq - Fq*Tq1 + (U*A*((Tq - Tf1) - (Tq1 - Tf)))/math.log((Tq - Tf1)/(Tq1 - Tf))
    

    return(dTfdt, dTqdt)


y0 = [290,360]
t = np.linspace(0,15,1000)

x = odeint(dhtex, y0, t)

Tf = x[:,0]
Tq = x[:,1]


plt.plot(t,Tf)