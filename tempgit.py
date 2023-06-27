from machine import Pin
from time import sleep
import dht


dhttt=Pin(27,Pin.IN)
dht_sensor=dht.DHT11(dhttt)

led=Pin(12,Pin.OUT)

while True:
    dht_sensor.measure()
    tempr=dht_sensor.temperature()
    print(tempr)
    if(tempr>25):
        led.value(1)
        sleep(1)
    else:
        led.value(0)
        sleep(1)
        