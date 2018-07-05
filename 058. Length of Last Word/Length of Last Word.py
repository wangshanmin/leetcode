#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:31:14 2018

@author: wangshanmin
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        else:
            val = s.split(' ')
            for i in range(len(val)):
                if val[len(val)-i-1] != '':
                    return len(val[len(val)-i-1])
            if val[0] == '':
                return 0
#            
        
if __name__== '__main__':
    print(Solution().lengthOfLastWord(" "))