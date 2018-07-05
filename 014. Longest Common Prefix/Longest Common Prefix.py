#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 09:55:38 2018

@author: wangshanmin
"""

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""   
        for i, letter_group in enumerate(zip(*strs)):#tuplet
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
if __name__ =='__main__':
    print(Solution().longestCommonPrefix(['abc','ab','abd']))