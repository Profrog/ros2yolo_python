# ros2yolo_python(fast->use that)

this project is basis in date of 2021/04/08


## getting weights_file
https://drive.google.com/file/d/1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT/view
is named <strong>yolov4.weights</strong> 

you need .cfg, .names, .weights file for yolo in ros2
if you download .weights file in that link, you put that in ~rosyolo_final/(in that dir, there are cfg folder, and then you can check .cfg and .names)
  
also  check rosyolo_final/ros2yolo/ros2yolo/ros2_yolo.py
(there is key code for yolo data sending to ros2)  

and check  what is
* yolo_image : yolo + original_image -> .jpg(yolo result)
* original_image : original_image -> .jpg(you want conveying to yolo)
* dir_weights : where is .weights
* dir_cfg :  where is .cfg
* dir_coco : where is .names

*path1 is used for if you wnat sending yolo_image or original image to otehr directory

---------------------------------------------------------------------------------------

## basis issue

this code use your webcam, if you don't have webcam in notebook you need other external webcam and usd connet to notebook
modify  <strong>vc = cv2.VideoCapture(0) # 0 = notebook_webcam, 2 = usb_webcam (in my computer)</strong> in ros2_yolo.py

if you want to modify publishing frequency(basis is 1) modifiy <strong> ros2yolo_publisher = Ros2yoloPublisher(1) </strong>

if you need to other size in yolo(basis is 416*416) check <strong> blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False) #it about detect_size. </strong> 

----------------------------------------------------------------------------------------------------------------------------

## <strong>use that</strong>

1. git clone https://github.com/Profrog/ros2yolo_python
2. colcon build
3. source install/setup.bash
4. ros2 run ros2yolo ros2_yolo

------------------------------


![example](https://user-images.githubusercontent.com/26535065/113983975-8b4bb900-9885-11eb-9fbd-6bf8b6c322c0.png)



-----------------------------------------------------------------------------------------------------------------

## system setting

    ### about yolo
    
    yolo version : yolov4

    notebook : HP-Pavilion-Gaming-Laptop-16-a0xxx
    process : Intel® Core™ i7-10750H CPU @ 2.60GHz × 12
    gpu1 : NVIDIA Corporation TU116M [GeForce GTX 1660 Ti Mobile]
    gpu2 : Intel Corporation UHD Graphics
    cuda: 11.2
    cuDNN : v8.1.1
    NVIDIA-SMI 460.39
    Driver Version: 460.39
    opencv :4.4.0
    python :3.8.5
    cmake : 3.20.0
    os : Ubuntu 20.04.2 LTS x86_64

    ### about ros2
    
    ros2 version : foxy

-----------------------

## ros2 and yolo tutorial(for that setting)
ros2 : https://docs.ros.org/en/foxy/Installation.html
yolov4 : https://robocademy.com/2020/05/01/a-gentle-introduction-to-yolo-v4-for-object-detection-in-ubuntu-20-04/





