# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:20:43 2023

@author: DELL
"""
import numpy as np
# =============================================================================
# print(np)
# =============================================================================
mylist=[1,2,3,4,5,6]
# =============================================================================
# print(mylist)
# =============================================================================
array = np.array(mylist,dtype=int)
# =============================================================================
# print(array)
# =============================================================================
# # =============================================================================
# =============================================================================
# =============================================================================
# # =============================================================================
# =============================================================================
# print(type(array))
# =============================================================================
# =============================================================================
# print(len(array))
# =============================================================================
# =============================================================================
# print(array.ndim)
# =============================================================================
# =============================================================================
# print(array.shape)
# =============================================================================

array2=array.reshape(3,2)
# =============================================================================
# print(array2)
# =============================================================================

array3=array2.reshape(3,-1)
# =============================================================================
# print(array3.ndim)
# =============================================================================

mylist2=[1,2,3]
mylist3=[4,5,6]
m ylist4=[9,7,8]
mul_arra=np.array([mylist2,mylist3,mylist4])
# =============================================================================
# print(mul_arra)
# =============================================================================
r =range(24)
# =============================================================================
# print(r)
# =============================================================================





