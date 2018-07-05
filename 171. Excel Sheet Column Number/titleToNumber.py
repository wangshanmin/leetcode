#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 15:51:32 2018

@author: wangshanmin
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            val = ord(s[i]) - ord('A') + 1
            result = result * 26 + val 
        return result
        
        
if __name__ == '__main__':
    print(Solution().titleToNumber('AB'))