import time

import pyarrow as pa
from dora import Node

STATES = [
    ("speed", 150, 3),  # 正转，速度150，持续3秒
    ("stop", 0, 2),     # 停止，持续2秒
    ("speed", -150, 3), # 反转，速度150，持续3秒
    ("brake", 255, 1)   # 刹车，持续1秒
]

def main():
    node = Node()
    state_idx = 0
    print("固定状态控制器启动...")

    while True:
        action, value, duration = STATES[state_idx]

        # 构造并发送指令
        command = {"action": action, "value": value}
        node.send_output(output_id="motor_command", data=pa.array([command]), metadata={})

        print(f"当前状态: {action} | 数值: {value} | 预计持续: {duration}s")

        # 等待指定时间
        time.sleep(duration)

        # 循环切换到下一个状态
        state_idx = (state_idx + 1) % len(STATES)


if __name__ == "__main__":
    main()
