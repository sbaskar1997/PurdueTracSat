from gpiozero import LightSensor, Buzzer
from time import sleep


ldr = LightSensor(4)
buzzer = Buzzer(17)

while True:
    sleep(.1)
    if ldr.value < .5:
        buzzer.on()
    else:
        buzzer.off()
