#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 14:39:39 2018

@author: wangshanmin
"""
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        re = ''
        while i < len(str):
            if str[i].isdigit():
                re += str[i]
                i = i+1
            elif re == '' and (str[i] == '+' or str[i] == '-'):
                re += str[i]
                i = i+1
            elif re == '' and str[i] == ' ':
                i = i+1
            else:
                break
        if re:
            try:
                re = int(re)
                if abs(re) <= 2**31 - 1:
                    return re
                else:
                    if abs(re) == re:
                        return 2**31 - 1
                    return 2**31*-1
            except:
                return 0
        return 0
            
        
        
        
        
if __name__ == '__main__':
    print(Solution().myAtoi("2147483648"))