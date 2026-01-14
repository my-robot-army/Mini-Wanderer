
# 配置常量
PWM_FREQ = 20000
PERIOD_NS = int(1e9 / PWM_FREQ)

class Motor:
    def __init__(self, chip, ch1, ch2):
        # 硬件初始化
        pass

    def set_speed(self, speed):
        pass

    def brake(self, val=255):
        pass

def forward(left, right, speed=255):
    print("forward")
    left.set_speed(speed)
    right.set_speed(speed)

def backward(left, right, speed=255):
    print("backward")
    left.set_speed(-speed)
    right.set_speed(-speed)

def turn_left(left, right, speed=255):
    print("turn left")
    left.set_speed(speed)
    right.set_speed(-speed)

def turn_right(left, right, speed=255):
    print("turn right")
    left.set_speed(-speed)
    right.set_speed(speed)

def bread(left, right):
    print("bread")
    left.brake()
    right.brake()

def sleep(left, right, speed=0):
    print("sleep")
    left.set_speed(speed)
    right.set_speed(speed)