#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 20:31:20 2018

@author: wangshanmin
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            count = 0
            for i in range(1,len(nums)):
                if nums[count] != nums[i]:
                    count +=1
                    nums[count] = nums[i]
        else:
            return 0
        return count+1

if __name__=="__main__":
    a=[1,2,2,3,3,4]
    print(Solution().removeDuplicates(a))