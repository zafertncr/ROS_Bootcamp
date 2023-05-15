#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def sin_wave():
    rospy.init_node('sin_wave') 
    pub= rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) 
    t = 0.0
    while not rospy.is_shutdown():
        vel_msg = Twist()
        vel_msg.linear.x = 0.5 
        vel_msg.angular.z = math.sin(2 * math.pi *0.1* t) 
        pub.publish(vel_msg)
        t += 0.1 
        rate.sleep()
if __name__ == '__main__':
    try:
        sin_wave()
    except rospy.ROSInterruptException:
        pass
