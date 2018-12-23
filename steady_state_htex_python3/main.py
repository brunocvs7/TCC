# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 01:12:21 2018

@author: Bruno Carlos
"""
import numpy as np
from htex import htex
from rapzero_htex import rapzero_htex
from derivada_htex  import derivada_htex
pf = 1000
pq = 800
Cpf  = 4180
Cpq = 2090
#Ff = np.arange(1, 100, 1)
#Fq = np.arange(1,100,1)
#Ff = np.array([0.201, 1])
#Fq = np.array([0.5, 1])


i = 0
j = 0
Teq = 375
Tef = 280
U = 250
A = 1.61
Ff = np.arange(0.201,0.5,0.1)
Fq = np.arange(0.5,1.5,0.1)
#Ff = np.array([1])
#Fq = np.array([1])
Ff = Ff/pf
Fq = Fq/pq
Tsf = np.zeros((len(Ff),len(Fq)))
Tsq = np.zeros((len(Ff),len(Fq)))
for xf in Ff:
    
    
    for xq in Fq:
        f = xf*Cpf*pf
        q = xq*Cpq*pq
        e = q*Teq + f*Tef
        Tsf[i,j] = rapzero_htex(htex,derivada_htex,200, xf, xq)
        Tssf = Tsf[i,j]
        Tsq[i,j] = (e - f*Tssf)/q
        j = j+1

    i = i+1
    
    j = 0


