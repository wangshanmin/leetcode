#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:16:54 2018

@author: wangshanmin
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop(-1))
        
#        nums[:] = nums[len(nums) - k:] + nums[0:len(nums) - k]

if __name__=='__main__':
    nums = [1,2,3,4,5,6]
    Solution().rotate(nums,3)
    print(nums)
         