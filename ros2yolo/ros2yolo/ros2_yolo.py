import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from custom_msg.msg import Ros2Yolo


import serial
import time
import os
import sys, time
import numpy as np
from scipy.ndimage import filters
import base64
import cv2
import io

from PIL import Image
from pyzbar import pyzbar
from datetime import datetime
import argparse
import time
import subprocess
import signal
import numpy as np
import re
import math

global yolo_image  #after yolo detecting image
yolo_image = 'image2.jpg'

global original_image #before yolo detecting image
original_image = 'image.jpg'

global src_ros2


global dir_weights
dir_weights = 'yolov4.weights'


global dir_cfg 
dir_cfg = 'cfg/yolov4.cfg'

global dir_coco
dir_coco = 'cfg/coco.names'


global path1
path1 = os.path.abspath('/home/mingyu/git_yolo/darknet/rosyolo2/ros2-vn300/dew_ws/image.jpg') 

#### about yolo #####3


global size0,string0
size0 = open('size.txt', 'r') #about size
string0 = size0.readline()


global fov
fov = 55
#other fov = 55

global w_fov
w_fov = 122


global h_fov
h_fov = 74

#### about camera ######


global image_d
global where_obj 

  
global d_info
global d_info0
 

#### about data #####
  
  
def encode_img(img_fn):#encoding for img to string
 img = img_fn
 jpg_img = cv2.imencode('.jpg', img)
 b64_string = base64.b64encode(jpg_img[1]).decode('utf-8') #utf-8, .jpg
 return b64_string
  

def decode_img(message): #decoding for string to img
 imgdata = base64.b64decode(str(message))
 image = Image.open(io.BytesIO(imgdata))
 image.save(yolo_image) #yolo_image here

        
class Ros2yoloPublisher(Node):

    def __init__(self, Hz):
        super().__init__('ros2yolo_publisher')
        self.frame_id = 'ros2yolo'
        self.publisher_ = self.create_publisher(Ros2Yolo, self.frame_id , 1)
        timer_period = 1/Hz  # seconds , how frequency pub data
        self.timer = self.create_timer(timer_period, self.yolo)
        

    def yolo(self):
        d_info0 = "" 
    
      
        net = cv2.dnn.readNet(dir_weights, dir_cfg)
        classes = []
        with open(dir_coco, "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
       
        print("waiting...")
            

        try: ## will go try
         	                
         #print("webcam start!")
         start = time.time()
         chk = 0         
         #vc.set(10,0.5)
         #ret, frame = vc.read()
         # cv2.imshow("Video Window", frame) #it can be show for  how frame  
             
         
         #cv2.imwrite(original_image,frame)     
         image = cv2.imread(original_image)
         #image = cv2.resize(image, None, fx=0.4, fy=0.4)
         height, width, channels = image.shape
             
         barcodes = pyzbar.decode(image)       
         blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False) #it about detect_size. check it 416*416
         net.setInput(blob)
         outs = net.forward(output_layers)
                   
         class_ids = []
         confidences = []
         boxes = []
         d_info = ""
         for out in outs:
          for detection in out:
           scores = detection[5:]
           class_id = np.argmax(scores)
           confidence = scores[class_id]
           if confidence > 0.5:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            # 좌표
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
                
                
                
            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)  
            font = cv2.FONT_HERSHEY_PLAIN
            
            
             
            for i in range(len(boxes)):
             if i in indexes:
              x, y, w, h = boxes[i]
              label = str(classes[class_ids[i]])
              
              #####about size####
              
              try:
               x_s = string0.find(label)
               
               if x_s < 0:
                raise Exception('no size')
                                            
               stringx = string0[x_s + len(label):x_s + len(label) + 20]
               linex = re.findall(r'(?<!\.)[-+]?\b\d+\.\d+(?!\.)\b', stringx)
               size_x = linex[0]
               size_y = linex[1] # getting image size
               size_z = linex[2]
               
               image_d = math.sqrt(width*width + height*height)
               size_d = math.sqrt(w*w + h*h)
               obj_d = math.sqrt(float(size_x)*float(size_x) + float(size_y)*float(size_y))               
               fov_d = (fov * math.pi/180) * size_d/image_d
               
               focal_l = (image_d/math.tan(fov/2 * math.pi/180))/2               
               fov_w = 2* (width / focal_l)  
               fov_h = 2* (height / focal_l)
               
               
               fov_ww = (fov_w * math.pi/180) * w/width
               fov_hh = (fov_h * math.pi/180) * h/height
               
                
               where_obj = obj_d/math.tan(fov_d)
               where_obj_x = (x + w/2 - width/2) * (obj_d/2) / (size_d/2)
               where_obj_y = math.sqrt(where_obj*where_obj - where_obj_x*where_obj_x)
               #where_obj_y = (y + h/2 - height/2) * (obj_d/2) / (size_d/2) #about y-asix
               d_info = label + ","  + str(where_obj) + "," + str(where_obj_x) + "," + str(where_obj_y) + "\n"
               
               if d_info0 != d_info:                        
                color = colors[i]
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                cv2.putText(image, label, (x, y + 30), font, 3, color, 3)
                cv2.putText(image, str(where_obj), (x, y + 60), font, 3, color, 3)
                #d_info = label + ","  + str(x) + "," + str(y) + "," + str(w) + "," + str(h) + " " + str(fov_w) + " " + str(fov_h) + "\n"
               
                # cv2.imshow("Image", image)
               
                if d_info != "":
                 msg = Ros2Yolo()
                 msg.o_image = encode_img(image)
                 msg.detect_info = d_info
                 msg.o_label = label
                 msg.o_x = where_obj_x
                 msg.o_y = where_obj_y
                 msg.o_size_x = float(size_x)
                 msg.o_size_z = float(size_z)
                  
                 self.get_logger().info('ros2yolo : "%s"' % msg.detect_info)
                 self.publisher_.publish(msg)   
                 decode_img(msg.o_image)
                 d_info0 = d_info
                 d_info = ""        
                
                                             
              except BaseException as e:
               print(e)
               d_info = ""
               #cv2.imshow("Image", image)             
               #####//size####
               
        except BaseException as f:
          print(f)
          d_info = ""
          #sys.exit()    
          
                                                   
        #vc.release()
        cv2.destroyAllWindows()
         
         
         
                        
                          
def main(args=None):

    rclpy.init(args=args)
    ros2yolo_publisher = Ros2yoloPublisher(2) # sensor frequerency is here
    rclpy.spin(ros2yolo_publisher)

    ros2yolo_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
