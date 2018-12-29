# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 01:25:00 2018

@author: Bruno Carlos
"""
def htex(Tsf, Ff, Fq, U = 250,A = 1.61, Teq= 500,Tef= 280,Cpq= 2090,  Cpf= 4180,pf = 1000,  pq = 800):
    
    import math
       
    f = Ff*Cpf*pf
    q = Fq*Cpq*pq
    e = q*Teq + f*Tef
    
    return(Tsf - Tef - (U*A/f)*((((e - f*Tsf)/q - Tef) - (Teq - Tsf))/math.log(((e - f*Tsf)/q - Tef)/(Teq - Tsf))))   