import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16, frequency=60)

servos = [0, 1, 2]


def setup():
    for s in servos:
        kit.servo[s].set_pulse_width_range(200, 577)


def set_all_to_angle(angle):
    for s in servos:
        kit.servo[s].angle = angle


setup()

set_all_to_angle(0)

time.sleep(2)

set_all_to_angle(180)

time.sleep(2)

set_all_to_angle(0)
