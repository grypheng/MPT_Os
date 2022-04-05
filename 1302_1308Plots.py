#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:42:52 2022

@author: gryphengoss
"""

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


#Create subplot

ax1 = plt.subplot(311)
ax1.plot(d18Oage,d18Oval, color='black', marker = '.', label = "d18O")
plt.ylabel('d18O (LR04)')
plt.title('IODP Sites 1302 and 1308 - Osmium Signature')
ax1.get_xaxis().set_visible(False)
ax1.set_ylim(6, 3) 
#ax1.set_ylim(525,1001) 
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
plt.annotate('d18O', 
             xy=(988, 5.7), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)
ax1.text(619,3.6,'MIS 15')
ax1.text(630,5.4,'MIS 16')
ax1.text(700,3.6,'MIS 17')
ax1.text(720,4.9,'MIS 18')
ax1.text(784,3.4,'MIS 19')
ax1.text(800,5.0,'MIS 20')
ax1.text(862,3.3,'MIS 21')
ax1.text(882,4.8,'MIS 22')
ax1.text(959,3.3,'MIS 23')



left, bottom, width, height = (630, 6, 60, -3)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect1)
left, bottom, width, height = (719, 6, 56, -3)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect2)
left, bottom, width, height = (796, 6, 65, -3)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect3)
left, bottom, width, height = (877, 6, 75, -3)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.1,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)



ax2 = plt.subplot(312, sharex = ax1)
ax2.plot(ch1302a,ch1302os, color='black', marker = '.', label = "1302")     
ax2.plot(ar1302a,ar1302os, color='black', linestyle = 'dashed', marker = '.')
plt.ylabel('187Os / 188Os')
#ax2.legend()
ax2.set_ylim(0,2.5)
ax2.get_xaxis().set_visible(False)
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
plt.annotate('1302 (Proximal)', 
             xy=(988, 0.25), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)
left, bottom, width, height = (630, 0, 60, 2.5)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect1)
left, bottom, width, height = (719, 0, 56, 2.5)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect2)
left, bottom, width, height = (796, 0, 65, 2.5)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect3)
left, bottom, width, height = (877, 0, 75, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)



ax3 = plt.subplot(313, sharex = ax1)
ax3.plot(ch1308a,ch1308os, color='black', marker = '.', label = "1308")     
ax3.plot(ar1308a,ar1308os, color='black', linestyle = 'dashed', marker = '.')
plt.ylabel('187Os / 188Os')
#ax3.legend()
#ax3.get_xaxis().set_visible(False)
ax3.set_ylim(0,2.5)
plt.xlabel('Age (ka)')
bbox=dict(boxstyle="round", alpha=0.1, color='grey')
plt.annotate('1308 (Distal)', 
             xy=(988, 0.25), size=14, color = 'black',
             ha='center', va="center",bbox=bbox)
left, bottom, width, height = (630, 0, 60, 2.5)
rect1=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect1)
left, bottom, width, height = (719, 0, 56, 2.5)
rect2=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect2)
left, bottom, width, height = (796, 0, 65, 2.5)
rect3=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect3)
left, bottom, width, height = (877, 0, 75, 2.5)
rect4=mpatches.Rectangle((left,bottom),width,height, 
                        #fill = False,
                        #color = "purple",
                        alpha = 0.2,
                        facecolor = 'grey',
                        linewidth = 2)
plt.gca().add_patch(rect4)



#ax4 = plt.subplot(414, sharex = ax1)
#ax4.plot(data['Age2'].dropna(),data['OspptCh'].dropna(), color='black', marker = '.', label = '1302')  
#ax4.plot(data['Age2'].dropna(),data['OspptAR'].dropna(), color='black', linestyle = 'dashed', marker = '.')
#plt.ylabel('Os ppt')
#ax4.legend()
#plt.xlabel('Age (ka)')

plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
