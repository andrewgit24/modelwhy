from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub()
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.CLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, 62, 112)
drive_base.settings(
    straight_speed=400,
    straight_acceleration=400,
    turn_rate=100,
    turn_acceleration=200
)
spin_motor = Motor(Port.F, Direction.CLOCKWISE)
lift_motor = Motor(Port.B, Direction.CLOCKWISE)

def move_straight(distance, speed):
    drive_base.straight(distance)

def turn_for_degrees(degrees, speed):
    drive_base.turn(degrees)

def move_lift_arm_up():
    lift_motor.run_until_stalled(-200)    

def move_lift_arm_down():
    lift_motor.run_until_stalled(200)    

def move_lift_arm(degrees, speed, stop_choice=Stop.COAST):
    lift_motor.run_angle(speed, degrees, stop_choice)

def move_spin_motor(degrees, speed):
    spin_motor.run_angle(speed, degrees)

def test_straight():
    drive_base.use_gyro(True)
    move_straight(800, 400)
    drive_base.use_gyro(False)

def test_robot():
    drive_base.use_gyro(True)
    move_straight(100, 400)
    turn_for_degrees(90, 200)
    move_straight(-100, 400)
    turn_for_degrees(-90, 200)
    drive_base.use_gyro(False)

def trip_1():
    drive_base.use_gyro(True)
    # clear left field
    move_straight(550, 400)
    turn_for_degrees(20, 200)
    move_straight(200, 400)
    move_straight(-450, 400)
    # treasure chest
    turn_for_degrees(32, 200)
    move_lift_arm(220, 200)
    move_straight(225, 400)
    move_lift_arm(-70, 50)
    move_straight(15, 400)
    move_lift_arm(70, 100)
    move_straight(-100, 400)
    # back to homebase
    turn_for_degrees(-45, 200)
    move_straight(-500, 400)
    drive_base.use_gyro(False)

def trip_2():
    drive_base.use_gyro(True)
    # coral reef flower
    move_straight(200, 400)
    move_lift_arm_up()
    turn_for_degrees(-70, 200)
    move_straight(540, 400)
    move_lift_arm(60, 200)
    turn_for_degrees(15, 400)
    move_lift_arm(55, 200)
    move_lift_arm(-55, 200)
    # shark
    turn_for_degrees(-87, 200)
    move_straight(-40, 400)
    move_lift_arm(68, 200)
    move_lift_arm_up()
    # coral buds and diver
    move_straight(-50, 400)
    turn_for_degrees(-25, 200)
    move_lift_arm(37, 200)
    move_straight(115, 400)
    move_lift_arm_up()
    # drop diver
    move_straight(-200, 400)
    turn_for_degrees(80, 200)
    move_straight(60, 400)
    move_lift_arm(35, 200)
    move_straight(-200, 400)
    # back to homebase
    move_lift_arm_up()
    turn_for_degrees(40, 200)
    move_straight(-700, 400)
    drive_base.use_gyro(False)

def trip_3():
    drive_base.use_gyro(True)
    # trident and deliver shark
    move_lift_arm_up()
    move_straight(480, 400)
    turn_for_degrees(-35, 200)
    move_straight(270, 400)
    move_straight(-50, 400)
    turn_for_degrees(20, 200)
    # crab
    move_straight(-220, 400)
    turn_for_degrees(45, 200)
    move_straight(350, 400)
    turn_for_degrees(-28, 200)
    move_straight(65, 400)
    move_lift_arm(186, 200)
    move_straight(-120, 400)
    # go to other homebase
    turn_for_degrees(-25, 200)
    move_straight(400, 400)
    turn_for_degrees(35, 200)
    move_straight(700, 400)
    drive_base.use_gyro(False)

def trip_4():
    drive_base.use_gyro(True)
    # get octopus
    move_straight(100, 400)
    turn_for_degrees(42, 200)
    move_straight(400, 400)
    # go to push angler fish
    turn_for_degrees(65, 200)
    move_straight(470, 400)
    turn_for_degrees(-120, 200)
    move_straight(670, 400)
    # back and release octopus
    move_straight(-220, 400)
    move_lift_arm(-150, 200)
    turn_for_degrees(-20, 200)
    move_straight(-120, 400)
    # lift submersible
    turn_for_degrees(65, 200)
    move_straight(305, 400)
    move_lift_arm(-100, 200)
    # sonar
    move_straight(-205, 400)
    turn_for_degrees(-80, 200)
    move_straight(-30, 400)
    move_spin_motor(360, 200)
    turn_for_degrees(-85, 200)
    move_straight(800, 400)
    drive_base.use_gyro(False)

def main():
    selected = hub_menu("T", "1", "2", "3", "4")

    if selected == "T":
        test_robot()
    elif selected == "1":
        trip_1()
    elif selected == "2":
        trip_2()
    elif selected == "3":
        trip_3()
    elif selected == "4":
        trip_x()

main()
