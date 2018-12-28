# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 01:12:21 2018

@author: Bruno Carlos
"""
import numpy as np
from htex import htex
from rapzero_htex import rapzero_htex
from derivada_htex  import derivada_htex

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

pf = 1000
pq = 800
Cpf  = 4180
Cpq = 2090

i = 0
j = 0
Teq = 420
Tef = 280
U = 250
A = 5
Ff = np.linspace(0.201,30,100)
Fq = np.linspace(0.5, 30,100)
Ff = Ff/pf
Fq = Fq/pq
Ff, Fq = np.meshgrid(Ff,Fq)
#Ff = np.array([1])
#Fq = np.array([1])

Tsf = np.zeros((len(Ff),len(Fq)))
Tsq = np.zeros((len(Ff),len(Fq)))

for i in range(len(Fq)):
    
    for j in range(len(Fq)):
        
        xf = Ff[i,j]
        xq = Fq[i,j]
        f = xf*Cpf*pf
        q = xq*Cpq*pq
        e = q*Teq + f*Tef
        Tsf[i,j] = rapzero_htex(htex,derivada_htex,200, xf, xq)
        Tssf = Tsf[i,j]
        Tsq[i,j] = (e - f*Tssf)/q
        
    j = 0
    
    

fig = plt.figure()
ax = fig.gca(projection='3d')   
surf = ax.plot_surface(Ff, Fq, Tsq, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0, 500)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')   
surf1 = ax1.plot_surface(Ff, Fq, Tsf, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax1.set_zlim(0, 500)
ax1.zaxis.set_major_locator(LinearLocator(10))
ax1.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig1.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

