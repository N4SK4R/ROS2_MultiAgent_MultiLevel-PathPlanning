# Robot-Operating-System
Design and implementation of a multi-agent path planning system using the Robot Operating System 2 (ROS2) framework. The system leverages ROS2’s various communication models to enable realtime efficient coordination between multiple autonomous agents operating in a shared multi-level environment

A publisher-subscriber communication model for agents to boradcast its position to the central co-ordinator which updates the global state map

A server-client communication model for agents to request path for scehduled tasks 

ROS2 uses a well-organized file structure to manage packages, nodes, and resources. <br>
A package is the basic unit of software organization. Each package contains all the necessary files for a specific functionality, such as nodes, launch files, configuration files, etc.

**System Info:** These packages were tested on Ubuntu 22.04 with ROS2 Humble.

### Runtime Instructions

Open Terminal 
```
mkdir ros2_ws
cd ros2_ws && mkdir src
cd src
```
After cloning the repo and building it, just type `ros2 launch rviz_marker display_marker.launch.py` into the terminal to get started. 
This will launch Rviz and show a 10x10 grid <br>
Then type `ros2 run agent service_test` on another terminal to display the agent marker on the grid

```
Ready to update goal pose for agent
```

To Broadcast Transforms type `ros2 service call /update_goal my_robot_interfaces/srv/UpdateGoal "goal_pose:` 
```
  position:
    x: 0.0
    y: 0.0
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"
```
Send a Geometry Pose msg to call the service

https://github.com/user-attachments/assets/f5409514-85fe-4ddf-b162-f3b95d7a29da

https://github.com/user-attachments/assets/52c1bb41-dbc0-40bb-9e08-968d06c5cfe2


