import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

servos = [0, 1, 2]


def setup():
    for s in servos:
        kit.servo[s].set_pulse_width_range(900, 2100)
        kit.servo[s].actuation_range = 160


def set_all_to_angle(angle):
    for s in servos:
        kit.servo[s].angle = angle


def set_servo_to_angle(s, angle):
    kit.servo[s].angle = angle


setup()

ranges = range(0, 160, 10)

for s in servos:
    for r in ranges:
        set_servo_to_angle(s, r)
        time.sleep(1)
