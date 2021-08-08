#!/usr/bin/env python
# license removed for brevity
 

import actionlib
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult

rospy.init_node('send_client_goal')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
rospy.loginfo("Waiting for move base server")
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'map' 
goal.target_pose.pose.position.x = -4
goal.target_pose.pose.position.y = 3
goal.target_pose.pose.orientation.z = 0.727
goal.target_pose.pose.orientation.w = 0.686

client.send_goal(goal)
client.wait_for_result()

goal.target_pose.header.frame_id = 'map' 
goal.target_pose.pose.position.x = -7
goal.target_pose.pose.position.y = 4
goal.target_pose.pose.orientation.z = 1
goal.target_pose.pose.orientation.w = 0

client.send_goal(goal)
client.wait_for_result()
