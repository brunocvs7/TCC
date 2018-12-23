# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 11:44:52 2018

@author: Bruno Carlos
"""
def rapzero_htex (f,df, chute, Ff,Fq, tol= 10**-5):
        
    xn = chute
    Ff = Ff
    Fq = Fq
    df= df
    f = f
        
    while (abs(f(xn, Ff, Fq)) > tol):
    
        xn = xn - (f(xn, Ff, Fq))/df(xn,Ff,Fq)
        
    
    return(xn)