import numpy as np
import random

    n= input("n= ")
def matran(n):
    M = np.random.randint(10, size=(n, n))
    return M
    print(M)
def định_thức():    
    Đ = np.linalg.det(M)
    return Đ
def rank_matran(M):
    R = np.linalg.matrix_rank(matran(n))
    return R
def luy_thua(M):
    a= matran(n)
    x= M.dot(a)
    y= M.dot(a).dot(a)
    return x, y
print("ma trận: ",matran(n))
print("định thức:",dinh_thuc(M))
print("rank:",rank_matran(M))
print("A^2:", x)
print()