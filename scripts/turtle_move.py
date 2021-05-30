#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def turtle_move(lin_vel,ang_vel):
    rospy.init_node('turtle_move', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) 

    vel = Twist()
    while not rospy.is_shutdown():
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel
        rospy.loginfo("Linear Vel = %f: Angular Vel = %f",lin_vel,ang_vel)

        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        lin_vel = 0.2
        ang_vel = 0.1
        turtle_move(lin_vel, ang_vel)
    except rospy.ROSInterruptException:
        pass