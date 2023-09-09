#!/usr/bin/env python3
import sys
import rospy
import moveit_commander


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_ur5_arm', anonymous=True)
robot = moveit_commander.RobotCommander()
arm_group = moveit_commander.MoveGroupCommander("arm_group")
arm_group.set_named_target("Home")
plan1 = arm_group.go()

rospy.sleep(8)

arm_group.set_named_target("inital_pose")
plan2 = arm_group.go()

arm_group.set_named_target("pick_up_pose")
plan3 = arm_group.go()

hand = moveit_commander.MoveGroupCommander("grriper")
hand.set_named_target("pick_up")
plan4 = hand.go()

print ("Object Attached")

arm_group.set_named_target("Drop_pose")
plan5 = arm_group.go()

hand.set_named_target("open")
plan6 = hand.go()

print("Object Detached")

arm_group.set_named_target("Home")
plan7 = arm_group.go()

moveit_commander.roscpp_shutdown()


   