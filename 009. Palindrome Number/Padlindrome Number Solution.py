#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 20:13:05 2018

@author: wangshanmin
"""

class Solution:
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        ranger = 1
        while x // ranger >= 10:
            ranger *= 10
        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) // 10  #cut head and end
            ranger //= 100
            print(x,ranger)

        return True
    
if __name__ == '__main__':
    a = 12321
    print(Solution().isPalindrome(a))