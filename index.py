import time
from adafruit_servokit import ServoKit
from easing_functions import CubicEaseInOut

kit = ServoKit(channels=16)

sz = 0  # base
s0 = 1
s1 = 2
s2 = 3
sc = 4  # claw
# servos = [sz, s0, s1, s2, sc]
servos = [sz, s0]
joints = [s0, s1, s2]


def setup():
    for s in servos:
        kit.servo[s].set_pulse_width_range(900, 2100)
        kit.servo[s].actuation_range = 180


def current_milli_time():
    return int(round(time.time() * 1000))


def set_all_to_angle(angle):
    for s in servos:
        kit.servo[s].angle = angle


def set_servo_to_angle(s, angle):
    kit.servo[s].angle = angle


def move_to(s, start_angle, end_angle, steps):
    line = CubicEaseInOut(start=start_angle, end=end_angle, duration=steps)
    for a in range(0, steps):
        set_servo_to_angle(s, line.ease(a))
        time.sleep(1)


def calibrate_servo(s):
    set_servo_to_angle(s, 0)
    time.sleep(2)
    set_servo_to_angle(s, 90)
    time.sleep(2)
    set_servo_to_angle(s, 180)


def point_up():
    move_to(s0, 0, 90, 5)
    move_to(s1, 0, 90, 5)
    move_to(s2, 0, 90, 5)


def point_straight():
    set_servo_to_angle(s0, 10)


def point_back():
    set_servo_to_angle(s0, 160)


class Arm:
    _base = 0
    _s = [0, 0, 0]
    _claw = 0

    def move_to(self, ):
        pass

    def render(self):
        set_servo_to_angle(sz, self._base)
        for k, ss in enumerate(joints):
            set_servo_to_angle(ss, self._s[k])
        set_servo_to_angle(sc, self._claw)


setup()
# time.sleep(0.2)
# point_up()
# time.sleep(0.5)
# point_straight()
# time.sleep(0.5)
# point_back()

set_all_to_angle(0)
time.sleep(0.2)
set_all_to_angle(90)
time.sleep(0.2)
set_all_to_angle(180)
