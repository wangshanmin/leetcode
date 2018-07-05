#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:39:04 2018

@author: wangshanmin
"""
import math
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        val = math.sqrt(x)
        return int(val)
   
if __name__ == '__main__':
    print(Solution().mySqrt(9))