from hub import port, motion_sensor
import runloop, motor_pair, motor

# async function to move motor pair straight
async def move_motor_pair(steering, speed):
    motor_pair.move(motor_pair.PAIR_1, steering, velocity=speed)

# motor move straight forward and backward
async def move_straight(distance, speed, KP=0.8, debug = False):
    #debugging
    if debug:
        print('===== move_straight =====')
        print('distance = ' + str(distance))
        print('speed = ' + str(speed))

    #initialize parameters and motor
    angle = 0
    KI=0.0
    timer = 200
    motion_sensor.reset_yaw(0)
    motor.reset_relative_position(port.D, 0)
    degree_factor=360/7.675
    if speed < 0 or distance < 0:
        distance = abs(distance)
        speed = abs(speed) * -1

    # drive the motor pair
    degrees = distance * degree_factor
    correction=0
    past_error = 0
    while abs(motor.relative_position(port.D)) < degrees:
        yaw=motion_sensor.tilt_angles()[0] * -0.1
        yaw=int(yaw)
        current_error= angle - yaw
        past_error = past_error +current_error
        correction = int(current_error *KP + past_error*KI)
        if speed < 0:
            correction *= -1
        runloop.run(move_motor_pair(correction, speed))
        runloop.sleep_ms(timer)
    motor_pair.stop(motor_pair.PAIR_1)

    # debugging
    if debug:
        yaw=motion_sensor.tilt_angles()[0] * -0.1
        print('Robot off course by ' + str(yaw) + " degrees")

# turn motor at an angle
async def turn_for_degrees(degrees, speed, KP=1.0, debug = False):
    #debugging
    if debug:
        print('===== turn_for_degrees =====')
        print('degrees = ' + str(degrees))
        print('speed = ' + str(speed))

    # initialize parameters and motor
    KI=0.0
    timer=200
    motion_sensor.reset_yaw(0)
    steer = 100
    adj_factor=180/112.5
    if speed < 0 or degrees < 0:
        degrees = abs(degrees)
        speed = abs(speed)
        steer = -100

    # turn motor pair
    adj_angle = int(degrees*adj_factor)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, adj_angle, steer, velocity=speed)
    yaw = motion_sensor.tilt_angles()[0]* -0.1
    # debugging
    if debug:
        print("current angle = " + str(yaw))

    # current errors
    error = degrees - abs(yaw)
    past_error = 0
    counter = 0
    while abs(error) > 2 and counter < 10:
        correction = int(error * KP + past_error * KI)
        if correction > 5 and counter > 3:
            correction = 5
        elif correction < -5 and counter > 3:
            correction = -5
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, correction, steer, velocity=speed)
        counter += 1
        yaw = motion_sensor.tilt_angles()[0]* -0.1
        # debugging
        if debug:
            print('correction = ' + str(correction))
            print("current angle = " + str(yaw))
        error = degrees - abs(yaw)
        past_error = past_error + error

    # get actual degrees
    if debug:
        yaw = motion_sensor.tilt_angles()[0]* -0.1
        actual_degrees=int(yaw)
        print('Actual Degrees ', actual_degrees)

# move the lift arm up and down
async def move_lift_arm(degrees, speed):
    if speed < 0 or degrees < 0:
        degrees = abs(degrees)
        speed = abs(speed) * -1
    await motor.run_for_degrees(port.B, degrees, speed)

# move the spin motor clockwise and counter-clockwise
async def move_spin_motor(degrees, speed):
    if speed < 0 or degrees < 0:
        degrees = abs(degrees)
        speed = abs(speed) * -1
    await motor.run_for_degrees(port.F, degrees, speed)

async def main():
    # initialize components
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    motion_sensor.reset_yaw(0)
    #await runloop.until(motion_sensor.stable)

    #await move_straight(100, 300, KP=0.75)
    await turn_for_degrees(-30, 250, KP=1.1, debug=True)
    #await move_straight(23, 400)
    #await turn_for_degrees(90, 200)
    #await move_straight(1, 400)
    #await turn_for_degrees(70, 200)
    #await move_straight(20, 400)



runloop.run(main())
