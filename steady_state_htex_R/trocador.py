# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 11:44:52 2018

@author: Bruno Carlos
"""

def rapzero (f, chute, tol= 10^-5):
    
    from scipy.misc import derivative
    
    xn = chute
    i = 1
    
    while (abs(f(xn)) > tol):
    
    xn = xn - (f(xn))/(derivative(f,xn))
    
