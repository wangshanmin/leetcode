#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:11:46 2018

@author: wangshanmin
"""

class Solution(object):
    def rob(self, num):
        if len(num) == 0:
            return 0

        if len(num) == 1:
            return num[0]

        num_i, num_i_1 = max(num[1], num[0]), num[0]  ### 2, 1
        for i in range(2, len(num)):
            num_i_1, num_i_2 = num_i, num_i_1     
            num_i = max(num[i] + num_i_2, num_i_1);    ###n-2 + num[i], n-1

        return num_i
             
        
if __name__ == '__main__':
    print(Solution().rob([2,1,1,2]))