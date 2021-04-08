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
      
        net = cv2.dnn.readNet(dir_weights, dir_cfg)
        classes = []
        with open(dir_coco, "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

      
        vc = cv2.VideoCapture(0) # 0 = notebook_webcam, 2 = usb_webcam (in my computer)
        print("waiting...")
            

        if True:
         #print("webcam start!")
         start = time.time()
         chk = 0         
         vc.set(10,0.5)
         ret, frame = vc.read()
         # cv2.imshow("Video Window", frame) #it can be show for  how frame  
             
         
         cv2.imwrite(original_image,frame)     
         image = cv2.imread(original_image)
         # image = cv2.resize(image, None, fx=0.4, fy=0.4)
         height, width, channels = image.shape
             
         barcodes = pyzbar.decode(image)       
         blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False) #it about detect_size. check it
         net.setInput(blob)
         outs = net.forward(output_layers)
                   
         class_ids = []
         confidences = []
         boxes = []
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
            
            global d_info
            d_info = ""
             
            for i in range(len(boxes)):
             if i in indexes:
              x, y, w, h = boxes[i]
              label = str(classes[class_ids[i]])
              color = colors[i]
              cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
              cv2.putText(image, label, (x, y + 30), font, 3, color, 3)
              d_info += label + ","  + str(x) + "," + str(y) + "," + str(w) + "," + str(h) + "\n"
              # cv2.imshow("Image", image)
             
            
             

    
         msg = Ros2Yolo()
         # print(msg)
         msg.o_image = encode_img(image)
         msg.detect_info = d_info
         self.get_logger().info('ros2yolo : "%s"' % msg.detect_info)
         self.publisher_.publish(msg)   

         decode_img(msg.o_image)   
         vc.release()
         cv2.destroyAllWindows()
         
         

                
                          
def main(args=None):

    rclpy.init(args=args)
    ros2yolo_publisher = Ros2yoloPublisher(1) # sensor frequerency is here
    rclpy.spin(ros2yolo_publisher)

    ros2yolo_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
