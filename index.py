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


def calibrate_servo(s):
    set_servo_to_angle(s, 0)
    time.sleep(2)
    set_servo_to_angle(s, 90)
    time.sleep(2)
    set_servo_to_angle(s, 180)


def point_up():
    set_servo_to_angle(s0, 90)
    time.sleep(0.5)
    set_servo_to_angle(s1, 90)
    time.sleep(0.5)
    set_servo_to_angle(s2, 90)


def point_straight():
    set_servo_to_angle(s0, 10)


def point_back():
    set_servo_to_angle(s0, 160)


setup()
time.sleep(0.2)
point_up()
time.sleep(0.5)
point_straight()
time.sleep(0.5)
point_back()
