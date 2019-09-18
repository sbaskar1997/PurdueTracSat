import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
from gpiozero import LightSensor, Buzzer



plt.style.use('fivethirtyeight')
x_vals = []
y_vals = []
index = count()


# Initialize
x_axis_start = 0
x_axis_end = 10

#Animate plot
def animate(i):
	data = pd.read_csv('data.csv') #read data
	#print(ldr.value)
	x = data['x_value']
	y1 = data['total_1']
	plt.cla()
	plt.axis([len(x)-50, len(x)+50, 0, 1]) #update axis
	plt.plot(x, y1)    

ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.show()


