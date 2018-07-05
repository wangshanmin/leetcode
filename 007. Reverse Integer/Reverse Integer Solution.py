#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 20:11:49 2018

@author: wangshanmin
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = []
        
        
        if x==0:
            return 0
            
        remains = abs(x)
        sign = -1 if x < 0 else 1
        
        while(True):
            # remains is not zero
            digit = remains % 10
            remains = remains / 10
            digits.append(digit)
            if remains == 0:
                break
        
        ret = 0
        for i in digits:
            ret *= 10
            ret += i
            
        ret *= sign
        if abs(ret) > 0x7FFFFFFF:
            return 0
        else:
            return ret