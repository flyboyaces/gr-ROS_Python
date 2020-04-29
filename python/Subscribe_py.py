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

msg = ""

class Subscribe_py(gr.sync_block):
	
	def __init__(self, topic, node_name, msg_type):
		rospy.init_node(node_name)
		rospy.Subscriber(topic, globals()[msg_type], self.callback)
		gr.sync_block.__init__(self,
			name="Subscribe_py",
			in_sig=None,
			out_sig=[np.byte])
		self.topic = topic
		self.node_name = node_name
		self.msg_type = msg_type

	def callback(self, data):
		global msg
		msg = pickle.dumps(data)

	def work(self, input_items, output_items):
		global msg
		out = output_items[0]
		_len = len(msg)
		if (_len > 0):
			out[0:_len] = [ord(x) for x in msg]
			msg = ""
			return (_len)
		else:
			return (0)

