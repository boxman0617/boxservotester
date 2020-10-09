import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

sx = 0
sy = 1
sz = 2
servos = [sx, sy, sz]

ranges = [
    [70, 180],  # x
    [70, 180],  # y
    [0, 180]    # z
]


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

for ss in servos:
    s_range = ranges[ss]
    for r in s_range:
        print(f'S [{ss}] angle -> {r}')
        set_servo_to_angle(ss, r)
        time.sleep(1)
