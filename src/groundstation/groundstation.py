import tkinter as tk
from lasercom import lasercom
import time
import os 
import sys
from serial import Serial
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import pandas as pd
import random

###To run this program: python groundstation.py <laserport> <receiverport>###



# Check for serial port names
if len(sys.argv) < 3:
    print("Error: Groundstation software requires both uplink and downlink ports as CLI arguments \nEx. python groundstation COM3 COM4")
    sys.exit()

#General setup
coms = lasercom()
uplinkPort = sys.argv[1] #Name of the serial port for the laser arduino
downlinkPort = sys.argv[2] #Name of the serial port for the reciever arduino
coms.resetArduino(uplinkPort) #reset laser arduino at the start
ser = Serial(downlinkPort, 9600)
root = tk.Tk()
root.title("TracSat Ground Station")
root.geometry("900x450")
#root.resizable(width=False, height=False)
root.minsize(width=900, height=530)
pauseCommand = "empty"
seconds_MC = 0
minutes_MC = 0
hours_MC = 0
stopMissionClock = 1
plot = tk.PhotoImage(file = r"icon_small.png")



#################
######UPLINK#####
#################

uplinkLabel = tk.Label(root, text='UPLINK', font='Helvetica 11 bold')
command = tk.Label(root, text="Command:")
currentlyTransmitting = tk.Label(root, text="Sending:")
commandEntry = tk.Entry(root)
currentTransmission = tk.Label(root, text="No Transmission", fg="red")
missionClock = tk.Label(root,text="Mission Clock:\t00:00:00", font='Helvetica 11')
missionClock.grid(row=3,column=5,pady=5, padx=10)

#Mission Clock 
def refresh_missionClock():
    global seconds_MC
    global minutes_MC
    global hours_MC
    global stopMissionClock
    if not stopMissionClock:
        if seconds_MC < 59:
            seconds_MC = seconds_MC + 1
        else:
            seconds_MC = 0
            if minutes_MC < 59:
                minutes_MC = minutes_MC + 1
            else:
                hours_MC = hours_MC + 1

    missionClock.config(text='Mission Clock:\t%02d:%02d:%02d' % (hours_MC, minutes_MC,seconds_MC))
    missionClock.after(1000, refresh_missionClock)

#Transmit button
def transmitFunction():
    command = commandEntry.get()
    global stopMissionClock
    if command is not "":
        global stopMissionClock
        stopMissionClock = 0
        print("Inputted Command:" + command)
        coms.sendData(uplinkPort, command)
        currentTransmission.config(fg="green")
        currentTransmission.config(text= command)
        stopMissionClock = 0

#Reset mission clock function
def resetMissionClock():
    global seconds_MC
    global minutes_MC
    global hours_MC
    global stopMissionClock
    seconds_MC = 0
    minutes_MC = 0
    hours_MC = 0
    stopMissionClock = 0  

# Reset button
def resetFunction():
    global seconds_MC
    global minutes_MC
    global hours_MC
    global stopMissionClock
    coms.resetArduino(uplinkPort)
    currentTransmission.config(fg="red")
    currentTransmission.config(text= "No Transmission")
    commandEntry.delete(0, 'end')
    stopMissionClock = 1
    seconds_MC = 0
    minutes_MC = 0
    hours_MC = 0

#Pause button
def pauseFunction():
    global stopMissionClock
    if pause["text"] == "Pause":
        global pauseCommand
        pauseCommand = commandEntry.get()
        coms.resetArduino(uplinkPort)
        pause.config(text='Unpause')
        print("Paused")
        currentTransmission.config(fg="red")
        currentTransmission.config(text= "No Transmission")
        stopMissionClock = 1

    else:
        print('Unpaused')
        coms.sendData(uplinkPort, pauseCommand)
        currentTransmission.config(fg="green")
        currentTransmission.config(text= pauseCommand)
        pause.config(text='Pause')
        stopMissionClock = 0

#Restart button
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Abrort button (Sends "Abort")
def abort():
    global stopMissionClock
    coms.sendData(uplinkPort, "abort")
    currentTransmission.config(fg="red")
    currentTransmission.config(text= "Abort Code")
    stopMissionClock = 1

def settings():
    window = tk.Toplevel(root)

    ## ADD SETTINGS HERE


refresh_missionClock()


