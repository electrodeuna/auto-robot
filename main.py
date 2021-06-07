from machine import Pin, UART
import time

command = ''
m11 = Pin(2, Pin.OUT)
m12 = Pin(3, Pin.OUT)
m21 = Pin(4, Pin.OUT)
m22 = Pin(5, Pin.OUT)

uart = UART(0, 9600)

while True:
    if uart.any():
        command = uart.readline()
        print(command)
    
    if "F" in command:
        m11.value(1)
        m21.value(1)
    elif "B" in command:
        m12.value(1)
        m22.value(1)
    elif "L" in command:
        m11.value(1)
    elif "R" in command:
        m21.value(1)
    else:
        m11.value(0)
        m12.value(0)
        m21.value(0)
        m22.value(0)