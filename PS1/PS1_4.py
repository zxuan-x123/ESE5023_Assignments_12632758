# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:00:14 2026

@author: Z-xuan
"""

#4.加1或者翻倍
def Least_moves(x):
    move = 0
    current = x
    while current > 1:
        if current % 2 == 1: #奇数，逆向只能减1
            current = current - 1
        else: #偶数，逆向除以2
            current = current // 2
        move += 1
    return move

print(Least_moves(2))
print(Least_moves(5))
