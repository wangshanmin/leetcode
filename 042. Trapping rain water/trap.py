#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:59:02 2018

@author: wangshanmin
"""
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
    ###time limited
#        re = 0
#        for i in range(len(height) - 1):
#            height1 = height[:i]
#            height2 = height[i+1:]
#            if height1 and height2:
#                m1 = max(height1[:])
#                m2 = max(height2[:])
#                re += max(0, min(m1, m2)-height[i])
#        return re
        i = 0
        j = len(height) -1
        re = 0
        max_l = max_r =0
        dl = {}
        dr = {}
        while i < len(height):
            dl[i] = max_l
            dr[j] = max_r
            if max_l < height[i]:
                max_l = height[i]
            if max_r < height[j]:
                max_r = height[j]
            i += 1
            j -= 1
        for i in range(len(dl)):
            re += max(0, min(dl[i], dr[i]) - height[i])
        return re 
                                   
        
        
        
        
        
if __name__=='__main__':
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))