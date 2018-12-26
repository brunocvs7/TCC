# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:58:33 2018

@author: Bruno Carlos
"""

def derivada_htex(Tsf, Ff, Fq, U = 250,A = 1.61, Teq= 500,Tef= 280,Cpq= 2090,  Cpf= 4180,pf = 1000,  pq = 800):
    import math
    
      
    f = Ff*Cpf*pf
    q = Fq*Cpq*pq
    e = q*Teq + f*Tef
    
    
    return(1 + (U * A/f) * ((f/q - 1)/math.log(((e - f * Tsf)/q - Tef)/(Teq - 
    Tsf)) - (((e - f * Tsf)/q - Tef) - (Teq - Tsf)) * ((f/q/(Teq - 
    Tsf) - ((e - f * Tsf)/q - Tef)/(Teq - Tsf)**2)/(((e - f * 
    Tsf)/q - Tef)/(Teq - Tsf)))/math.log(((e - f * Tsf)/q - Tef)/(Teq - 
    Tsf))**2))