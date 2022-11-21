# lidar_gostop.py

import rospy, time
from sensor_msgs.msg import LaserScan #라이다
from std_msgs.msg import Int32MultiArray #초음파
from xycar_msgs.msg import xycar_motor

motor_msg = xycar_motor()
ultra_msg = None
distance = []

def callback(data): # 토픽이 들어오면 실행되는 콜백함수
    global distance, motor_msg
    global ultra_msg
    distance = data.ranges
    ultra_msg = data.data
    
def drive_go():
    global motor_msg, pub
    motor_msg.speed = 5
    motor_msg.angle = 0
    pub.publish(motor_msg)

def drive_stop():
    global motor_msg, pub
    motor_msg.speed = 0 # m/s
    motor_msg.angle = 0 # 0.4 = 20도
    pub.publish(motor_msg)
# 노드 선언 & 구독과 발행할 토픽 선언
rospy.init_node('lidar_driver') 
rospy.init_node('ultra_driver')
rospy.Subscriber('/scan', LaserScan, callback, queue_size = 1)
rospy.Subscriber('xycar_ultrasonic', Int32MultiArray, callback, queue_size = 1)
# xycar_ultrasonic 토픽이 도착하면 Int32MultiArray 메세지가 들어있는데, 
# callback 함수를 불러라.
pub = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)
    
time.sleep(3) # lidar 가동 시간 기다리기

while not rospy.is_shutdown():
    ok = 0
    for degree in range(30, 150):
        if distance[degree] <= 0.3: # 30cm
            ok += 1
        if ok > 3:
            drive_stop()
            break
    if ok <= 3:
        drive_go
        
    if ultra_msg[2] > 0 and ultra_msg[2] < 10: # 0 < 거리 < 10 이면 정차
        drive_stop()
    else:
        drive_go()    
        
# lidar_drive.py
