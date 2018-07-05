#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 10:08:11 2018

@author: wangshanmin
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        val = 0
        for i in range(len(digits)):
            val = digits[i] + val * 10 
        val = val + 1
        
        while val != 0:
            result.append(val % 10)
            val = val // 10 
        return list(reversed(result))
        
    
if __name__ =='__main__':
    print(Solution().plusOne([1,9]))