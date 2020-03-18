import tkinter as tk
from lasercom import lasercom
import time
import os 
import sys

coms = lasercom()
uplinkPort = 'COM3'
coms.resetArduino(uplinkPort)
#coms.sendData('COM3', "tracsat")

root = tk.Tk()
root.title("TracSat Ground Station")
root.geometry("900x150")
#root.resizable(width=False, height=False)
root.minsize(width=900, height=150)

pauseCommand = "pause"

command = tk.Label(root, text="Command:")
currentlyTransmitting = tk.Label(root, text="Sending:")
commandEntry = tk.Entry(root)
currentTransmission = tk.Label(root, text="No Transmission", fg="red")

def transmitFunction():
    command = commandEntry.get()
    if command is not "":
        print("Inputted Command:" + command)
        coms.sendData(uplinkPort, command)
        currentTransmission.config(fg="green")
        currentTransmission.config(text= command)

def resetFunction():
    coms.resetArduino(uplinkPort)
    currentTransmission.config(fg="red")
    currentTransmission.config(text= "No Transmission")
    commandEntry.delete(0, 'end')

def pauseFunction():
    if pause["text"] == "Pause":
        global pauseCommand
        pauseCommand = commandEntry.get()
        coms.resetArduino(uplinkPort)
        pause.config(text='Unpause')
        print("Paused")
        currentTransmission.config(fg="red")
        currentTransmission.config(text= "No Transmission")
    else:
        print('Unpaused')
        coms.sendData(uplinkPort, pauseCommand)
        currentTransmission.config(fg="green")
        currentTransmission.config(text= pauseCommand)
        pause.config(text='Pause')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def abort():
    coms.sendData(uplinkPort, "abort")
    currentTransmission.config(fg="red")
    currentTransmission.config(text= "Abort Code")


transmit = tk.Button(root, text ="Transmit", width = 26, command=transmitFunction)
stop = tk.Button(root, text ="Stop")
reset = tk.Button(root, text ="Reset", command=resetFunction)
abort = tk.Button(root, text ="Abort", command=abort)
pause = tk.Button(root, text ="Pause", width = 15, command=pauseFunction)
resetMissionClock = tk.Button(root, text ="Reset Mission Clock")
extrabutton1 = tk.Button(root, text ="Self Destruct")
extrambutton2 = tk.Button(root, text ="Restart GUI", command=restart_program)
groundstationSoftware = tk.Label(root, text="Tracsat Ground Station Software \n Version 1.0.0 \n Copyright 2020. All Rights Reserved. \n Tracsat is a subsidiary of GA Electromagnetic Systems.")

 
command.grid(row=0,column =0, pady=5)
currentlyTransmitting.grid(row=2,column =0, sticky="W")
currentTransmission.grid(row=2,column =1, pady=5, sticky="W")
commandEntry.grid(row=0,column =1, pady=5, padx=15)
transmit.grid(row=1,columnspan = 2, pady=5)
#stop.grid(row=1,column = 1,  pady=5)
reset.grid(row=0,column = 2, pady=5, padx=5)
abort.grid(row=1,column = 2, pady=5, padx=5)
pause.grid(row=0,column = 3, pady=5, padx=5)
resetMissionClock.grid(row=1,column = 3, pady=5, padx=5)
extrabutton1.grid(row=0,column = 4, pady=5, padx=5)
extrambutton2.grid(row=1,column = 4, pady=5, padx=5)
groundstationSoftware.grid(row = 0, rowspan=2,column = 5, sticky="NE", pady=5,)
root.grid_columnconfigure(5, weight=1)

tk.mainloop()

