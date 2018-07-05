#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:05:35 2018

@author: wangshanmin
"""

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            result += n // 5
            n //= 5
        return result
        
if __name__ == '__main__':
    print(Solution().trailingZeroes(30))