def getjoint(name):
    
    import roslib; roslib.load_manifest('pyrobots_actionlib')
    import rospy
    from sensor_msgs.msg import JointState
    
    data = rospy.wait_for_message("/joint_states", JointState)
    idx = data.name.index(name)
    return data.position[idx]

