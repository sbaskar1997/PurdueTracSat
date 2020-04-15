try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from serial import Serial
import time 


class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                
                return r
            else:
                self.buf.extend(data)
                

                
class Timer:
    def __init__(self, parent):
        
        # variable storing time
        self.seconds = 0
        # label displaying time
        self.label = tk.Label(parent, text="LOS", font="Arial 30", width=10)
        self.label.pack()
        # start the timer
        self.label.after(90, self.refresh_label)

    def refresh_label(self):
        """ refresh the content of the label every second """
        # increment the time
        global rl
        if ser.inWaiting()>0:
            try:
                data = (rl.readline().decode())
            except:
                data = "LOS"
            print(data)
        else:
            data = "LOS"
        self.label.configure(text=data)
        # request tkinter to call self.refresh after 1s (the delay is given in ms)
        self.label.after(90, self.refresh_label)

if __name__ == "__main__":
    root = tk.Tk()
    ser = Serial('COM4', 9600)
    rl = ReadLine(ser)
    timer = Timer(root)
    root.mainloop()