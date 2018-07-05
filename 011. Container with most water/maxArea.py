#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 19:12:41 2018

@author: wangshanmin
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(height) - 1
        while  i <= j:
            val = abs((i-j)*min(height[i],height[j]))
            if val > res:
                res= val
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return res
    
    
if __name__=='__main__':
    print(Solution().maxArea([1,2,1]))