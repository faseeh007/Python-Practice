#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:41:03 2019

@author: abhishekbodapati
"""

n=int(input("Enter number of elements in list:\n"))
print("Enter elements:")
l1=[]
for i in range(n):
    a=int(input())
    l1.append(a)
print("Entered list is",l1)
m=int(input("Enter no. of elements to be deleted:\n"))
for j in range(m):
    l1.pop()
print("List after deleting is",l1)