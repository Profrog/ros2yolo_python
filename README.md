# ros2yolo_python_yolomap

## start
* git clone https://github.com/Profrog/ros2yolo_python -b yolomap
* colcon build
* ./rosyolo


---------------------------------------------------------------

## result
![20210510_172342](https://user-images.githubusercontent.com/26535065/117773899-da657f00-b273-11eb-941b-06ac15e43e40.jpg)

![20210511_160606](https://user-images.githubusercontent.com/26535065/117773912-ddf90600-b273-11eb-9cef-ab4d63e7f3fa.jpg)
in real

![20210511_160624](https://user-images.githubusercontent.com/26535065/117773918-df2a3300-b273-11eb-9bbe-afe889226ac9.jpg)
in grid


---------------------------------------------------------------

## config

camera.py : webcam python code
size.txt : object's real size 'label{ x, y ,z }' -> m(meter) and label only use in cfg/???.names
yolomap1.png : result image
image2.jpg : yolo detect image
