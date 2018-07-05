#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:12:05 2018

@author: wangshanmin
"""

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
#        else:
#            
#            return min(strs)
               
               
if __name__ == '__main__':
    a = ['abc','abc']
    print(Solution().longestCommonPrefix(a))
            