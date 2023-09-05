from ev3dev2.motor import OUTPUT_B, OUTPUT_C, LargeMotor
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.button import Button


class Robot:
    def __init__(self):
        self.left_motor = LargeMotor(OUTPUT_B)
        self.right_motor = LargeMotor(OUTPUT_C)
        self.left_touch_sensor = TouchSensor(INPUT_1)
        self.right_touch_sensor = TouchSensor(INPUT_2)
        self.button = Button()
        self.speed = 50

    def move_forward(self):
        self.left_motor.on(speed=self.speed)
        self.right_motor.on(speed=self.speed)

    def move_backward(self):
        self.left_motor.on(speed=-self.speed)
        self.right_motor.on(speed=-self.speed)

    def move_left(self):
        self.left_motor.on(speed=-self.speed)
        self.right_motor.on(speed=self.speed)

    def move_right(self):
        self.left_motor.on(speed=self.speed)
        self.right_motor.on(speed=-self.speed)

    def return_to_start(self):
        movements_stack = []

        movements_stack.append(self.move_forward)
        movements_stack.append(self.move_right)
        movements_stack.append(self.move_backward)
        movements_stack.append(self.move_left)

        while movements_stack:
            movement = movements_stack.pop()
            movement()

    def run(self):
        while True:
            if self.button.up:
                self.move_forward()
            elif self.button.down:
                self.move_backward()
            elif self.button.left:
                self.move_left()
            elif self.button.right:
                self.move_right()
            elif self.button.enter:
                self.return_to_start()

            if self.left_touch_sensor.is_pressed or self.right_touch_sensor.is_pressed:
                self.speed = 20
            else:
                self.speed = 50


robot = Robot()
robot.run()