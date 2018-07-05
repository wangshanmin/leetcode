#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:27:27 2018

@author: wangshanmin
"""

class Solution:
    def twoSum(self, nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
if __name__== '__main__':
    nums = [1,2,3,4,5]
    target = 6
    print(Solution().twoSum(nums,target))