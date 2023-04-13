import board
import digitalio
import time
import adafruit_rotaryio
from math import copysign

# Pin definitions
MODE1_PIN = board.GP11
MODE2_PIN = board.GP12
MODE3_PIN = board.GP13
STEP_PIN = board.GP14
DIR_PIN = board.GP15
ENCODER_CLK_PIN = board.GP16
ENCODER_DT_PIN = board.GP17
ENCODER_SW_PIN = board.GP18

# Configure pins
mode1 = digitalio.DigitalInOut(MODE1_PIN)
mode1.direction = digitalio.Direction.OUTPUT

mode2 = digitalio.DigitalInOut(MODE2_PIN)
mode2.direction = digitalio.Direction.OUTPUT

mode3 = digitalio.DigitalInOut(MODE3_PIN)
mode3.direction = digitalio.Direction.OUTPUT

step = digitalio.DigitalInOut(STEP_PIN)
step.direction = digitalio.Direction.OUTPUT

dir = digitalio.DigitalInOut(DIR_PIN)
dir.direction = digitalio.Direction.OUTPUT

encoder = adafruit_rotaryio.IncrementalEncoder(ENCODER_CLK_PIN, ENCODER_DT_PIN)
encoder_switch = digitalio.DigitalInOut(ENCODER_SW_PIN)
encoder_switch.direction = digitalio.Direction.INPUT
encoder_switch.pull = digitalio.Pull.UP

# Microstep mode (1/8 step)
mode1.value = False
mode2.value = True
mode3.value = True

# Parameters
speed = 0.01
acceleration = 0.0002
direction = True

previous_encoder_position = encoder.position

def rotate_motor(steps, direction, speed):
    dir.value = direction
    for _ in range(steps):
        step.value = True
        time.sleep(speed)
        step.value = False
        time.sleep(speed)

while True:
    current_encoder_position = encoder.position
    encoder_delta = current_encoder_position - previous_encoder_position
    previous_encoder_position = current_encoder_position

    if encoder_delta != 0:
        direction = copysign(1, encoder_delta) > 0
        speed = max(0.001, speed + acceleration * abs(encoder_delta))

    if not encoder_switch.value:  # Switch pressed
        speed = 0.01  # Reset speed

    if speed > 0.001:  # Only move if speed is above threshold
        rotate_motor(1, direction, speed)
