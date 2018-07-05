#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:39:49 2018

@author: wangshanmin
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"}":"{","]":"[",")":"("}
        stack = []
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or stack.pop() != dict[char]:
                    return False
            else:
                return False
        return stack == []
    
if __name__ == '__main__':
    a="[]"
    print(Solution().isValid(a))
                    
                    
                