from hub import port, motion_sensor
import runloop, motor_pair, motor, sys
sys.path.append('/flash/customlib')
from team66218lib import move_straight, turn_for_degrees, move_lift_arm, move_spin_motor

async def main():
    # initialize components
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    motion_sensor.reset_yaw(0)
    #await runloop.until(motion_sensor.stable)

    await move_straight(23, 400, True)
    await turn_for_degrees(90, 200, True)
    await move_straight(1, 400, True)
    await turn_for_degrees(80, 200, True)
    await move_straight(22, 400, True)

runloop.run(main())
