import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
#from gpiozero import LightSensor, Buzzer




plt.style.use('fivethirtyeight')
#ldr = LightSensor(4)
x_vals = []
y_vals = []
index = count()
# Initialize
x_axis_start = 0
x_axis_end = 10

def animate(i):
    data = pd.read_csv('data.csv')
    #print(ldr.value)
    x = data['x_value']
    y1 = data['total_1']
    print(len(x))
    plt.cla()
    plt.axis([len(x)-50, len(x)+50, 0, 1])
    plt.plot(x, y1)

        #plt.axis([x_axis_start, x_axis_end, 0, 1])
    

ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()


