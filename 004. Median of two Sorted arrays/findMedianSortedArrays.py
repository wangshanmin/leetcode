#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:33:16 2018

@author: wangshanmin
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2 
        num = sorted(num)
        nums =len(num)
        if nums % 2 == 0:
            return float((num[nums//2] + num[nums//2-1]) / 2)
        else:
            return float(num[nums//2])
        
if __name__=='__main__':
    print(Solution().findMedianSortedArrays([1,2],[3,4]))