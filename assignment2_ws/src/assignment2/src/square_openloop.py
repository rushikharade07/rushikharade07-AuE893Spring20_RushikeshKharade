#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    #
    # PI = 3.1415926535897
    # side_sq = 2
    speed = 0.2
    angular_speed = 0.2
    distance = 2
    # angular_speed = speed*2*PI/360
    # relative_angle = angle*2*PI/360

    count = 1

    while (count < 5):

        vel_msg.linear.x = speed
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        t0 = rospy.Time.now().to_sec()
        current_distance = 0


        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
            #After the loop, stops the robot
        vel_msg.linear.x = 0

        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = angular_speed

        t10 = rospy.Time.now().to_sec()
        current_angle = 0
        # t10 = rospy.Time.now().to_sec()
        # #
        while(current_angle < 1.57):
             velocity_publisher.publish(vel_msg)
             t11 = rospy.Time.now().to_sec()
             current_angle = angular_speed*(t11-t10)

        vel_msg.angular.z = 0
        #Force the robot to stop
        # velocity_publisher.publish(vel_msg)

        count = count + 1

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
