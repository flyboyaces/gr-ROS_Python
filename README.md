# ROS Interface for GNU Radio
This Out-of-Tree Module is designed to interface the Robot Operating System (ROS) with GNU Radio.

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This OOT contains two blocks: Publisher_py and Subscriber_py. 
### Publisher_py
* Type: Sink
* Input: Byte
* Function: Takes Byte data as input and converts it into ROS data
### Subscriber_py
* Type: Source
* Output: Byte
* Function: Takes data from ROS and converts it into Byte data.
## Technologies
This OOT has been tested and verified using the following packages:
* ROS Melodic
* GNU Radio 3.7.11
* Python 2.7.11
* Ubuntu 18.04 LTS

## Setup
From inside the gr-ROS_Python directory, execute the following commands:
```
mkdir build
cd build
cmake ../
make
sudo make install
sudo ldconfig
```
