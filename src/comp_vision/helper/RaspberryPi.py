from __future__ import division
import os
import time
import psutil
from subprocess import PIPE, Popen
import psutil

class RaspberryPi:
    def __init__(self):
        pass

    @property
    def temp(self):
        self._temp = os.popen('vcgencmd measure_temp').readline()
        return self._temp

    @property
    def ram(self):
        self._ram = Ram()
        return self._ram

    @property
    def disk(self):
        self._disk = Disk()
        return self._disk

class Ram:
    def __init__(self):
        self.ram_struct = psutil.phymem_usage()

    @property
    def ram_total(self):
        self._ram_total = self.ram_struct.total / 2**20
        return self._ram_total

    @property
    def ram_used(self):
        self._ram_used = self.ram_struct.used / 2**20
        return self._ram_used

    @property
    def ram_free(self):
        self._ram_free = self.ram_struct.free / 2**20
        return self._ram_free

class Disk:
    def __init__(self):
        self._disk = psutil.disk_usage('/')

    @property
    def disk_total(self):
        self._disk_total = self._disk.total / 2**30
        return self._disk_total

    @property
    def disk_used(self):
        self._disk_used = self._disk.used / 2**30
        return self._disk_used

    @property
    def disk_free(self):
        self._disk_free = self._disk.free / 2**30
        return self._ram_free

pi = RaspberryPi()
print(pi.ram)
