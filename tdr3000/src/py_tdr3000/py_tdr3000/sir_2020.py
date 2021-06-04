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
        line_gng = self.ser.readline() #$GNGGA
        line_gph = self.ser.readline() #$GPHDT
        gph_list = line_gph.decode().replace('\x00','').split(',')
 
        if gph_list[0] == '$GNGGA':  #except process
         a = line_gph
         line_gph = line_gng
         line_gng = a
         gph_list = line_gph.decode().replace('\x00','').split(',')
     
     
     
        #heading_data = float(gph_list[1])
        gng_list = line_gng.decode().replace('\x00','').split(',')
        #latitude0 = gng_list[2]
        #longitude0 = gng_list[4]
      
    

        #msgList0 = self.tdr3000(gphdt)
        
        
        
             
        if len(gng_list) <= 0:
            self.get_logger().info('INS(LLA) 데이터 형태가 아니거나 데이터가 부족합니다. 현재 데이터 형태는 "%s" 입니다.' % msgList[0])
        else:    
            msg = Tdr3000()
            logString = ("\nLatitude : " 
                         + msgList[3] + "\nLongitude : " + msgList[5] + "\nheading_degree : " + msgList0[1]) 
                         
            # header
            quo, rem = divmod(float(msgList[1]), 1)
            quo = int(quo)
            rem = round(rem*1000000)
            msg.header.frame_id = self.frame_id
            msg.header.stamp.nanosec = rem
            msg.header.stamp.sec = quo
            
            # sensor data
            #msg.utc = float(msgList[1]) 
            msg.latitude = float(msgList[2])
            #msg.hemisphere_lati = msgList[3]
            msg.longitude = float(msgList[4])
            #msg.hemisphere_long = msgList[5]
            #msg.indicator = float(msgList[6])
            #msg.num_satellites = float(msgList[7])
            #msg.hdop = float(msgList[8])
            #msg.altitude = float(msgList[9])
            #msg.unit_altitude = msgList[10]
            #msg.geoidal_sep = float(msgList[11])
            #msg.unit_geoidal = msgList[12]
            msg.heading_degree = float(gph_list[1])
            
            # msg.speedground = float(msgList[7])
            # msg.courseground = float(msgList[8])
            
            # pup msg
            self.publisher_.publish(msg)
            
            if gng_list[0] == "$GNGGA":
                self.get_logger().info('sir_2020 : ------------- "%s"' % logString)
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
