#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:00:37 2018

@author: wangshanmin
"""

class Solution(object):
    def isHappy(self, n):
        lookup = {}
        while n != 1 and n not in lookup:
            lookup[n] = True
            n = self.nextNumber(n)
        return n == 1

    def nextNumber(self, n):
        new = 0
        for char in str(n):
            new += int(char)**2
        return new
                
        
if __name__=='__main__':
    print(Solution().isHappy(12))
            
            