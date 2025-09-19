from machine import Pin
import time

led = Pin(25, Pin.OUT)  # Use "LED" for Pico W
for i in range(5):
    print(i)
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
