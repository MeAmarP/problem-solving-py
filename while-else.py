#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To test while-else loop 
Created on Thu Nov 15 21:29:09 2018

@author: amarp
"""

import time

try:
    myMainFlag = 1
    while myMainFlag:
        myVisionFlag = 1
        while myVisionFlag:
            print('Run Vision Code')
            time.sleep(1)
            myVisionFlag = 0
except KeyboardInterrupt:
    print('Halt Vision Code')        
            