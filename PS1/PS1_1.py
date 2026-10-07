# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:22:44 2026

@author: Z-xuan
"""

#1.流程图
import random
a=random.randint(0,100)
b=random.randint(0,100)
c=random.randint(0,100)

def Deter_size(a, b, c):
    if a > b:
        if b > c:
            return a, b, c      
        else:
            if a > c:
                return a, c, b  
            else:
                return c, a, b  
    else:
        if a > c:
            return b, a, c      
        else:
            if b > c:
                return b, c, a  
            else:
                return c, b, a 

result = Deter_size(a, b, c)
print(f"a={a}, b={b}, c={c}")
print(f"{result}")
