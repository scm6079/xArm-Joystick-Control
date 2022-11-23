import sys
from xarm.wrapper import XArmAPI

if __name__ == "__main__":
    """ Main entry point """
    if len(sys.argv) >= 2:
        ip = sys.argv[1]
    else:
        try:
            from configparser import ConfigParser

            parser = ConfigParser()
            parser.read('robot.conf')
            ip = parser.get('xArm', 'ip')
        except:
            ip = input('Please input the xArm ip address:')
            if not ip:
                print('input error, exit')
                sys.exit(1)
    ########################################################

    arm = XArmAPI(ip)
    arm.motion_enable(enable=True)
    arm.set_mode(0)
    arm.set_state(state=0)

    print("\n*** Set the robot to the home position ***\n")
    arm.reset(wait=True)

    print("\n*** Motion step a1 ***\n")
    arm.set_position(x=300, y=0, z=150, roll=-180, pitch=0, yaw=0, speed=100, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Motion step a2 ***\n")
    arm.set_position(x=300, y=200, z=250, roll=-180, pitch=0, yaw=0, speed=200, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Motion step a3 ***\n")
    arm.set_position(x=500, y=200, z=150, roll=-180, pitch=0, yaw=0, speed=300, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Motion step a4 ***\n")
    arm.set_position(x=500, y=-200, z=250, roll=-180, pitch=0, yaw=0, speed=400, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Motion step a5 ***\n")
    arm.set_position(x=300, y=-200, z=150, roll=-180, pitch=0, yaw=0, speed=500, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Motion step a6 ***\n")
    arm.set_position(x=300, y=0, z=250, roll=-180, pitch=0, yaw=0, speed=400, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Set the robot to the home position ***\n")
    arm.reset(wait=True)

    print("\n*** Motion step b1 ***\n")
    arm.set_position(x=300, y=0, z=150, roll=-3.1415926, pitch=0, yaw=0, speed=100, is_radian=True, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Motion step b2 ***\n")
    arm.set_position(x=300, y=200, z=250, roll=-3.1415926, pitch=0, yaw=0, speed=200, is_radian=True, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Motion step b3 ***\n")
    arm.set_position(x=500, y=200, z=150, roll=-3.1415926, pitch=0, yaw=0, speed=300, is_radian=True, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Motion step b4 ***\n")
    arm.set_position(x=500, y=-200, z=250, roll=-3.1415926, pitch=0, yaw=0, speed=400, is_radian=True, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Motion step b5 ***\n")
    arm.set_position(x=300, y=-200, z=150, roll=-3.1415926, pitch=0, yaw=0, speed=500, is_radian=True, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Motion step b6 ***\n")
    arm.set_position(x=300, y=0, z=250, roll=-3.1415926, pitch=0, yaw=0, speed=400, is_radian=True, wait=True)
    # print(arm.get_position(), arm.get_position(is_radian=True))

    print("\n*** Set the robot to the home position ***\n")
    arm.reset(wait=True)

    print("\n*** Disconnect ***\n")
    arm.disconnect()
