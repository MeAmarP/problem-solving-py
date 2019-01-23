#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Prob Link: https://www.hackerearth.com/practice/python/getting-started/input-and-output/practice-problems/golf/jadoo-and-dna-transcription/
Created on Wed Dec 26 20:55:34 2018

@author: amarp
"""


def JadooDNATrans(InChar):
    if(InChar == 'G'):
        return 'C'
    elif(InChar == 'C'):
        return 'G'
    elif(InChar == 'T'):
        return 'A'
    elif(InChar == 'A'):
        return 'U'

print(JadooDNATrans(input()))