transmit = tk.Button(root, text ="Transmit", width = 26, command=transmitFunction)
stop = tk.Button(root, text ="Stop")
reset = tk.Button(root, text ="Reset", command=resetFunction)
abort = tk.Button(root, text ="Abort", command=abort)
pause = tk.Button(root, text ="Pause", width = 15, command=pauseFunction)
resetMissionClock = tk.Button(root, text ="Reset Mission Clock", command=resetMissionClock)
extrabutton1 = tk.Button(root, text ="  Settings  ", command=settings)
extrambutton2 = tk.Button(root, text ="Restart GUI", command=restart_program)
groundstationSoftware = tk.Label(root, text="Tracsat Ground Station Software \n Version 1.0.0") #\n Copyright 2020. All Rights Reserved. \n Tracsat is a subsidiary of GA Electromagnetic Systems.")

uplinkLabel.grid(row=0,column=0, sticky="W")
command.grid(row=1,column =0, pady=5)
currentlyTransmitting.grid(row=3,column =0, pady=5, sticky="W")
currentTransmission.grid(row=3,column =1, pady=5, sticky="W")
commandEntry.grid(row=1,column =1, pady=5, padx=15)
transmit.grid(row=2,columnspan = 2, pady=5)
#stop.grid(row=1,column = 1,  pady=5)
reset.grid(row=1,column = 2, pady=5, padx=5)
abort.grid(row=2,column = 2, pady=5, padx=5)
pause.grid(row=1,column = 3, pady=5, padx=5)
resetMissionClock.grid(row=2,column = 3, pady=5, padx=5)
extrabutton1.grid(row=1,column = 4, pady=5, padx=5)
extrambutton2.grid(row=2,column = 4, pady=5, padx=5)
groundstationSoftware.grid(row = 0, rowspan=2,column = 5, sticky="NE", pady=5,)


root.grid_columnconfigure(5, weight=1)




#################
#####DOWNLINK####
#################

def accel_x_plot_func():
    x_vals = []
    y_vals = []
    index = count()
    # Initialize
    x_axis_start = 0
    x_axis_end = 10
    #Animate plot
    def animate(i):
        data = pd.read_csv('data.csv') #read data
        x = data['x_value']
        y1 = data['total_1']
        plt.cla()
        plt.axis([len(x)-50, len(x)+50, 0, 1]) #update axis
        plt.plot(x, y1)    
        plt.xticks([])
        plt.title("Acceleration in X Direction")
        plt.ylabel("Acceleration")
    ani = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.show()

def accel_y_plot_func():
    plt.close(1) 
    x_vals = []
    y_vals = []
    index = count()
    # Initialize
    x_axis_start = 0
    x_axis_end = 10
    #Animate plot
    def animate(i):
        data = pd.read_csv('data.csv') #read data
        x = data['x_value']
        y1 = data['total_1']
        plt.cla()
        plt.axis([len(x)-50, len(x)+50, 0, 1]) #update axis
        plt.plot(x, y1)    
        plt.xticks([])
        plt.title("Acceleration in Y Direction")
        plt.ylabel("Acceleration")
    ani = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.show()

def vel_x_plot_func():
    plt.close(1) 
    x_vals = []
    y_vals = []
    index = count()
    # Initialize
    x_axis_start = 0
    x_axis_end = 10
    #Animate plot
    def animate(i):
        data = pd.read_csv('data.csv') #read data
        x = data['x_value']
        y1 = data['total_1']
        plt.cla()
        plt.axis([len(x)-50, len(x)+50, 0, 1]) #update axis
        plt.plot(x, y1)    
        plt.xticks([])
        plt.title("Velocity in X Direction")
        plt.ylabel("Velocity")
    ani = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.show()

def vel_y_plot_func():
    plt.close(1) 
    x_vals = []
    y_vals = []
    index = count()
    # Initialize
    x_axis_start = 0
    x_axis_end = 10
    #Animate plot
    def animate(i):
        data = pd.read_csv('data.csv') #read data
        x = data['x_value']
        y1 = data['total_1']
        plt.cla()
        plt.axis([len(x)-50, len(x)+50, 0, 1]) #update axis
        plt.plot(x, y1)    
        plt.xticks([])
        plt.title("Velocity in Y Direction")
        plt.ylabel("Velocity")
    ani = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.show()

