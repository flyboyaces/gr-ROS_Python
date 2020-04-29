#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2020 Zachary Hudson.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import rospy
import pickle
import numpy as np
from gnuradio import gr
from std_msgs.msg import *
from sensor_msgs.msg import *
from geometry_msgs.msg import *

class Publish_py(gr.sync_block):

	def __init__(self, topic, node_name, msg_type):
		rospy.init_node(node_name)
		self.pub = rospy.Publisher(topic, globals()[msg_type], queue_size=10)
		rate = rospy.Rate(10)
		gr.sync_block.__init__(self,
			name="Publish_py",
			in_sig=[np.byte],
			out_sig=None)
		self.topic = topic
		self.node_name = node_name
		self.msg_type = msg_type

	def work(self, input_items, output_items):
		in0 = input_items[0]
		msg = pickle.loads(in0.tostring())
		self.pub.publish(msg)
		print(msg)
		return len(input_items[0])