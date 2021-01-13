# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:42:11 2018

@author: Lorenz Bock
"""

import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import localtime, strftime
import numpy as np

url = "http://134.2.195.227:9000/innentemp"


xar = []
yar = []
tar = []
xtick = 0
stuff = 1

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

r = requests.get(url)
temp = float(r.text)
yar.append(temp)

def animate(i):
   
   r = requests.get(url)
   temp = float(r.text)
   yar.append(temp)
   now = strftime("%H:%M", localtime())
   tar.append(now)
   ax1.clear()
   ax1.plot(yar)
   ax1.set_ylim((min(yar)-0.1), (max(yar)+0.1))
   plt.xticks(np.arange(len(yar)), tar)
   #print(yar, xtick, temp)
   if len(yar) > 12:
       del yar[0]
        
ani = animation.FuncAnimation(fig, animate, interval=300000)
plt.show()
