#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 20:00:15 2018

@author: wangshanmin
"""

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


if __name__== '__main__':
    nums = [1,2,3,4,5]
    target = 6
    print(Solution().twoSum(nums,target))