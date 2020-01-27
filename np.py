#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 13:00:47 2018

@author: Mengxi Shen
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use("ggplot")

data = np.load("pop2010.npy")
# normalize data for y-axis
data.sort()
ydata = data.cumsum()/data.sum()
# normalize data for x-axis
xdata = np.arange(data.size)
nxdata = xdata/data.size
# draw and save the graph
plt.xlabel('countires')
plt.ylabel('common poulation')
plt.title('population-lorenz')
plt.plot(nxdata,ydata)
plt.savefig('population-lorenz', dpi=200)