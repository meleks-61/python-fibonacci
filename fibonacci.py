# -*- coding: utf-8 -*-
"""fibonacci

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1haPa-_FC5jny3ylOGyPNZrTDzNuOUajX
"""

list = []#Fibonacci
n = 0
for i in range(10):
  if (i==0) or (i==1):
    n = 1
    list.append(n)
  else:
    n += list[i-2]
    list.append(n)
print("here,Fibonacci's first ten numbers:",list)