#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:53:10 2018

@author: amarp
"""

R1 = b'450'
R2 = b'45'
R3 = b'500'

AllDist = [R1,R2,R3]
R11 = int(AllDist[0].decode())
R12 = int(AllDist[1].decode())
R13 = int(AllDist[2].decode())
intAllDist = [R11,R12,R13]
print(intAllDist)
