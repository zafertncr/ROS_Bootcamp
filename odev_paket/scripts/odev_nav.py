#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def move_base_demo():
    rospy.init_node('move_base_demo', anonymous=True)
    
    goal_publisher = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    
    # Rota listesini oluşturun
    route = []
    
    # Kullanıcıdan hedef konumları alın ve rotaya ekleyin
    while True:
        goal_x = input("Hedef konumun x koordinatını girin (çıkmak için q): ")
        if goal_x == "q":
            break
        goal_y = input("Hedef konumun y koordinatını girin: ")
        
        # Hedef konumu rotaya ekleyin
        goal = PoseStamped()
        goal.header.frame_id = "map"  # Hedef konumun referans çerçevesi
        goal.pose.position.x = float(goal_x)
        goal.pose.position.y = float(goal_y)
        goal.pose.position.z = 0.0
        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0
        
        route.append(goal)
    
    rospy.sleep(1)  # Yayıncının başlatılması için bir süre bekleme
    
    # Rotayı yayınlayın
    for goal in route:
        goal_publisher.publish(goal)
        rospy.sleep(1)
    
    # Başlangıç konumuna dön
    for goal in reversed(route):
        goal_publisher.publish(goal)
        rospy.sleep(1)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        move_base_demo()
    except rospy.ROSInterruptException:
        pass
