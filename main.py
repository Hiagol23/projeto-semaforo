from machine import Pin
from utime import sleep

led_verde = Pin(14, Pin.OUT)
led_amarelo = Pin(12, Pin.OUT)
led_vermelho = Pin(13, Pin.OUT)

while True:
    
    led_verde.on()
    led_amarelo.off()
    led_vermelho.off()
    sleep(20)
    sleep(0.5)

    led_verde.off()
    led_amarelo.on()
    led_vermelho.off()
    sleep(10)
    sleep(0.5)

    led_verde.off()
    led_amarelo.off()
    led_vermelho.on()
    sleep(7)
    sleep(0.5)
