#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:23:40 2018

@author: wangshanmin
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
if __name__=='__main__':
    print(Solution().strStr("hello", "ll"))