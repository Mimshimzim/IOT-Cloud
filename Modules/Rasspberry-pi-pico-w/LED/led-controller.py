from machine import Pin
import time


LED_PIN_NUMBER = 15

led = Pin(LED_PIN_NUMBER, Pin.OUT)

def turn_on():
    led.value(1)

def turn_off():
    led.value(0)

