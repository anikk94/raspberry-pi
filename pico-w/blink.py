import machine
import utime
# Pin number is weird for pico-w
led_onboard = machine.Pin("LED", machine.Pin.OUT)

while True:
    led_onboard.value(1)
    utime.sleep(1)
    led_onboard.value(0)
    utime.sleep(1)
