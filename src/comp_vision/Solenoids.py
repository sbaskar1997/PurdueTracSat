#!/usr/bin/env python
# Python set of classes that open and close individual solenoids
# Import native modules
import time

class sol1:
    def __init__(self, pi):
        self._pi = pi

    def open(self):
        self._pi.write(18,1)
	time.sleep(.1)
	self._pi.write(18,0)

    def close(self):
        self._pi.write(23,1)
	time.sleep(.1)
	self._pi.write(23,0)

class sol2:
    def __init__(self, pi):
        self._pi = pi

    def open(self):
        self._pi.write(24,1)
	time.sleep(.3)
	self._pi.write(24,0)

    def close(self):
        self._pi.write(25,1)
	time.sleep(.3)
	self._pi.write(25,0)


class sol3:
    def __init__(self, pi):
        self._pi = pi

    def open(self):
        self._pi.write(12,1)
	time.sleep(.2)
	self._pi.write(12,0)

    def close(self):
        self._pi.write(16,1)
	time.sleep(.2)
	self._pi.write(16,0)

class sol4:
    def __init__(self, pi):
        self._pi = pi

    def open(self):
        self._pi.write(20,1)
	time.sleep(.02)
	self._pi.write(20,0)

    def close(self):
        self._pi.write(21,1)
	time.sleep(.02)
	self._pi.write(21,0)

