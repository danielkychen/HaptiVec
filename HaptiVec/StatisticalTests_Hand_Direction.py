# -*- coding: utf-8 -*-
"""
Created on Tue Jan 01 21:50:15 2019

@author: Daniel
"""

#This Script is for analysing any differences between directions
#and handedness of participants
from scipy.stats import friedmanchisquare

#Import data for each direction
NL = [100, 90, 100, 90, 30, 100, 100, 90, 90, 100]
NW = [100, 40, 100, 80, 60, 100, 90, 100, 100, 100]
W = [90, 40, 70, 100, 50, 100, 80, 100, 100, 90]
SW = [100, 80, 60, 80, 80, 100, 100, 100, 100, 100]
SL = [80, 90, 80, 100, 100, 100, 100, 90, 100, 100]
SR = [100, 100, 100, 100, 100, 100, 70, 60, 90, 100]
SE = [100, 40, 50, 100, 100, 90, 100, 80, 30, 100]
E = [80, 40, 100, 100, 90, 100, 60, 100, 80, 60]
NE = [100, 50, 90, 90, 70, 100, 100, 100, 90, 100]
NR = [100, 90, 80, 70, 50, 100, 100, 100, 100, 100]

#Perform friedman's test on the directions
stat, p = friedmanchisquare(NL, NW, W, SW, SL, SR, SE, E, NE, NR)

print('Statistics=%.3f, p=%.3f' % (stat, p))

#------------------------------------------------------------------------#

#Remove the 2 left-handers from sample and redo friedman's test
NL = [100, 90, 30, 100, 100, 90, 90, 100]
NW = [100, 40, 100, 80, 60, 100, 90, 100]
W = [90, 40, 70, 100, 50, 100, 80, 100]
SW = [100, 80, 60, 80, 80, 100, 100, 100]
SL = [80, 100, 100, 100, 100, 90, 100, 100]
SR = [100, 100, 100, 100, 100, 100, 70, 90]
SE = [100, 40, 50, 100, 100, 90, 30, 100]
E = [80, 40, 100, 100, 90, 100, 60, 60]
NE = [100, 50, 90, 90, 70, 100, 90, 100]
NR = [100, 90, 80, 70, 50, 100, 100, 100]

stat, p = friedmanchisquare(NL, NW, W, SW, SL, SR, SE, E, NE, NR)

print('Statistics=%.3f, p=%.3f' % (stat, p))

#------------------------------------------------------------------------#

