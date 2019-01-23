# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:44:11 2019

@author: apotdar
"""

def isPalindrome(InputStr):
    myStr = list(InputStr)
    myRevStr = list(reversed(myStr))
    if myStr == myRevStr:
        print('YES')
    else:
        print('NO')
        
if __name__ == '__main__':
    isPalindrome(input())
