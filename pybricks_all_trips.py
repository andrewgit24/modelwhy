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
    straight_acceleration=800,
    turn_rate=100,
    turn_acceleration=200
)
spin_motor = Motor(Port.F, Direction.CLOCKWISE)
lift_motor = Motor(Port.B, Direction.CLOCKWISE)

def test_robot():
    drive_base.use_gyro(True)
    drive_base.straight(100)
    drive_base.turn(90)
    drive_base.straight(-100)
    drive_base.turn(-90)
    drive_base.use_gyro(False)

def trip_1():
    drive_base.use_gyro(True)
    drive_base.straight(560)
#    lift_motor.run_angle(200, -50)
    drive_base.use_gyro(False)

def trip_2():
    drive_base.use_gyro(True)
    drive_base.straight(238)
    lift_motor.run_angle(200, -130)
    drive_base.straight(260)
    lift_motor.run_angle(200, 60)
    drive_base.straight(-200)
    drive_base.turn(45)
    lift_motor.run_angle(200, -60)
    drive_base.straight(575)
    drive_base.turn(-92)
    drive_base.use_gyro(False)

def trip_3():
    drive_base.use_gyro(True)
    drive_base.straight(100)
    drive_base.use_gyro(False)

def trip_4():
    drive_base.use_gyro(True)
    drive_base.straight(100)
    drive_base.use_gyro(False)

def trip_5():
    drive_base.use_gyro(True)
    drive_base.straight(795)
    spin_motor.run_angle(300, -780)
    spin_motor.run_angle(300, -200)
    drive_base.straight(-100)
    drive_base.turn(-30)
    drive_base.straight(-350)
    drive_base.straight(250)
    drive_base.turn(35)
    drive_base.straight(-800)
    drive_base.use_gyro(False)

def trip_6():
    drive_base.use_gyro(True)
    drive_base.straight(100)
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
