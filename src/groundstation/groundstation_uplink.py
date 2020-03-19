import tkinter as tk
from lasercom import lasercom
import time
import os 
import sys
from serial import Serial
from datetime import datetime
import pytz

coms = lasercom()
uplinkPort = 'COM3'
downlinkPort = 'COM4'
coms.resetArduino(uplinkPort)
#coms.sendData('COM3', "tracsat")
ser = Serial(downlinkPort, 9600)
root = tk.Tk()
root.title("TracSat Ground Station")
root.geometry("900x450")
#root.resizable(width=False, height=False)
root.minsize(width=900, height=450)

pauseCommand = "empty"
seconds_MC = 0
minutes_MC = 0
hours_MC = 0
stopMissionClock = 1

uplinkLabel = tk.Label(root, text='UPLINK', font='Helvetica 11 bold')
command = tk.Label(root, text="Command:")
currentlyTransmitting = tk.Label(root, text="Sending:")
commandEntry = tk.Entry(root)
currentTransmission = tk.Label(root, text="No Transmission", fg="red")
missionClock = tk.Label(root,text="Mission Clock:\t00:00:00", font='Helvetica 11')
missionClock.grid(row=3,column=5,pady=5, padx=10)

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

def resetMissionClock():
    global seconds_MC
    global minutes_MC
    global hours_MC
    global stopMissionClock
    seconds_MC = 0
    minutes_MC = 0
    hours_MC = 0
    stopMissionClock = 0  

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

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def abort():
    global stopMissionClock
    coms.sendData(uplinkPort, "abort")
    currentTransmission.config(fg="red")
    currentTransmission.config(text= "Abort Code")
    stopMissionClock = 1

refresh_missionClock()


transmit = tk.Button(root, text ="Transmit", width = 26, command=transmitFunction)
stop = tk.Button(root, text ="Stop")
reset = tk.Button(root, text ="Reset", command=resetFunction)
abort = tk.Button(root, text ="Abort", command=abort)
pause = tk.Button(root, text ="Pause", width = 15, command=pauseFunction)
resetMissionClock = tk.Button(root, text ="Reset Mission Clock", command=resetMissionClock)
extrabutton1 = tk.Button(root, text ="Self Destruct")
extrambutton2 = tk.Button(root, text ="Restart GUI", command=restart_program)
groundstationSoftware = tk.Label(root, text="Tracsat Ground Station Software \n Version 1.0.0 \n Copyright 2020. All Rights Reserved. \n Tracsat is a subsidiary of GA Electromagnetic Systems.")

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





downlinkLabel = tk.Label(root, text='DOWNLINK', font='Helvetica 11 bold')
currentReceivingLabel = tk.Label(root,text="Receiving:")
currentReceiving = tk.Label(root,text="LOS", fg="red")
currentTime = tk.Label(root,font='Helvetica 11')
GATime = tk.Label(root,font='Helvetica 11')
moscowTime = tk.Label(root,font='Helvetica 11')


downlinkLabel.grid(row=4,column=0, columnspan=2, pady=5, sticky="W")
currentReceivingLabel.grid(row=5,column=0,pady=5,sticky="w")


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
GATime.grid(row=6,column=5,columnspan=2,pady=5)
moscowTime.grid(row=7,column=5,columnspan=2,pady=5)


refresh_currentTime()
refresh_serialInput()
refresh_GATime()
refresh_moscowTime()

#currentReceiving.after(90, refresh_serialInput)



tk.mainloop()

