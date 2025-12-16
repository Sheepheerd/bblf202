# Load libraries
from machine import Pin, ADC
from time import sleep_ms

# Parameters
measure_repeat = 5
measure_wait = 50  # ms between readings
threshold = 12000  # adjust based on your surface test

# Initialization: Onboard LED
led_onboard = Pin(25, Pin.OUT, value=0)

# Initialization of the ADC0 (GPIO26) for TCRT5000
sensor_a = ADC(26)

# Function: Measure sensor and return average
def measureColor():
    value_sum = 0
    for _ in range(measure_repeat):
        value_sum += sensor_a.read_u16()
        sleep_ms(measure_wait)
    avg_value = int(value_sum / measure_repeat)
    return avg_value

# Endless loop for live detection
print('Start continuous measurement')
while True:
    avg = measureColor()
    if avg < threshold:
        print('White detected:', avg)
        led_onboard.on()
    else:
        print('Nothing detected:', avg)
        led_onboard.off()
    sleep_ms(100)  # short pause to avoid flooding the terminal

