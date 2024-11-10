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

def move_lift_arm(degrees, speed):
    lift_motor.run_angle(speed, degrees)

def move_spin_motor(degrees, speed):
    spin_motor.run_angle(speed, degrees)

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
    move_straight(210, 400)
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
    # coral tree support
    move_straight(108, 400)
    move_lift_arm(-130, 200)
    move_straight(260, 400)
    move_lift_arm(60, 200)
    move_straight(-200, 400)
    # shark
    turn_for_degrees(45, 200)
    move_lift_arm(-60, 200)
    move_straight(590, 400)
    turn_for_degrees(-87, 200)
    move_straight(295, 400)
    # coral buds and diver
    move_straight(-325, 400)
    turn_for_degrees(40, 200)
    move_straight(130, 400)
    turn_for_degrees(-85, 200)
    move_lift_arm(55, 200)
    move_straight(170, 400)
    move_lift_arm(-55, 200)
    move_straight(-185, 400)
    # coral reef support
    turn_for_degrees(95, 200)
    move_straight(-50, 400)
    move_lift_arm(40, 200)
    move_straight(90, 400)
    move_lift_arm(25, 200)
    move_straight(-100, 400)
    # coral reef flower
    move_straight(80, 400)
    move_lift_arm(40, 200)
    move_lift_arm(-100, 200)
    # back to homebase
    move_straight(-700, 400)
    drive_base.use_gyro(False)

def trip_3():
    drive_base.use_gyro(True)
    # trident and deliver shark
    move_straight(180, 400)
    turn_for_degrees(-10, 200)
    move_straight(300, 400)
    turn_for_degrees(-25, 200)
    move_straight(270, 400)
    move_straight(-50, 400)
    turn_for_degrees(20, 200)
    # back to homebase
    move_straight(-700, 400)
    drive_base.use_gyro(False)

def trip_4():
    drive_base.use_gyro(True)
    # crab
    move_straight(780, 400)
    move_lift_arm(200, 200)
    move_straight(-55, 400)
    move_lift_arm(-40, 200)
    # back to homebase on other side
    move_straight(-100, 400)
    move_lift_arm(-160, 200)
    turn_for_degrees(-40, 200)
    move_straight(250, 400)
    turn_for_degrees(50, 200)
    move_straight(900, 400)
    drive_base.use_gyro(False)

def trip_5():
    drive_base.use_gyro(True)
    # sonar discovery
    move_straight(795, 400)
    move_spin_motor(-780, 300)
    move_spin_motor(-200, 300)
    move_straight(-100, 400)
    # change shipping lanes
    turn_for_degrees(-30, 200)
    move_straight(-350, 400)
    move_straight(250, 400)
    # back to homebase
    turn_for_degrees(35, 200)
    move_straight(-800, 400)
    drive_base.use_gyro(False)

def trip_6():
    drive_base.use_gyro(True)
    # get the octopus
    move_straight(360, 400)
    # go to push angler fish
    turn_for_degrees(65, 200)
    move_straight(450, 400)
    turn_for_degrees(-120, 200)
    move_straight(650, 400)
    # back and release octopus
    move_straight(-220, 400)
    move_lift_arm(-150, 200)
    turn_for_degrees(-20, 200)
    move_straight(-120, 400)
    # lift submersible
    turn_for_degrees(65, 200)
    move_straight(310, 400)
    move_lift_arm(-100, 200)
    move_straight(-310, 400)
    drive_base.use_gyro(False)

def main():
    selected = hub_menu("T", "1", "2", "3", "4", "5", "6")

    if selected == "T":
        test_robot()
    elif selected == "1":
        trip_1()
    elif selected == "2":
        trip_2()
    elif selected == "3":
        trip_3()
    elif selected == "4":
        trip_4()
    elif selected == "5":
        trip_5()
    elif selected == "6":
        trip_6()

main()
