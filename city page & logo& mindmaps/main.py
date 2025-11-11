from machine import Pin
from time import sleep


pins= [2, 4, 16, 17, 5, 18, 13, 14]

leds= [Pin(x, Pin.OUT) for x in pins]
entrance = Pin(34, Pin.IN)
exit = Pin(35, Pin.IN)

cars= 0
last_en= 0
last_ex= 0

while True:
    s1 = entrance.value()
    s2 = exit.value()
    if last_en ==0 and s1 == 1:
        if  cars < 8 :
            leds[cars].on()
            cars += 1
        sleep(0.3)
    if last_ex == 0 and s2 == 1:
        if cars > 0:
            cars -= 1
            leds[cars].off()
        sleep(0.3)
    last_en = s1
    last_ex = s2
    sleep(0.05)