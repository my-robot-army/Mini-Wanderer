from dora import Node

from mock_motor import forward, Motor, bread, sleep


def main():
    left_motor = Motor(0, 0, 1)
    right_motor = Motor(0, 2, 3)
    node = Node()

    print("电机驱动节点已启动，等待指令...")

    for event in node:
        if event["type"] == "INPUT" and event["id"] == "motor_command":
            try:
                arr = event["value"]  # StructArray
                # 把第一个元素取出来，还原成 dict
                command = {name: arr.field(name)[0].as_py() for name in arr.type.names}

                action = command.get("action", "speed")
                value = command.get("value", 0)

                if action == "speed":
                    forward(left_motor, right_motor, value)
                elif action == "brake":
                    bread(left_motor, right_motor)
                elif action == "stop":
                    sleep(left_motor, right_motor)

            except Exception as e:
                print(f"处理指令出错: {e}")


if __name__ == "__main__":
    main()
