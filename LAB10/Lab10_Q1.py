#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:34:11 2021

@author: alphantulukcu
"""
#%%
import matplotlib.pyplot as pl
import numpy as np

initial = np.array([30,35,40,45,50,55,60,65,70])
bounce = np.array([22,26,29,34,38,40,45,50,52])

fit = np.polyfit(initial, bounce, 1)
pvalue = np.polyval(fit, initial)

pl.clf()
pl.plot(initial, bounce, 'bo', initial, pvalue, "r-")
pl.xlabel('Initial Height')
pl.ylabel('Bounce Height')
pl.title('Initial Height vs. Bounce Height')
pl.legend(['data','trendline'])
# %%
