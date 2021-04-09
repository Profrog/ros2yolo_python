# ros2yolo_python(빨리하려면 -> 사용법으)

해당 프로젝트는 2021/04/08에 작성

<strong>본 프로젝트는 웹캠에서 이미지를 받아 yolo로 탐지 시킨 후 이미지 상에서의 좌표{x,y,w,h}와 라벨, 원본 데이터를 ros2에 publish해주는 package입니다</strong> 


## weights_file 얻기
https://drive.google.com/file/d/1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT/view
<strong>yolov4.weights</strong> 다운로드

본 패키지를 돌리기 위해서는 .cfg, .names, .weights file이 필요합니다  
.weights file를 다운로드 받고 ~rosyolo_final/ 폴더에 복사 붙여넣기 합니다(cfg folder가 있는 경로입니다)
  
  
또한 핵심 기능들은 해당 코드에서 확인할 수 있습니다 :rosyolo_final/ros2yolo/ros2yolo/ros2_yolo.py
  

체크해야할 파라미터.
* yolo_image : yolo + original_image -> .jpg(yolo result)
* original_image : original_image -> .jpg(you want conveying to yolo)
* dir_weights : where is .weights
* dir_cfg :  where is .cfg
* dir_coco : where is .names

*path1는 절대 경로로 이미지를 보내고 싶을 때 응용하여 사용하시면 되겠습니다

---------------------------------------------------------------------------------------

## 기본적인 이슈

해당 패키지는 webcam를 필요로 합니다. 만약에 내장 웹캠이 없을 시에는 따로 웹캠을 구하여 usb포트로 연결하셔야 하며 그로인하여 코드가 작동하지 않는다면
<strong>vc = cv2.VideoCapture(0) # 0 = notebook_webcam, 2 = usb_webcam (in my computer)</strong> in ros2_yolo.py
여기를 수정

만약에 publishing 주기를 변경하고 싶다면(현재는 1초에 한 번씩 발행) <strong> ros2yolo_publisher = Ros2yoloPublisher(1) </strong> 여기를 수정.

yolo에서 다른 사이즈 기반의 이미지(기본 416* 416) 학습하였을 시에는  <strong> blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False) #it about detect_size. </strong> in ros2_yolo.py
여기를 수정

----------------------------------------------------------------------------------------------------------------------------

## <strong>사용법</strong>

1. git clone https://github.com/Profrog/ros2yolo_python
2. colcon build
3. source install/setup.bash
4. ros2 run ros2yolo ros2_yolo

------------------------------


![example](https://user-images.githubusercontent.com/26535065/113983975-8b4bb900-9885-11eb-9fbd-6bf8b6c322c0.png)



-----------------------------------------------------------------------------------------------------------------

## 시스템 환경

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

## ros2와 yolov4 개발환경 셋팅을 위한 참조 
* ros2 : https://docs.ros.org/en/foxy/Installation.html
* yolov4 : https://github.com/AlexeyAB/darknet





