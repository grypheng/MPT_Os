#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:42:52 2022

@author: gryphengoss
"""

#%%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

data = "/Users/gryphengoss/Desktop/IODP_1302_1308/IODP-Master_Goss.xlsx"

#Load spreadsheet
IODPdata = pd.ExcelFile(data)

#Print the sheet names
print(IODPdata.sheet_names)

#parse sheets
ar1302 = IODPdata.parse('1302-AquaR')
ch1302 = IODPdata.parse("1302-Chromic")
ar1308 = IODPdata.parse("1308-AquaR")
ch1308 = IODPdata.parse("1308-Chromic")
d18O = IODPdata.parse('d18O')
newsamps = IODPdata.parse('Current_Requests')

#create variables
d18Oval = d18O['d18Ovaluepermil']
d18Oage = d18O['d18O age']

ar1302a = ar1302['Age Increment']
ar1302os = ar1302['187Os/188Os']
ch1302a = ch1302['Age Increment']
ch1302os = ch1302['187Os/188Os']

ar1308a = ar1308['Age Increment']
ar1308os = ar1308['187Os/188Os']
ch1308a = ch1308['Age Increment']
ch1308os = ch1308['187Os/188Os']

new1308os = newsamps['1308Placer']
new1308a = newsamps['1308Age']
new1302os = newsamps['1302Placer']
new1302a = newsamps['1302Age']


#%%
#Only 1302 plot ###############################################################
ax111 = plt.subplot(111)
ax111.plot(ch1302a,ch1302os, color='black', marker = '.', label = "1302 Chromic")     
font = {'family' : 'normal',
             'size'   : 12}
plt.rc('font', **font)
#ax111.plot(ar1302a,ar1302os, color='black', linestyle = 'dashed', marker = '.',label = "1302 Inverse Aqua Regia")
plt.ylabel('187Os / 188Os')
#ax111.legend()
ax111.set_ylim(0,2.5)
plt.xlabel('Age (ka)')
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
plt.annotate('1302 (Proximal)', 
             xy=(588, 2.4), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)
left, bottom, width, height = (630, 0, 60, 2.5)
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()


#%%
#Only 1308 plot ###############################################################
ax222 = plt.subplot(111)
ax222.plot(ch1308a,ch1308os, color='black', marker = '.', label = "1308 Chromic")
font = {'family' : 'normal',
             'size'   : 12}
plt.rc('font', **font)
#ax222.plot(ar1308a,ar1308os, color='black', linestyle = 'dashed', marker = '.', label = "1308 Inverse Aqua Regia")
plt.ylabel('187Os / 188Os')
#ax222.legend()
ax222.set_ylim(0,2.5)
plt.xlabel('Age (ka)')
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
plt.annotate('1308 (Distal)', 
             xy=(488, 2.4), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)
left, bottom, width, height = (630, 0, 60, 2.5)
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()




#%%
#Stack of all three plots #####################################################

ax1 = plt.subplot(311)
ax1.plot(d18Oage,d18Oval, color='black', marker = '', label = "d18O")
font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)
plt.ylabel('d18O (LR04)')
plt.title('IODP Sites 1302 and 1308 - Osmium Signature')
ax1.get_xaxis().set_visible(False)
ax1.set_ylim(5.5, 3) 
#ax1.set_ylim(525,1001) 
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
plt.annotate('d18O', 
             xy=(1175, 5.25), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)
ax1.text(420,3.21,'MIS 11',size=9)
ax1.text(440,5.26,'12',size=9)
ax1.text(499,3.43,'13',size=9)
ax1.text(551,4.67,'14',size=9)
ax1.text(583,3.39,'15',size=9)
ax1.text(630,5.2,'16',size=9)
ax1.text(700,3.6,'17',size=9)
ax1.text(720,4.9,'18',size=9)
ax1.text(784,3.4,'19',size=9)
ax1.text(800,5.0,'20',size=9)
ax1.text(862,3.4,'21',size=9)
ax1.text(882,4.8,'22',size=9)
ax1.text(910,3.85,'23',size=9)
ax1.text(924,4.6,'24',size=9)
ax1.text(959,3.3,'25',size=9)
ax1.text(970,4.67,'26',size=9)
ax1.text(989,3.64,'27',size=9)
ax1.text(998,4.39,'28',size=9)
ax1.text(1028,3.49,'29',size=9)
ax1.text(1044,4.60,'30',size=9)
ax1.text(1077,3.20,'31',size=9)
ax1.text(1094,4.41,'32',size=9)
ax1.text(1114,3.63,'33',size=9)
ax1.text(1130,4.54,'34',size=9)
ax1.text(1170,3.39,'35',size=9)
ax1.text(1201,4.47,'36',size=9)


left, bottom, width, height = (406, 6, 30, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (492, 6, 48, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (612, 6, 18, -3)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect1)
left, bottom, width, height = (697, 6, 25, -3)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect2)
left, bottom, width, height = (782, 6, 15, -3)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect3)
left, bottom, width, height = (861, 6, 21, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (956, 6, 11, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1023, 6, 16, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1074, 6, 23, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1111, 6, 15, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1184, 6, 15, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)



ax2 = plt.subplot(312, sharex = ax1)
ax2.plot(ch1302a,ch1302os, color='black', marker = '.', label = "1302") 
ax2.plot(new1302a,new1302os, color='red', marker = 'o', label = "New 1302")   
font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)  
#ax2.plot(ar1302a,ar1302os, color='black', linestyle = 'dashed', marker = '.')
plt.ylabel('187Os / 188Os')
#ax2.legend()
ax2.set_ylim(0,2.5)
ax2.get_xaxis().set_visible(False)
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
plt.annotate('1302 (Proximal)', 
             xy=(1175, 0.25), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)

left, bottom, width, height = (406, 0, 30, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (492, 0, 48, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (612, 0, 18, 2.5)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect1)
left, bottom, width, height = (697,0, 25, 2.5)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect2)
left, bottom, width, height = (782, 0, 15, 2.5)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect3)
left, bottom, width, height = (861, 0, 21, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (956, 0, 11, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1023, 0, 16, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1074, 0, 23, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1111, 0, 15, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1184, 0, 15, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)




ax3 = plt.subplot(313, sharex = ax1)
ax3.plot(ch1308a,ch1308os, color='black', marker = '.', label = "1308") 
ax3.plot(new1308a,new1308os, color='red', marker = 'o', label = "New 1308") 
font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)    
#ax3.plot(ar1308a,ar1308os, color='black', linestyle = 'dashed', marker = '.', label = "Inverse Aqua Regia")
plt.ylabel('187Os / 188Os')
#ax3.legend()
#ax3.get_xaxis().set_visible(False)
ax3.set_ylim(0,2.5)
plt.xlabel('Age (ka)')
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
plt.annotate('1308 (Distal)', 
             xy=(1175, 0.25), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)
left, bottom, width, height = (406, 0, 30, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (492, 0, 48, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (612, 0, 18, 2.5)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect1)
left, bottom, width, height = (697,0 , 25, 2.5)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect2)
left, bottom, width, height = (782, 0, 15, 2.5)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect3)
left, bottom, width, height = (861, 0, 21, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (956, 0, 11, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1023, 0, 16, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1074, 0, 23, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1111, 0, 15, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (1184, 0, 15, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)


plt.subplots_adjust(wspace=0, hspace=0)
plt.show()

#%%
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
import numpy as np
import scipy.stats
from scipy.stats import pearsonr
import seaborn as sns

x = (3.89,3.39,3.5,4.31,3.88,3.88,3.88,4.9,5.05,4.8,4.75,4.68,4.75,4.79,4.79,4.77,4.64,4.5,4.4,
     3.64,3.84,4.61,4.32,4.02,4.17,4.17,4.67,4.11,4.11,3.48,3.9,4.07,3.63,4.06,4.59)
y = ch1302os




pyplot.scatter(x,y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"b")
pyplot.show()



#%%
#Zones of red interglacial and blue glacial based on Os##################################

ax1 = plt.subplot(211)
ax1.plot(d18Oage,d18Oval, color='black', marker = '', label = "d18O")
font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)
plt.ylabel('d18O (LR04)')
plt.title('IODP Sites 1302 and 1308 - Osmium Signature')
ax1.get_xaxis().set_visible(True)
ax1.set_ylim(5.5, 3) 
ax1.set_xlim(570.5,879) 
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
plt.annotate('d18O', 
             xy=(850, 5.25), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)

ax1.text(576,3.39,'MIS 15',size=9)
ax1.text(630,5.2,'16',size=9)
ax1.text(700,3.6,'17',size=9)
ax1.text(720,4.85,'18',size=9)
ax1.text(782,3.5,'19',size=9)
ax1.text(800,4.85,'20',size=9)
ax1.text(862,3.4,'21',size=9)
ax1.text(873,4.8,'22',size=9)



left, bottom, width, height = (571.6, 6, 12.7, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (584.3, 6, 42.4, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.4,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (626.7, 6, 10.9, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (637.6, 6, 11.2, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (648.4, 6, 27.7, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.4,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (676.11, 6, 17.4, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (693.51, 6, 10.9, -3)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect1)
left, bottom, width, height = (704.41,6, 21.7, -3)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.4,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect2)
left, bottom, width, height = (726.12, 6, 5.9, -3)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect3)
left, bottom, width, height = (732.2, 6, 12.8, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (745, 6, 16.6, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.4,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (761.8, 6, 59.5, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (821.3, 6, 11.4, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (832.71, 6, 20.3, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (853.01, 6, 24.7, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)



ax2 = plt.subplot(212, sharex = ax1)
ax2.plot(ch1302a,ch1302os, color='black', marker = '.', label = "1302")   
font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)  
#ax2.plot(ar1302a,ar1302os, color='black', linestyle = 'dashed', marker = '.')
plt.ylabel('187Os / 188Os')
#ax2.legend()
ax2.set_ylim(0,2.5)
ax2.get_xaxis().set_visible(True)
plt.xlabel('Age (ka)')
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
plt.annotate('1302 (Proximal)', 
             xy=(850, 0.25), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)
left, bottom, width, height = (571.6, 0, 12.7, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (584.3, 0, 42.4, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.4,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (626.7, 0, 10.9, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (637.6, 0, 11.2, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (648.4, 0, 27.7, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.4,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (676.11, 0, 17.4, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (693.51, 0, 10.9, 2.5)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect1)
left, bottom, width, height = (704.41,0, 21.7, 2.5)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.4,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect2)
left, bottom, width, height = (726.12, 0, 5.9, 2.5)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect3)
left, bottom, width, height = (732.2, 0, 12.8, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (745, 0, 16.6, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.4,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (761.8, 0, 59.5, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (821.3, 0, 11.4, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (832.71, 0, 20.3, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (853.01, 0, 24.7, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)

plt.subplots_adjust(wspace=0, hspace=0)
plt.show()

#%%
#Line d18O and scatter Os 1302
#Zones of red interglacial and blue glacial based on Os##################################

ax1 = plt.subplot(111)
ax1.plot(d18Oage,d18Oval, color='grey', marker = '', label = "d18O")
ax2 = ax1.twinx()
ax2.scatter(ch1302a,ch1302os, color='black', marker = 's', label = "1302")   
ax2.set_ylim(0,2.5)
font = {'family' : 'normal',
        'size'   : 15}
plt.rc('font', **font)
plt.ylabel('d18O (LR04)')
#plt.title('IODP Site 1302 - Osmium Signature')
ax1.set_ylim(5.5, 3) 
ax1.set_xlim(570.5,879) 
ax1.set_ylabel('d18O (LR04)')
ax2.set_ylabel('187Os / 188Os')
ax1.set_xlabel('Age (ka)')



#MIS labels
ax1.text(576,3.39,'MIS 15',size=15)
ax1.text(630,5.2,'16',size=15)
ax1.text(700,3.6,'17',size=15)
ax1.text(720,4.85,'18',size=15)
ax1.text(782,3.5,'19',size=15)
ax1.text(800,4.85,'20',size=15)
ax1.text(862,3.4,'21',size=15)
ax1.text(871,4.8,'22',size=15)

#Warming in red, cooling in blue
left, bottom, width, height = (571.6, 0, 12.7, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (584.3, 0, 42.4, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (626.7, 0, 10.9, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (637.6, 0, 11.2, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (648.4, 0, 27.7, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (676.11, 0, 17.4, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (693.51, 0, 10.9, 2.5)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect1)
left, bottom, width, height = (704.41,0, 21.7, 2.5)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect2)
left, bottom, width, height = (726.12, 0, 6.0, 2.5)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect3)
left, bottom, width, height = (732.1, 0, 12.8, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (745, 0, 16.8, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (761.8, 0, 59.5, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (821.3, 0, 11.4, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (832.71, 0, 20.3, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'blue',
                        linewidth = 2)
plt.gca().add_patch(rect4)
left, bottom, width, height = (853.01, 0, 24.7, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)


plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
