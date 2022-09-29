# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 22:26:54 2022

@author: David
"""
import numpy as np

def algFib(n):
    matRec = [[1,1],[1,0]]
    matAct = matrix_power(matRec, n)
    fib_n = int(matAct[1][0])
    return fib_n

# Hasta 1475 sin overflow
def matrix_power(a, power):
    if power == 0:
        return np.eye(len(a),len(a[1]))
    if power == 1:
        return a
    rows, columns = len(a), len(a[0])
    result = np.zeros((rows, columns))
    b = a
    for step in range(1, power):
        result = np.zeros((rows, columns)) # reset result to all zeroes matrix here
        for i in range(0, rows):
            for j in range(0, columns):
                for m in range(0, rows):
                    result[i][j] += a[i][m] * b[m][j]
        a = result
    return result