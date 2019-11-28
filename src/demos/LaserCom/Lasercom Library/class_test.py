from lasercom import lasercom

coms = lasercom()
#vector = coms.uplink('/dev/tty.usbmodem14301')
coms.resetArduino('/dev/tty.usbmodem14101')
coms.downlink('/dev/tty.usbmodem14101', "1,20,30,40,500")
