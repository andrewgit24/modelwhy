from hub import light_matrix, port, motion_sensor
import runloop, motor_pair, motor

async def move_straight(distance, speed ):
    #initialize parameters and motor
    angle = 0
    KP=0.3
    KI=0.0
    motion_sensor.reset_yaw(0)
    motor.reset_relative_position(port.D, 0)
    degree_factor=360/7.675
    if speed < 0:
        return
    if distance < 0:
        distance = distance * -1
        speed = speed * -1
    # drive the motor pair
    degrees = distance*degree_factor
    correction=0
    past_error = 0
    while abs(motor.relative_position(port.D)) < degrees:
        yaw=motion_sensor.tilt_angles()[0] * -0.1
        yaw=int(yaw)
        current_error= angle - yaw
        past_error = past_error +current_error
        correction = int(current_error *KP + past_error*KI)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity=speed)
    motor_pair.stop(motor_pair.PAIR_1)

async def turn_for_degrees(degrees, speed=300):
    # initialize parameters and motor
    KP=0.3
    KI=0.005
    motion_sensor.reset_yaw(0)
    adj_factor=180/112.5
    if speed < 0:
        return
    # turn motor pair
    adj_angle = int(degrees*adj_factor)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, adj_angle, 100, velocity=speed)
    yaw = motion_sensor.tilt_angles()[0]* -0.1
    error = degrees - yaw
    counter = 0
    while abs(error) > 2 and counter < 10:
        correction = int(error)
        if correction > 5:
            correction = 5
        elif correction < -5:
            correction = -5
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, correction, 100, velocity=speed)
        counter += 1
        yaw = motion_sensor.tilt_angles()[0]* -0.1
        error = degrees - yaw
    # get actual degrees
    yaw = motion_sensor.tilt_angles()[0]* -0.1
    actual_degrees=int(yaw)
    print("Actual Degrees ", actual_degrees)

async def move_lift_arm(degrees, speed):
    if speed < 0:
        return
    if degrees < 0:
        degrees = degrees * -1
        speed = speed * -1
    await motor.run_for_degrees(port.B, degrees, speed)

async def move_spin_motor(degrees, speed):
    if speed < 0:
        return
    if degrees < 0:
        degrees = degrees * -1
        speed = speed * -1
    await motor.run_for_degrees(port.F, degrees, speed)

async def main():
    # initialize components
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    motion_sensor.reset_yaw(0)
    #await runloop.until(motion_sensor.stable)

    await move_straight(23, 400)
    await turn_for_degrees(90, 200)
    await move_straight(1, 400)
    await turn_for_degrees(70, 200)
    await move_straight(20, 400)



runloop.run(main())
