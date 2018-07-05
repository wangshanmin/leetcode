#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:58:35 2018

@author: wangshanmin
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, val in enumerate(numbers):
            temp = target - val
            if temp in dict:
                return [dict[temp]+1, index+1]
            dict[val] = index
            
if __name__ == '__main__':
    print(Solution().twoSum([1,3,4,5,7],8))