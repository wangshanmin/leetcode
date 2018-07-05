#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:04:15 2018

@author: wangshanmin
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows > 0:
            res = [[1]]
            for i in range(1, numRows):
                list_ = [1]*(i+1)
                if i > 1:
                    for j in range(1, i):
                        list_[j] = res[i-1][j] + res[i-1][j-1]
                res.append(list_)
            return res
        else:
            return []
                
            
if __name__=='__main__':
    print(Solution().generate(5))