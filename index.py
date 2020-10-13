import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

sz = 0  # base
s0 = 1
s1 = 2
s2 = 3
sc = 4  # claw
servos = [sz, s0, s1, s2, sc]


def setup():
    for s in servos:
        kit.servo[s].set_pulse_width_range(900, 2100)
        kit.servo[s].actuation_range = 180


def set_all_to_angle(angle):
    for s in servos:
        kit.servo[s].angle = angle


def set_servo_to_angle(s, angle):
    kit.servo[s].angle = angle


setup()

set_servo_to_angle(sz, 0)

time.sleep(2)

set_servo_to_angle(sz, 90)

time.sleep(2)

set_servo_to_angle(sz, 180)
