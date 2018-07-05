#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:16:24 2018

@author: wangshanmin
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums:
            count = 0
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[count] = nums[i]
                    count +=1
            del nums[count:]
            return count
if __name__== "__main__":
    a = [1,2,2,3,3,4,5]
    target = 3
    print(Solution().removeElement(a, target))