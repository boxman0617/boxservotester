import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[0].angle = 0
kit.servo[1].angle = 0
kit.servo[2].angle = 0

time.sleep(2)

kit.servo[0].angle = 180
kit.servo[1].angle = 180
kit.servo[2].angle = 180

time.sleep(2)

kit.servo[0].angle = 0
kit.servo[1].angle = 0
kit.servo[2].angle = 0