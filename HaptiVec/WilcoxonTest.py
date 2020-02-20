# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:01:39 2018

@author: Daniel
"""

import numpy as np
from scipy import stats

NL = np.array([100, 90, 100, 90, 30, 100, 100, 90, 90, 100])
NW = np.array([100, 40, 100, 80, 60, 100, 90, 100, 100, 100])
W = np.array([90, 40, 70, 100, 50, 100, 80, 100, 100, 90])
SW = np.array([100, 80, 60, 80, 80, 100, 100, 100, 100, 100])
SL = np.array([80, 90, 80, 100, 100, 100, 100, 90, 100, 100])
SR = np.array([100, 100, 100, 100, 100, 100, 70, 60, 90, 100])
SE = np.array([80, 40, 100, 100, 90, 100, 60, 100, 80, 60])
E = np.array([80, 40, 100, 100, 90, 100, 60, 100, 80, 60])
NE = np.array([100, 50, 90, 90, 70, 100, 100, 100, 90, 100])
NR = np.array([100, 90, 80, 70, 50, 100, 100, 100, 100, 100])

chance_level = np.array([20, 20, 20, 20, 20, 20, 20, 20, 20, 20])

hi = stats.wilcoxon(NR,chance_level)