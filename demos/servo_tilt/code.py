# Wiring:
#   Servo brown wire  -> GND
#   Servo red wire          -> VOUT (5V from USB)
#   Servo yellow wire -> A1

import time

import board
import pwmio
from adafruit_motor import servo

from adafruit_circuitplayground import cp

pwm = pwmio.PWMOut(board.A1, duty_cycle=0, frequency=50)
my_servo = servo.Servo(pwm)

cp.pixels.brightness = 0.2
cp.play_tone(523, 0.1)  # Beep so we know the program started

while True:
    # Tilt the board left and right to move the servo
    x, y, z = cp.acceleration  # x goes from about -9.8 to 9.8

    angle = (x + 9.8) / 19.6 * 180  # Turn -9.8..9.8 into 0..180 degrees
    angle = max(0, min(angle, 180))
    my_servo.angle = angle

    # Light up the pixel that matches the angle
    cp.pixels.fill((0, 0, 0))
    cp.pixels[int(angle / 180 * 9)] = (0, 255, 0)

    time.sleep(0.05)