def direction_plot_func():
    plt.close(1) 
    x_vals = []
    y_vals = []
    index = count()
    # Initialize
    x_axis_start = 0
    x_axis_end = 10
    #Animate plot
    def animate(i):
        data = pd.read_csv('data.csv') #read data
        x = data['x_value']
        y1 = data['total_1']
        plt.cla()
        plt.axis([len(x)-50, len(x)+50, 0, 1]) #update axis
        plt.plot(x, y1)    
        plt.xticks([])
        plt.title("Direction")
        plt.ylabel("Angle")
    ani = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.show()
    
def all_plot_func():
    plt.close(1) 
    # Create a figure with two subplots
    fig = plt.figure()
    ax1 = fig.add_subplot(5,1,1)
    ax2 = fig.add_subplot(5,1,2)
    ax3 = fig.add_subplot(5,1,3)
    ax4 = fig.add_subplot(5,1,4)
    ax5 = fig.add_subplot(5,1,5)
    # Adjust spacing between plots
    plt.subplots_adjust(top = 0.93, bottom = 0.07, hspace = 0.6)
    #define the function for use in matplotlib.animation.funcAnimation
    def animate(i):
        data = pd.read_csv('data.csv') #read data
        x = data['x_value']
        y1 = data['total_1']
        # Set subplot data
        xlim = len(y1)
        ax1.clear()
        ax1.plot(y1)
        ax1.set_xlim(xlim - 30, xlim)
        ax1.set_xticks([])
        ax2.clear()
        ax2.plot(y1)
        ax2.set_xlim(xlim - 30, xlim)
        ax2.set_xticks([])
        ax3.clear()
        ax3.plot(y1)
        ax3.set_xlim(xlim - 30, xlim)
        ax3.set_xticks([])
        ax4.clear()
        ax4.plot(y1)
        ax4.set_xlim(xlim - 30, xlim)
        ax4.set_xticks([])
        ax5.clear()
        ax5.plot(y1)
        ax5.set_xlim(xlim - 30, xlim)
        ax5.set_xticks([])
        # Set subplot titles
        ax1.set_title("X Acceleration")
        ax2.set_title("Y Acceleration")
        ax3.set_title("X Velocity")
        ax4.set_title("Y Velocty")
        ax5.set_title("Direction")
    ani = FuncAnimation(fig, animate, interval=100)
    plt.show()

downlinkLabel = tk.Label(root, text='DOWNLINK', font='Helvetica 11 bold')
currentReceivingLabel = tk.Label(root,text="Receiving:")
currentReceiving = tk.Label(root,text="LOS", fg="red")
currentTime = tk.Label(root,font='Helvetica 11')
GATime = tk.Label(root,font='Helvetica 11')
moscowTime = tk.Label(root,font='Helvetica 11')
accel_x_label = tk.Label(root,text="X Acceleration:")
accel_y_label  = tk.Label(root,text="Y Acceleration:")
direction_label  = tk.Label(root,text="Direction:")
vel_x_label  = tk.Label(root,text="X Velocity:")
vel_y_label  = tk.Label(root,text="Y Velocity:")
accel_x = tk.Label(root,text="0")
accel_y = tk.Label(root,text="0")
direction = tk.Label(root,text="0")
vel_x = tk.Label(root,text="0")
vel_y = tk.Label(root,text="0")
accel_x_plot = tk.Button(root, image = plot, width = 17, height = 17, command=accel_x_plot_func)
accel_y_plot = tk.Button(root, image = plot, command=accel_y_plot_func)
direction_plot = tk.Button(root, image = plot, command=direction_plot_func)
vel_x_plot = tk.Button(root, image = plot, command=vel_x_plot_func)
vel_y_plot = tk.Button(root, image = plot, command=vel_y_plot_func)
write = tk.Button(root, text="Write")
allPlots = tk.Button(root, text="All Plots", command=all_plot_func)


downlinkLabel.grid(row=4,column=0, columnspan=2, pady=5, sticky="W")
currentReceivingLabel.grid(row=5,column=0,pady=5,sticky="w")
accel_x_label.grid(row=6,column=0,pady=5,sticky="w")
accel_y_label.grid(row=7,column=0,pady=5,sticky="w")
vel_x_label.grid(row=8,column=0,pady=5,sticky="w")
vel_y_label.grid(row=9,column=0,pady=5,sticky="w")
direction_label.grid(row=10,column=0,pady=5,sticky="w")
accel_x_plot.grid(row=6,column=2,pady=5,sticky="w")
accel_y_plot.grid(row=7,column=2,pady=5,sticky="w")
vel_x_plot.grid(row=8,column=2,pady=5,sticky="w")
vel_y_plot.grid(row=9,column=2,pady=5,sticky="w")
direction_plot.grid(row=10,column=2,pady=5,sticky="w")
write.grid(row=11,column=0,pady=5,sticky="w")
allPlots.grid(row=11,column=2,pady=5)

