# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 10:59:24 2018

@author: Bruno Carlos
"""

from sympy import symbols, diff
x, y, a = symbols('x y a', real=True)
d = diff( x**2 + y**3 + a*y, y)



diff( x**2 + y**3 + a*y, y).subs({x:3, y:1, a:1})




lambdasq = 0.09
Ca = 3
qOsq = 2




