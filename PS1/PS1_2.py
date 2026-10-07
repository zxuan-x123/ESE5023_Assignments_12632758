# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:59:41 2026

@author: Z-xuan
"""

#2.矩阵乘法
#2.1
import numpy as np

M1=np.random.randint(0,50,size=(5,10))
M2=np.random.randint(0,50,size=(10,5))

#2.2
def Matrix_multip(a, b):
    rows = a.shape[0]      
    cols = b.shape[1]      
    k_len = a.shape[1]

    arr = np.zeros((rows, cols))

    # 遍历结果的每一行
    for i in range(rows):
        # 遍历结果的每一列
        for j in range(cols):
            # 把第 i 行和第 j 列对应位置相乘再累加
            s = 0
            for k in range(k_len):
                s += a[i][k] * b[k][j]
            arr[i][j] = s

    return arr

result = Matrix_multip(M1, M2)
print("结果形状：", result.shape)
print(result)
