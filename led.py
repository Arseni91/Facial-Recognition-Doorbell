from gpiozero import LED
from time import sleep

led = LED(21)
led1 = LED(20)
led.on()
sleep(5)
led.off()
led1.on()
sleep(5)
led1.off()