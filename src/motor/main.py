from machine import Pin, PWM
from utime import sleep

# === Left Motor - Channel A ===
aina1 = Pin(18, Pin.OUT)   # AIN1
aina2 = Pin(17, Pin.OUT)   # AIN2
pwma  = PWM(Pin(16))       # PWMA
pwma.freq(1000)

# === Right Motor - Channel B ===
bin1 = Pin(21, Pin.OUT)    # BIN1
bin2 = Pin(20, Pin.OUT)    # BIN2
pwmb = PWM(Pin(19))        # PWMB
pwmb.freq(1000)

led = Pin(25, Pin.OUT)

button = Pin(9, Pin.IN, Pin.PULL_UP) 

DUTY_CYCLE = 25

def duty_percent_to_u16(duty):
    return int((duty * 65535) / 100)

# === Control Functions ===
def left_forward(duty):
    aina1.value(1)
    aina2.value(0)
    pwma.duty_u16(duty_percent_to_u16(duty))

def left_backward(duty):
    aina1.value(0)
    aina2.value(1)
    pwma.duty_u16(duty_percent_to_u16(duty))

def right_forward(duty):
    bin1.value(1)
    bin2.value(0)
    pwmb.duty_u16(duty_percent_to_u16(duty))

def right_backward(duty):
    bin1.value(0)
    bin2.value(1)
    pwmb.duty_u16(duty_percent_to_u16(duty))

def both_forward(duty):
    left_forward(duty)
    right_forward(duty)

def both_backward(duty):
    left_backward(duty)
    right_backward(duty)

def stop_both():
    aina1.value(0)
    aina2.value(0)
    pwma.duty_u16(0)
    bin1.value(0)
    bin2.value(0)
    pwmb.duty_u16(0)

# === Startup Message ===
print("Dual motor robot ready. Press the button to start a forward-backward cycle.")

# === Main Loop ===
while True:
    if button.value() == 0:
        led.toggle()
        print(f"Button pressed! Running cycle at {DUTY_CYCLE}% duty...")

        both_forward(DUTY_CYCLE)
        sleep(5)

        both_backward(DUTY_CYCLE)
        sleep(5)

        stop_both()
        print("Cycle complete. Press button again for next cycle.")
        led.toggle()

        sleep(0.2)
        while button.value() == 0:
            sleep(0.01)
        sleep(0.2)

    sleep(0.05)
