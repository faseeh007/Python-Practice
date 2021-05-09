#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:50:12 2019

@author: abhishekbodapati
"""

n = int(input("Enter num"))
l1=[]
l2=[]
l3=[]
m=n
for i in range(n):
    x=int(input("enter"))
    l1.append(x)
print("l1 is",l1)
for i in range(1,n+1):
    y=l1[-i]
    l2.append(y)
print("l2 is ",l2)
for j in range(m):
    z=l1[j]+l2[j]
    l3.append(z)
print("after adding",l3)
    