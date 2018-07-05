#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 14:12:59 2018

@author: wangshanmin
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result, dvd = "", n

        while dvd:
            result += chr((dvd - 1) % 26  + ord('A')) 
            dvd = (dvd - 1) // 26
        return result[::-1]

if __name__ == "__main__":
    print(Solution().convertToTitle(28))
