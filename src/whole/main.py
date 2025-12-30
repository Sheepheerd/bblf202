from machine import Pin, PWM
from utime import sleep

left_a1 = Pin(18, Pin.OUT)
left_a2 = Pin(17, Pin.OUT)
pwma    = PWM(Pin(16))
pwma.freq(1000)

# Right Motor - Channel B
right_b1 = Pin(21, Pin.OUT)
right_b2 = Pin(20, Pin.OUT)
pwmb     = PWM(Pin(19))
pwmb.freq(1000)

# === IR Sensors ===
left_ir  = Pin(8, Pin.IN) 
right_ir = Pin(7, Pin.IN) 

# Onboard LED
led = Pin(25, Pin.OUT)

# Speeds
BASE_SPEED = 19    
TURN_SPEED = 10   
CORRECTION_SPEED = 10

def duty_percent_to_u16(duty):
    return int((duty * 65535) / 100)

def set_motors(left_duty, right_duty):
    left_a1.value(1)
    left_a2.value(0)
    pwma.duty_u16(duty_percent_to_u16(left_duty))

    right_b1.value(1)
    right_b2.value(0)
    pwmb.duty_u16(duty_percent_to_u16(right_duty))

def stop_motors():
    pwma.duty_u16(0)
    pwmb.duty_u16(0)

print("Line follower started! Place on line and power on.")

while True:
    left_val  = left_ir.value()  
    right_val = right_ir.value()

    led.value(left_val or right_val)
    print("left_val:", left_val, " right_val:", right_val)

    if left_val == 0 and right_val == 0:
        set_motors(BASE_SPEED, BASE_SPEED)

    elif left_val == 0 and right_val == 1:
        set_motors(BASE_SPEED, BASE_SPEED - CORRECTION_SPEED)

    elif left_val == 1 and right_val == 0:
        set_motors(BASE_SPEED - CORRECTION_SPEED, BASE_SPEED)

    else:
        stop_motors()

    sleep(0.01) 


