#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:40:14 2018

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
        for i in range(len(numbers)):
            if numbers[i] in dict.keys():
                return [dict[numbers[i]]+1, i+1]
            else:
                dict[target - numbers[i]] = i
        
        
if __name__ == '__main__':
    print(Solution().twoSum([1,3,4,5,7],8))