Generating Features
$ cd ~/catkin_ws
$ roslaunch sensor_stick training.launch

Capturing Features
$ cd ~/catkin_ws
$ rosrun sensor_stick capture_features.py

Train Your SVM
$ pip install sklearn scipy
$ rosrun sensor_stick train_svm.py

Object Recognition python script
$ roslaunch sensor_stick robot_spawn.launch
in new terminal
$ chmod +x object_recognition.py
$ ./object_recognition.py

