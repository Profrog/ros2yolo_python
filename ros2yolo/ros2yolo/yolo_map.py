import rclpy
from rclpy.node import Node
from custom_msg.msg import Ros2Yolo     # CHANGE
import numpy as np
import matplotlib.pyplot as plt
import os

global map_x
map_x = 1000

global map_y
map_y = 1000


global yolomap0
yolomap0 = np.zeros((map_x,map_y))

global image_name
image_name = 'yolomap1.png'

global seq
seq = 0 

global image_dir
image_dir = 'map_data/'


class Yolomap(Node):
     
    def __init__(self,Hz):
        super().__init__('yolomap')
        self.frame_id = 'ros2yolo'
        self.subscription = self.create_subscription(Ros2Yolo, self.frame_id ,self.listener_callback, 1)
        timer_period = 1/Hz  # seconds , how frequency pub data
        #self.timer = self.create_timer(timer_period, self.listener_callback)
        #self.subscription
        msg = Ros2Yolo
        
        
    def point_mark(self,x1,x2,y1,y2,data):    
     for x0 in range(x1,x2 +1,1):
       for y0 in range(y1,y2 +1,1):
         yolomap0[x0,y0] = int(data) #after using other way  
        
        
        

    def listener_callback(self,msg):
     try:        
      
        
       camera_x = int(map_x/2)
       camera_y = 0
       
       #yolomap0 = np.zeros((map_x,map_y))    
       #self.point_mark(int(camera_x - map_x/10) ,int(camera_x + map_x/10) , int(camera_y) , int(camera_y + map_y/5) , 2)
      
      
        
       o_map_xl = int((msg.o_x*100 - msg.o_size_x)) + camera_x
       o_map_xr = int((msg.o_x*100 + msg.o_size_x)) + camera_x
       o_map_yf = int((msg.o_y*100 - msg.o_size_z)) + camera_y
       o_map_yb = int((msg.o_y*100 + msg.o_size_z)) + camera_y
       
          
       if o_map_xl < 0: o_map_xl = 0
       if o_map_xl >= map_x: o_map_xl = map_x - 1
       if o_map_xr < 0: o_map_xr = 0
       if o_map_xr >= map_x: o_map_xr = map_x - 1
       
       if o_map_yf < 0: o_map_yf = 0
       if o_map_yf >= map_y: o_map_yf = map_y - 1
       if o_map_yb < 0: o_map_yb = 0
       if o_map_yb >= map_y: o_map_yb = map_y - 1
       
       print(msg.o_label + ":" + str(o_map_xl) + "," + str(o_map_xr) + "^" + str(o_map_yf) + "," + str(o_map_yb)+ "\n")
       
       
       '''
       for x0 in range(o_map_xl, o_map_xr+1,1):
        for y0 in range(o_map_yf, o_map_yb+1,1):
         yolomap0[x0,y0] = 1 #after using other way
       '''
       
       self.point_mark(o_map_xl,o_map_xr,o_map_yf,o_map_yb,1)
       
       
       
       plt.matshow(yolomap0)

       global seq 
       if seq < 100:
        seq +=1
       
       else:
        seq = 1
                
       image_name =  image_dir + "yolomap" + str(seq) + ".jpg"


       
       if os.path.isfile(image_name):
        os.remove(image_name) 


       plt.savefig(image_name)
       
                
     except BaseException as e:
      print(e)  
      #self.get_logger().info('I heard: "%s"' % msg.detect_info) # CHANGE
         
       

def main(args=None):
    rclpy.init(args=args)
    yolo_map = Yolomap(2)
    rclpy.spin(yolo_map)

    yolo_map.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
