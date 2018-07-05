#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:51:33 2018

@author: wangshanmin
"""

class Solution:
    def getRow(self, rowIndex):
        result = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            old = result[0] = 1
            for j in range(1, i + 1):
                old, result[j] = result[j], old + result[j]
        return result
    
if __name__ == '__main__':
    print(Solution().getRow(3))