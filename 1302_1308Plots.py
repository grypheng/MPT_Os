#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:42:52 2022

@author: gryphengoss
"""

#%% Import data
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import style
from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot
import numpy as np
from matplotlib import gridspec

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
#newsamps = IODPdata.parse('Current_Requests')
SLsheet = IODPdata.parse("SeaLevel")
CO2sheet = IODPdata.parse("pCO2")

#create variables
#d18Oval = d18O.iloc[:,1] If the below line does work locate using integer position
d18Oval = d18O['d18Ovalpm']
d18Oage = d18O['d18O age']
d18Oerr = d18O['error']

ar1302a = ar1302['Age Increment']
ar1302os = ar1302['187Os/188Os']
ch1302a = ch1302['Age Increment']
ch1302os = ch1302['187Os/188Os']
ch1302ppt = ch1302['192Os(ppt)']
ch1308ppt = ch1308['192Os(ppt)']
ch1302err =ch1302['OsError']
ch1308err =ch1308['OsError']

ar1308a = ar1308['Age Increment']
ar1308os = ar1308['187Os/188Os']
ch1308a = ch1308['Age Increment']
ch1308os = ch1308['187Os/188Os']

#new1308os = newsamps['1308Placer']
#new1308a = newsamps['1308Age']
#new1302os = newsamps['1302Placer']
#new1302a = newsamps['1302Age']

SLdata = SLsheet['SL']
SLa = SLsheet['Time']
SLup = SLsheet['SL_upper']
SLlo = SLsheet['SL_lower']

CO2data = CO2sheet['pCO2']
CO2a = CO2sheet['Time']
CO2up = CO2sheet['pCO2_upper']
CO2lo =CO2sheet['pCO2_lower']


#%% only 1302 and d18O
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


#%% only 1308 and d18O
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




#%% 3 Rows: 1302 1308 and d18O all stacked
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

#%% Os ratio 

x = 1/ch1302ppt
y = ch1302os

x.dropna(inplace=True)
y.dropna(inplace=True)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--", color='black')
plt.scatter(x,y, color='white', marker = 'o', label = "1302", edgecolors='black')
plt.xlabel('1 / 192Os')
plt.ylabel('187Os / 188Os')
plt.yticks([0,1,2,3],['0','1','2','3'])
plt.xticks([.02,0.04,0.06,0.08,0.1],['0.02','0.04','0.06','0.08','0.1'])

plt.show   


#%% 1302 d18O separate plots red and blue
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

#%% Line d18O and scatter Os 1302 red and blue-overlayed
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
ax1.set_xlim(565,880) 
ax1.set_ylabel('d18O (LR04)')
ax2.set_ylabel('187Os / 188Os')
ax1.set_xlabel('Age (ka)')



#MIS labels
ax1.text(600,3.45,'MIS 15',size=15)
ax1.text(630,5.15,'16',size=15)
ax1.text(700,3.55,'17',size=15)
ax1.text(720,4.85,'18',size=15)
ax1.text(782,3.5,'19',size=15)
ax1.text(800,4.85,'20',size=15)
ax1.text(862,3.45,'21',size=15)
ax1.text(871,4.8,'22',size=15)

#Warming in red, cooling in blue
left, bottom, width, height = (565, 0, 19.5, 2.5)
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
left, bottom, width, height = (648.8, 0, 27.7, 2.5)
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
left, bottom, width, height = (744.9, 0, 16.8, 2.5)
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
left, bottom, width, height = (853.01, 0, 27, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)


plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
#%% 5 columns: of d18o 1302 os/ppt and 1308 os/ppt

ax1 = plt.subplot(151)
ax1.plot(d18Oval,d18Oage, color='black', marker = '', label = "d18O")
font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)
#plt.ylabel('d18O (LR04)')
#plt.title('IODP Sites 1302 and 1308 - Osmium Signature')
ax1.get_xaxis().set_visible(True)
#ax1.set_ylim(5.5, 3) 
ax1.legend()
ax1.set_ylim(440,1300) 
bbox=dict(boxstyle="round", alpha=0.1, color='white')
plt.annotate('d18O', 
             xy=(850, 5.25), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)


ax2 = plt.subplot(152, sharey = ax1)
ax2.plot(ch1302os,ch1302a, color='black', marker = '.', label = "1302 - Os ratio")   
font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)  
#ax2.plot(ar1302a,ar1302os, color='black', linestyle = 'dashed', marker = '.')
#plt.ylabel('187Os / 188Os')
ax2.legend()
ax2.set_xlim(0,2.5)
ax2.get_yaxis().set_visible(False)
#plt.xlabel('Age (ka)')
bbox=dict(boxstyle="round", alpha=0.1, color='white')


ax3 = plt.subplot(153, sharey = ax1)
ax3.plot(ch1302ppt,ch1302a, color='black', marker = '.', label = "1302 - 192 ppt")   
font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)  
#ax2.plot(ar1302a,ar1302os, color='black', linestyle = 'dashed', marker = '.')
#plt.ylabel('187Os / 188Os')
ax3.legend()
ax3.set_xlim(0,55)
ax3.get_yaxis().set_visible(False)
#plt.xlabel('Age (ka)')
bbox=dict(boxstyle="round", alpha=0.1, color='white')

ax4 = plt.subplot(154, sharey = ax1)
ax4.plot(ch1308os,ch1308a, color='black', marker = '.', label = "1308 - Os ratio")   
font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)  
#ax2.plot(ar1302a,ar1302os, color='black', linestyle = 'dashed', marker = '.')
#plt.ylabel('187Os / 188Os')
ax4.legend()
ax4.set_xlim(0,2.5)
ax4.get_yaxis().set_visible(False)
#plt.xlabel('Age (ka)')
bbox=dict(boxstyle="round", alpha=0.1, color='white')

ax5 = plt.subplot(155, sharey = ax1)
ax5.plot(ch1308ppt,ch1308a, color='black', marker = '.', label = "1308 - 192 ppt")   
font = {'family' : 'normal',
        'size'   : 12}
plt.rc('font', **font)  
#ax2.plot(ar1302a,ar1302os, color='black', linestyle = 'dashed', marker = '.')
#plt.ylabel('187Os / 188Os')
ax5.legend()
ax5.set_xlim(0,55)
ax5.get_yaxis().set_visible(False)
#plt.xlabel('Age (ka)')
bbox=dict(boxstyle="round", alpha=0.1, color='white')


plt.subplots_adjust(wspace=0.05, hspace=0)
plt.show()

#%% 3 columns: of d18o LR04, outset: 1302 and 1308

fig = plt.figure(figsize=(7, 5))

#d18O top plot
ax1 = fig.add_subplot(3,1,1)
ax1.spines["top"].set_color("white")
ax1.spines["bottom"].set_color("grey")
ax1.spines["left"].set_color("grey")
ax1.spines["right"].set_color("grey")
ax1.plot(d18Oage,d18Oval, color='black', marker = '', linewidth=0.75, label = "d18O")
font = {'family' : 'normal',
        'size'   : 10}
plt.rc('font', **font)
plt.ylabel('d18O (LR04)')
#plt.title('IODP Sites 1302 and 1308 - Osmium Signature')
#ax1.get_xaxis().set_visible(False)
ax1.set_ylim(5.5, 2) 
ax1.invert_xaxis()
ax1.set_xlim(2000,0) 
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
left, bottom, width, height = (500, 5.25, 800, -2.3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        fill = False,
                        color = "black",
                        alpha = 0.3,
                      #  facecolor = 'black'
                        linewidth = 1)
plt.gca().add_patch(rect4)
#41ky-bars
left, bottom, width, height = (695, 2.5, 450, -0.1)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        fill = True,
                        color = "black",
                        alpha = 1,
                        facecolor = 'black',
                        linewidth = 1)
plt.gca().add_patch(rect4)
ax1.text(1035,2.3,'41 ky cycles',size=12)
#100ky-bars
left, bottom, width, height = (120, 2.5, 500, -0.1)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        fill = True,
                        color = "black",
                        alpha = 1,
                        facecolor = 'black',
                        linewidth = 1)
plt.gca().add_patch(rect4)
ax1.text(500,2.3,'100 ky cycles',size=12)




#1308 middle plot
ax2 = fig.add_subplot(3,1,2)
ax2.plot(ch1308a,ch1308os, color='black', marker = '.', linewidth=1,label = "1308")
ax2.invert_xaxis()
font = {'family' : 'normal',
        'size'   : 10}
plt.rc('font', **font)  
#ax2.plot(ar1302a,ar1302os, color='black', linestyle = 'dashed', marker = '.')
plt.ylabel('187Os / 188Os')
#ax2.legend()
#ax2.set_ylim(0,2)
ax2.set_yticks([0,1,2],['0','1','2'])
ax2.spines["top"].set_color("white")
ax2.spines["bottom"].set_color("grey")
ax2.spines["left"].set_color("grey")
ax2.spines["right"].set_color("grey")
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
left, bottom, width, height = (550, 0.25, 340, 1.65)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        fill = False,
                        color = "black",
                        alpha = 0.3,
                      #  facecolor = 'black'
                        linewidth = 1)
plt.gca().add_patch(rect4)
ax22 = ax2.twinx()
ax22.spines["top"].set_color("white")
ax22.spines["bottom"].set_color("grey")
ax22.spines["left"].set_color("grey")
ax22.spines["right"].set_color("grey")
ax22.plot(d18Oage,d18Oval, color='grey', marker = '', linewidth=0.5, label = "d18O")
#ax22.invert_xaxis()
ax22.invert_yaxis()
#ax22.set_ylim(5.5,3)
ax22.set_xlim(1267,410)
ax22.set_yticks([6,5,4,3],['6','5','4','3'])
plt.ylabel('d18O (LR04)')


#1302 bottom plot
ax3 = fig.add_subplot(3,1,3)
ax3.spines["top"].set_color("white")
ax3.spines["bottom"].set_color("grey")
ax3.spines["left"].set_color("grey")
ax3.spines["right"].set_color("grey")
ax3.plot(ch1302a,ch1302os, color='black', marker = '.', linewidth=1,label = "1302")
ax3.invert_xaxis()
font = {'family' : 'normal',
        'size'   : 10}
plt.rc('font', **font)    
#ax3.plot(ar1308a,ar1308os, color='black', linestyle = 'dashed', marker = '.', label = "Inverse Aqua Regia")
plt.ylabel('187Os / 188Os')
#ax3.legend()
#ax3.get_xaxis().set_visible(False)
#ax3.set_ylim(0,2.5)
ax3.set_yticks([0,1,2,3],['0','1','2','3'])
plt.xlabel('Age (ka)')
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
ax33 = ax3.twinx()
ax33.spines["top"].set_color("white")
ax33.spines["bottom"].set_color("grey")
ax33.spines["left"].set_color("grey")
ax33.spines["right"].set_color("grey")
ax33.plot(d18Oage,d18Oval, color='grey', marker = '', linewidth=0.5, label = "d18O")
ax33.invert_yaxis()
ax33.set_ylim(5.5,3)
ax33.set_yticks([6,5,4,3],['6','5','4','3'])
ax33.set_xlim(893,555)
plt.ylabel('d18O (LR04)')



######## first box lines
con1 = ConnectionPatch(xyA=(1300, 5.25), coordsA=ax1.transData, 
                       xyB=(1267, 2), coordsB=ax2.transData, color = 'black',alpha=0.3)
# Add left side to the figure
fig.add_artist(con1)
con2 = ConnectionPatch(xyA=(500, 5.25), coordsA=ax1.transData, 
                       xyB=(410, 2), coordsB=ax2.transData, color = 'black',alpha=0.3)
# Add right side to the figure
fig.add_artist(con2)

######### Second boxlines
con3 = ConnectionPatch(xyA=(889, 0.24), coordsA=ax2.transData, 
                       xyB=(893, 3), coordsB=ax3.transData, color = 'black',alpha=0.3)
# Add left side to the figure
fig.add_artist(con3)
con4 = ConnectionPatch(xyA=(550, 0.24), coordsA=ax2.transData, 
                       xyB=(555, 3), coordsB=ax3.transData, color = 'black', alpha=0.3)
# Add right side to the figure
fig.add_artist(con4)

fig.subplots_adjust(wspace=0.55, hspace=0.55)

#%% NEW 2 columns: 1302 SL Co2 D18O and 1308 ""

fig = plt.figure(figsize=(5, 5))



#1308
ax2 = fig.add_subplot(2,1,1)
ax2.plot(ch1308a,ch1308os, color='black', marker = '.', linewidth=1.5,label = "1308")
ax2.invert_xaxis()
font = {'family' : 'normal',
        'size'   : 10}
plt.rc('font', **font)  
#ax2.plot(ar1302a,ar1302os, color='black', linestyle = 'dashed', marker = '.')
#plt.ylabel('187Os / 188Os')
#ax2.legend()
#ax2.set_ylim(0,2)
ax2.set_yticks([0,1,2],['0','1','2'])

#bbox=dict(boxstyle="round", alpha=0.1, color='grey')
#left, bottom, width, height = (550, 0.25, 340, 1.65)
#rect4=mpatches.Rectangle((left,bottom),width,height, 
#                        fill = False,
#                        color = "black",
#                        alpha = 0.3,
                      #  facecolor = 'black'
#                        linewidth = 1)
#plt.gca().add_patch(rect4)
ax22 = ax2.twinx()

ax22.plot(d18Oage,d18Oval, color='grey', marker = '', linewidth=0.5, label = "d18O")
ax22.invert_yaxis()
ax22.set_ylim(5.5,3)
ax22.set_xlim(1267,410)
ax22.set_yticks([6,5,4,3],['6','5','4','3'])
ax222 = ax2.twinx()
ax222.spines['left'].set_position(('outward', 25))
ax222.plot(SLa,SLdata, color='blue', marker = '', linewidth=0.5, label = "Sea Level")

ax2222 = ax222.twinx()
ax2222.spines['right'].set_position(('outward', 25))
ax2222.plot(CO2a,CO2data, color='red', marker = '', linewidth=0.5, label = "pCO2")
#plt.ylabel('d18O (LR04)')


#1302 bottom plot
ax3 = fig.add_subplot(2,1,2)
ax3.plot(ch1302a,ch1302os, color='black', marker = '.', linewidth=1.5,label = "1302")
ax3.invert_xaxis()
font = {'family' : 'normal',
        'size'   : 10}
plt.rc('font', **font)    
#plt.ylabel('187Os / 188Os')
ax3.set_yticks([0,1,2,3],['0','1','2','3'])
plt.xlabel('Age (ka)')

ax33 = ax3.twinx()
ax33.plot(d18Oage,d18Oval, color='grey', marker = '', linewidth=0.5, label = "d18O")
ax33.invert_yaxis()
ax33.set_ylim(5.5,3)
ax33.set_yticks([6,5,4,3],['6','5','4','3'])
ax33.set_xlim(893,555)
#plt.ylabel('d18O (LR04)')

ax333 = ax3.twinx()
ax333.spines['left'].set_position(('outward', 25))
ax333.plot(SLa,SLdata, color='blue', marker = '', linewidth=0.5, label = "Sea Level")

ax3333 = ax333.twinx()
ax3333.spines['right'].set_position(('outward', 25))
ax3333.plot(CO2a,CO2data, color='red', marker = '', linewidth=0.5, label = "pCO2")


#plt.ylabel('pCO2')



######## first box lines


######### Second boxlines
#con3 = ConnectionPatch(xyA=(889, 0.24), coordsA=ax2.transData, 
#                       xyB=(893, 3), coordsB=ax3.transData, color = 'black',alpha=0.3)
# Add left side to the figure
#fig.add_artist(con3)
#con4 = ConnectionPatch(xyA=(550, 0.24), coordsA=ax2.transData, 
#                       xyB=(555, 3), coordsB=ax3.transData, color = 'black', alpha=0.3)
# Add right side to the figure
#fig.add_artist(con4)

fig.subplots_adjust(wspace=0.1, hspace=0.1)







#%% small 1308 on top, big 1302 with sl, co2, d18O


fig = plt.figure(figsize=(4, 7)) 
gs = gridspec.GridSpec(5, 1, height_ratios=[3.5,3,3,3,3]) 

#1308Plot
ax0 = plt.subplot(gs[0])
ax0.plot(ch1308a,ch1308os, color='black', marker = '.', linewidth=1.5,label = "1308")
ax0.invert_xaxis()
font = {'family' : 'normal',
        'size'   : 10}
plt.rc('font', **font)  
ax0.set_yticks([0,1,2],['0','1','2'])
plt.ylabel('187Os / 188Os')
ax0.xaxis.set_ticks_position('top')


ax00 = plt.subplot(gs[0])
ax00 = ax0.twinx()
ax00.invert_xaxis()
ax00.plot(d18Oage,d18Oval, color='grey', marker = '', linewidth=0.5, label = "d18O")
ax00.invert_yaxis()
plt.ylabel('d18O (LR04)')
ax00.set_ylim(5.8,3)
ax00.set_xlim(445,1230)
ax00.set_yticks([5.8,5,4,3],['','5','4','3'])
#Grey showing time of next plot
left, bottom, width, height = (570, 0, 320, 50)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        color = "grey",
                        alpha = 0.2,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect1)

#41ky-bars
left, bottom, width, height = (825, 5.5, 300, 0.02)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        fill = True,
                        color = "black",
                        alpha = 1,
                        facecolor = 'black',
                        linewidth = 1)
plt.gca().add_patch(rect4)
ax00.text(920,5.4,'41 ky cycles',size=10)

#100ky-bars
left, bottom, width, height = (500, 5.5, 300, 0.02)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        fill = True,
                        color = "black",
                        alpha = 1,
                        facecolor = 'black',
                        linewidth = 1)
plt.gca().add_patch(rect4)
ax00.text(595,5.4,'100 ky cycles',size=10)



#1302 Plot Osmium:
ax1 = plt.subplot(gs[1])
#ax1.plot(ch1302a,ch1302os, color='black', marker = '.', linewidth=1,label = "1302")
ax1.errorbar(ch1302a, ch1302os, xerr = ch1302err, elinewidth = 1, capsize=10, color = 'black')
ax1.invert_xaxis()
font = {'family' : 'normal',
        'size'   : 10}
plt.rc('font', **font)    
plt.ylabel('187Os / 188Os')
ax1.set_yticks([0,1,2,3],['0','1','2',''])
ax1.set_xlim(570,878)
ax1.get_xaxis().set_visible(False)
ax1.spines["top"].set_color("black")
ax1.spines["bottom"].set_color("white")
ax1.spines["left"].set_color("black")
ax1.spines["right"].set_color("black")
plt.xlabel('Age (ka)')
#Warming in red, cooling in blue
left, bottom, width, height = (600, 0, 30, 50)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect1)
#Warming in red, cooling in blue
left, bottom, width, height = (690, 0, 30, 50)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect2)
#Warming in red, cooling in blue
left, bottom, width, height = (770, 0, 30, 50)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect3)
#Warming in red, cooling in blue
left, bottom, width, height = (840, 0, 30, 50)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)

#d18O
ax11 = plt.subplot(gs[2])
#ax11.plot(d18Oage,d18Oval, color='grey', marker = '', linewidth=1, label = "d18O")
ax11.errorbar(d18Oage, d18Oval, xerr = d18Oerr, elinewidth = 1, capsize=10, color = 'grey')
ax11.yaxis.set_ticks_position('right')
ax11.yaxis.set_label_position("right")
ax11.invert_yaxis()
ax11.set_ylim(5.5,3)
ax11.set_yticks([5.5,5,4,3],['','5','4','3'])
ax11.set_xlim(570,878)
ax11.get_xaxis().set_visible(False)
ax11.spines["top"].set_color("white")
ax11.spines["bottom"].set_color("white")
ax11.spines["left"].set_color("black")
ax11.spines["right"].set_color("black")
plt.ylabel('d18O (LR04)')
#Warming in red, cooling in blue
left, bottom, width, height = (600, 0, 30, 50)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect1)
#Warming in red, cooling in blue
left, bottom, width, height = (690, 0, 30, 50)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect2)
#Warming in red, cooling in blue
left, bottom, width, height = (770, 0, 30, 50)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect3)
#Warming in red, cooling in blue
left, bottom, width, height = (840, 0, 30, 50)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)


#Sea Level
ax111 = plt.subplot(gs[3])
ax111.plot(SLa,SLdata, color='blue', marker = '', linewidth=1, label = "Sea Level")
#ax111.fill_between(x, SLup, SLlo)
ax111.set_xlim(570,878)
ax111.get_xaxis().set_visible(False)
ax111.spines["top"].set_color("white")
ax111.spines["bottom"].set_color("white")
ax111.spines["left"].set_color("black")
ax111.spines["right"].set_color("black")
plt.ylabel('Global Mean Sea Level (m)')
ax111.set_ylim(-120,0)
#Warming in red, cooling in blue
left, bottom, width, height = (600, 0, 30, -120)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect1)
#Warming in red, cooling in blue
left, bottom, width, height = (690, 0, 30, -120)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect2)#Warming in red, cooling in blue
left, bottom, width, height = (770, 0, 30, -120)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect3)
#Warming in red, cooling in blue
left, bottom, width, height = (840, 0, 30, -120)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)

ax111L = plt.subplot(gs[3])
ax111L.plot(SLa,SLup, color='blue', marker = '', linewidth=0.5, label = "Sea Level")
ax111L.set_xlim(570,878)
ax111L.get_xaxis().set_visible(False)
ax111L.spines["top"].set_color("white")
ax111L.spines["bottom"].set_color("white")
ax111L.spines["left"].set_color("black")
ax111L.spines["right"].set_color("black")
ax111L.set_ylim(-120,0)

ax111u = plt.subplot(gs[3])
ax111u.plot(SLa,SLlo, color='blue', marker = '', linewidth=0.5, label = "Sea Level")
ax111u.set_xlim(570,878)
ax111u.get_xaxis().set_visible(False)
ax111u.spines["top"].set_color("white")
ax111u.spines["bottom"].set_color("white")
ax111u.spines["left"].set_color("black")
ax111u.spines["right"].set_color("black")
ax111u.set_ylim(-120,0)


#pCO2
ax1111 = plt.subplot(gs[4])
ax1111.get_xaxis().set_visible(True)
ax1111.set_xlim(570,878)
ax1111.plot(CO2a,CO2data, color='red', marker = '', linewidth=1, label = "pCO2")
ax1111.yaxis.set_ticks_position('right')
ax1111.yaxis.set_label_position("right")
ax1111.spines["top"].set_color("white")
ax1111.spines["bottom"].set_color("black")
ax1111.spines["left"].set_color("black")
ax1111.spines["right"].set_color("black")
plt.ylabel('pCO2 (ppmv)')
ax1111.set_ylim(170,300)
#Warming in red, cooling in blue
left, bottom, width, height = (600, 170, 30, 300)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect1)
#Warming in red, cooling in blue
left, bottom, width, height = (690, 170, 30, 300)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect2)
#Warming in red, cooling in blue
left, bottom, width, height = (770, 170, 30, 300)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect3)
#Warming in red, cooling in blue
left, bottom, width, height = (840, 170, 30, 300)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.3,
                        facecolor = 'red',
                        linewidth = 2)
plt.gca().add_patch(rect4)

ax1111u = plt.subplot(gs[4])
ax1111u.get_xaxis().set_visible(True)
ax1111u.set_xlim(570,878)
ax1111u.plot(CO2a,CO2up, color='red', marker = '', linewidth=0.5, label = "pCO2")
ax1111u.yaxis.set_ticks_position('right')
ax1111u.yaxis.set_label_position("right")
ax1111u.spines["top"].set_color("white")
ax1111u.spines["bottom"].set_color("black")
ax1111u.spines["left"].set_color("black")
ax1111u.spines["right"].set_color("black")
ax1111u.set_ylim(170,300)

ax1111L = plt.subplot(gs[4])
ax1111L.get_xaxis().set_visible(True)
ax1111L.set_xlim(570,878)
ax1111L.plot(CO2a,CO2lo, color='red', marker = '', linewidth=0.5, label = "pCO2")
ax1111L.yaxis.set_ticks_position('right')
ax1111L.yaxis.set_label_position("right")
ax1111L.spines["top"].set_color("white")
ax1111L.spines["bottom"].set_color("black")
ax1111L.spines["left"].set_color("black")
ax1111L.spines["right"].set_color("black")
ax1111L.set_ylim(170,300)





fig.subplots_adjust(wspace=0, hspace=0)













