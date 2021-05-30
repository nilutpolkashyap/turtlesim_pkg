#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

def turtle_move():
    rospy.init_node('turtle_move', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1) 

    vel = Twist()

    vel.linear.x = 0
    vel.angular.z = 0
    pub.publish(vel)
    rate.sleep()

    for i in range(2):
        vel.linear.x = 0
        vel.angular.z = 0
        pub.publish(vel)
        rate.sleep()

    	vel.linear.x = 4
    	vel.angular.z = 0
    	pub.publish(vel)
        rate.sleep()

    	vel.linear.x = 0
    	vel.angular.z = 1.565
    	pub.publish(vel)
        rate.sleep()

        vel.linear.x = 5
        vel.angular.z = 0
        pub.publish(vel)
        rate.sleep()

        vel.linear.x = 0
        vel.angular.z = 1.565
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        turtle_move()
    except rospy.ROSInterruptException:
        pass