import tkinter as tk
from tkinter import *
from tkinter import messagebox
from winsound import *
import tkinter.font as font


root = tk.Tk()
root.title("TracSat Ground Station")
root.geometry("900x350")
#root.resizable(width=False, height=False)
root.minsize(width=900, height=150)

command = tk.Label(root, text="Command:")
currentlyTransmitting = tk.Label(root, text="Sending:")
currentTransmission = tk.Label(root, text="No Transmission", fg="red")
commandEntry = tk.Entry(root)
transmit = tk.Button(root, text ="Transmit", width = 26)
stop = tk.Button(root, text ="Stop")
reset = tk.Button(root, text ="Reset")
abort = tk.Button(root, text ="Abort")
pause = tk.Button(root, text ="Pause", width = 15)
resetMissionClock = tk.Button(root, text ="Reset Mission Clock")

def selfdestruct():
    messagebox.showinfo('Message title', 'you are fucked')
def play():
    return PlaySound("videoplayback.wav",SND_FILENAME)
def screwyou():
    play()

extrabutton1 = tk.Button(root, text ="Self Destruct",command=screwyou)
extrabutton2 = tk.Button(root, text ="extrabutton2")
groundstationSoftware = tk.Label(root, text="Tracsat Ground Station Guidance Computer \n Version 1.0.0 \n Copyright © 2020. All Rights Reserved. \n Tracsat is a subsidiary of GA Electromagnetic Systems.")

myFont = font.Font(size=30)
lbl = Label(root, text="",fg ="red")
lbl['font']=myFont
lbl.grid(column=1, row=3)
lbl2 = Label(root, text="",fg="red")
lbl3 = Label(root, text="")
lbl4 = Label(root, text="")
lbl2.grid(column=2, row=6)
lbl3.grid(column=0, row=7)
lbl4.grid(column=1, row=7)

#def clicked4():
    #lbl.configure(text="Button was clicked !!")
#btn = Button(root, text="Click Me", command=clicked4)

commandNoun = tk.Entry(root)
commandVerb = tk.Entry(root)
commandNoun.grid(row=4,column =0)
commandVerb.grid(row=5,column =0)

#btn.grid(column=5, row=4)
def verbClick():
    res_verb = commandVerb.get()
    return res_verb

def nounClick():
    res_noun = commandNoun.get()
    return res_noun

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def submit():
    res_verb = verbClick()
    res_noun = nounClick()
    commandNoun.delete(0,'end')
    commandVerb.delete(0,'end')

    if res_verb == '50':
        if res_noun == '20':
            lbl.configure(text = "MASTER ALARM")
            #lbl2.configure(text = "BANK ANGLE")
            #lbl3.configure(text = "PULL UP")
            PlaySound("alarm.wav",SND_FILENAME)
        



noun = Button(root, text="Noun",command=nounClick)
verb = Button(root, text="Verb",command=verbClick)
noun.grid(row=4,column =1,pady=5,padx=5)
verb.grid(row=5,column =1,pady=5,padx=5)
submit = Button(root, text="Submit",command=submit)
submit.grid(row=6,column =0,pady=5,padx=5)


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
extrabutton2.grid(row=1,column = 4, pady=5, padx=5)
groundstationSoftware.grid(row = 0, rowspan=2,column = 5, sticky="NE", pady=5,)
root.grid_columnconfigure(5, weight=1)


tk.mainloop()