# coding: utf-8

import pymysql
import xlrd,xlwt
import os
import multiscale_entropy as me
import numpy as np


workbook = xlrd.open_workbook("实验数据-各流型的液膜厚度.xlsx")
sheet_name = workbook.sheet_names()

sheet = workbook.sheet_by_name(sheet_name[4])  # sheet number
a = sheet.col(2)  # column number
t = 6  # scale size

print(1)
b = []
for i in range(len(a)):
    b.append(a[i].value)
print(2)
# u = np.array(b[:3000])
U0 = np.array(b[:1000])
U1 = np.array(b[1000:2000])
U2 = np.array(b[2000:3000])
U3 = np.array(b[3000:4000])
U4 = np.array(b[4000:5000])
U5 = np.array(b[5000:6000])
U6 = np.array(b[6000:7000])
U7 = np.array(b[7000:8000])
U8 = np.array(b[8000:9000])
U9 = np.array(b[9000:10000])
print(3)
# print(me.SampEn(u, 3, 0.15))
print(me.multiscale_entropy(U0, 3, 0.15, t))
print(me.multiscale_entropy(U1, 3, 0.15, t))
print(me.multiscale_entropy(U2, 3, 0.15, t))
print(me.multiscale_entropy(U3, 3, 0.15, t))
print(me.multiscale_entropy(U4, 3, 0.15, t))
print(me.multiscale_entropy(U5, 3, 0.15, t))
print(me.multiscale_entropy(U6, 3, 0.15, t))
print(me.multiscale_entropy(U7, 3, 0.15, t))
print(me.multiscale_entropy(U8, 3, 0.15, t))
print(me.multiscale_entropy(U9, 3, 0.15, t))
