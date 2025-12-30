from machine import Pin, ADC
from time import sleep_ms

measure_repeat = 5
measure_wait = 50
threshold = 12000

led_onboard = Pin(25, Pin.OUT, value=0)

sensor_a = ADC(26)

def measureColor():
    value_sum = 0
    for _ in range(measure_repeat):
        value_sum += sensor_a.read_u16()
        sleep_ms(measure_wait)
    avg_value = int(value_sum / measure_repeat)
    return avg_value

print('Start continuous measurement')
while True:
    avg = measureColor()
    if avg < threshold:
        print('White detected:', avg)
        led_onboard.on()
    else:
        print('Nothing detected:', avg)
        led_onboard.off()
    sleep_ms(100)

