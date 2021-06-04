import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from custom_msg.msg import Tdr3000

import serial
import numpy as np
import time
import os
# Tdr3000
# tdr3000


class PortCtrl():
    
    def __init__(self, baudRate=115200, portNum = None):
        os.system('ls /dev/serial/by-id/')
        if portNum==None:
            print('select port')
            self.portNum = input()
        else:
            self.portNum = str(portNum)
        os.system("sudo chmod a+rw /dev/ttyUSB"+self.portNum)
        self.ser = serial.Serial('/dev/ttyUSB'+self.portNum, baudRate, timeout = 1)
        
        
class Tdr3000Publisher(Node):

    def __init__(self, portCls, Hz):
        super().__init__('tdr3000_publisher')
        self.frame_id = 'tdr3000/num'+portCls.portNum
        self.publisher_ = self.create_publisher(Tdr3000, self.frame_id , 1)
        timer_period = 1/(Hz*2)  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.ser = portCls.ser

    def tdr3000(self, string):
        data_list = string.decode().replace('\x00','').split(',') 
        return data_list
        
    def status(self, errorBit):
        self.gpsFix = errorBit[5]
        self.mode = errorBit[6]*2+errorBit[7]
        self.gpsCompass = errorBit[14]
        self.INSHeding = errorBit[15]


    def timer_callback(self):
        #gnhdt = self.ser.readline()
        #serialBuffer = self.ser.readline()
        #msgList = self.tdr3000(serialBuffer)
        #gngga = self.ser.readline()
        serial_a = self.ser.readline()
        
        if len(serial_a) <= 0:
            self.get_logger().info('INS(LLA) 데이터 형태가 아니거나 데이터가 부족합니다. 현재 데이터 형태는 "%s" 입니다.' % msgList[0])
        else:    
            msg = Tdr3000()
            #logString = ("\nLatitude : " 
                         #+ msgList[3] + "\nLongitude : " + msgList[5] + "\nSpeedground : " + msgList[7]) 
                         
            # header
            #quo, rem = divmod(float(msgList[1]), 1)
            #quo = int(quo)
            #rem = round(rem*1000000)
            msg.header.frame_id = self.frame_id
            msg.header.stamp.nanosec = rem
            msg.header.stamp.sec = quo
            
            # sensor data
            #msg.latitude = float(msgList[3])
            #msg.longitude = float(msgList[5])
            #msg.speedground = float(msgList[7])
            # msg.courseground = float(msgList[8])
            msg.serial_data = serial_a
          

            # pup msg
            self.publisher_.publish(msg)
            
            if msgList[0] == "$GNRMC":
                self.get_logger().info('tdr_3000 : ------------- "%s"' % logString)
                # self.get_logger().info('GPS fix : "%s"' % str(bool(self.gpsFix)) )
                # self.get_logger().info('tdr3000 Heading fix : "%s" \n\n\n' % str(bool(self.INSHeding)) )
            else:
                self.get_logger().info('INS(LLA) 데이터 형태가 아닙니다. 현재 데이터 형태는 "%s" 입니다.' % msgList[0])


def main(args=None):

    portCls = PortCtrl(baudRate=115200, portNum = 0) # 인자 portNum = 0 을 지우면 사용자 입력으로 진행됩니다.

    rclpy.init(args=args)
    tdr3000_publisher = Tdr3000Publisher(portCls,40) # sensor rate는 여기에
    rclpy.spin(tdr3000_publisher)

    tdr3000_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
