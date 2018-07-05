#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 13:41:30 2018

@author: wangshanmin
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for num in nums:
            if num  in res:
                res.remove(num)
            else:
                res.append(num)
        return res[-1]
    
if __name__=='__main__':
    print(Solution().singleNumber([1,2,3,4,3,2,1]))