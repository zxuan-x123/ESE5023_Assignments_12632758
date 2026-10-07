# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:59:53 2026

@author: Z-xuan
"""

#3.帕斯卡三角
#(1)Numpy
import numpy as np

def Pascal_triangle(k):
    arr = np.zeros((k, k))

    arr[:, 0] = 1

    for i in range(1, k):
        arr[i][i] = 1

        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    return arr

k_100 = Pascal_triangle(100)
for i in range(100):
    print(k_100[i, :i+1])
    
k_200=Pascal_triangle(200)

#(2)列表嵌套
def Pascal_triangle_1(k):
    triangle = []
    
    for i in range(k):
        row = [1] * (i + 1) #行
               
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j] #列
        
        triangle.append(row)
    
    return triangle

k1_100 = Pascal_triangle_1(100)
for row in k1_100:
    print(row)