def refresh_serialInput():
    global ser
    bytesToRead = ser.inWaiting()
    data = ser.readline(bytesToRead).strip()
    print(data)
    if not data:
        data = "LOS"
        color = "red"
    else:
        color = "green"
    currentReceiving.configure(text=data, fg=color)
    currentReceiving.after(90, refresh_serialInput)

def refresh_currentTime():
    now = datetime.now()
    timeString = now.strftime("%H:%M:%S")
    currentTime.config(text="Current Time:\t" + timeString)
    currentTime.after(1000,refresh_currentTime)

def refresh_GATime():
    timezone = pytz.timezone("America/New_York")
    GATimezone = datetime.now(timezone)
    timeString = GATimezone.strftime("%H:%M:%S")
    GATime.config(text="General Atomics HQ Time:\t" + timeString)
    GATime.after(1000,refresh_GATime)

def refresh_moscowTime():
    timezone = pytz.timezone("Europe/Moscow")
    moscowTimezone = datetime.now(timezone)
    timeString = moscowTimezone.strftime("%H:%M:%S")
    moscowTime.config(text="Moscow Time:\t" + timeString)
    moscowTime.after(1000,refresh_moscowTime)




currentReceiving.grid(row=5,column=1,pady=5,sticky="w")
currentTime.grid(row=5,column=5,columnspan=2,pady=5)
#GATime.grid(row=6,column=5,columnspan=2,pady=5)
#moscowTime.grid(row=7,column=5,columnspan=2,pady=5)

accel_x.grid(row=6,column=1,pady=5,sticky="w")
accel_y.grid(row=7,column=1,pady=5,sticky="w")
vel_x.grid(row=8,column=1,pady=5,sticky="w")
vel_y.grid(row=9,column=1,pady=5,sticky="w")
direction.grid(row=10,column=1,pady=5,sticky="w")


refresh_currentTime()
refresh_serialInput()
refresh_GATime()
refresh_moscowTime()

#currentReceiving.after(90, refresh_serialInput)




#################
######SYSTEM#####
#################

systemPref = tk.Label(root, text='SYSTEM PREFORMANCE', font='Helvetica 11 bold')
servoAngleLabel = tk.Label(root,text="Servo Angle:")
trackingStatusLabel = tk.Label(root,text="Signal Status:")
airBearingsStatusLabel = tk.Label(root,text="Air Bearings:")
solenoidsStatusLabel = tk.Label(root,text="Solenoids:")
raspberryPiStatusLabel = tk.Label(root,text="Raspberry Pi:")
servoAngle = tk.Label(root,text="8 degrees")
trackingStatus = tk.Label(root,text="Tracking")
airBearingsStatus = tk.Label(root,text="Nominal", fg='green')
solenoidsStatus = tk.Label(root,text="Nominal", fg='green')
raspberryPiStatus = tk.Label(root,text="Nominal", fg='green')

systemPref.grid(row=12,column=0, columnspan=2, pady=5, sticky="W")
servoAngleLabel.grid(row=13,column=0, columnspan=2, pady=5, sticky="W")
trackingStatusLabel.grid(row=14,column=0, columnspan=2, pady=5, sticky="W")
airBearingsStatusLabel.grid(row=13,column=3, columnspan=2, pady=5, sticky="W")
solenoidsStatusLabel.grid(row=14,column=3, columnspan=2, pady=5, sticky="W")
raspberryPiStatusLabel.grid(row=15,column=3, columnspan=2, pady=5, sticky="W")
servoAngle.grid(row=13,column=1, columnspan=2, pady=5, sticky="W")
trackingStatus.grid(row=14,column=1, columnspan=2, pady=5, sticky="W")
airBearingsStatus.grid(row=13,column=4, columnspan=2, pady=5, sticky="W")
solenoidsStatus.grid(row=14,column=4, columnspan=2, pady=5, sticky="W")
raspberryPiStatus.grid(row=15,column=4, columnspan=2, pady=5, sticky="W")

tk.mainloop()

