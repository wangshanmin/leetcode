#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 18:40:48 2018

@author: wangshanmin
"""
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        dict['I'] = 1
        dict['V'] = 5
        dict['X'] = 10
        dict['L'] = 50
        dict['C'] = 100       
        dict['D'] = 500
        dict['M'] = 1000
        i = 0
        val = 0
        while i < len(s):
            if i+1 < len(s):
                if s[i+1] > s[i]:
                    val -= dict[s[i]]
                else:
                    val += dict[s[i]]
            else:
                val += dict[s[i]]
            i += 1
        return val
        
if __name__=='__main__':
    print(Solution().romanToInt("IX"))        
 
