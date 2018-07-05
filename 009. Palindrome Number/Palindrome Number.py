#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:02:54 2018

@author: wangshanmin
"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        target = x
        if x < 0:
            return False
        if x < 2**32:
            result = 0
            while x != 0:
                val = x % 10
                newresult = result*10 + val
                result = newresult
                x = x // 10
            if result > 2**32:
                return False
            else: 
                if target == result:
                    return True
                else:
                    return False
                
if __name__ == '__main__':
    a = 123
    print(Solution().isPalindrome(a))