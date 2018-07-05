#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:36:24 2018

@author: wangshanmin
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        val = bin(n)[2:][::-1]
        return int(val + '0'*(32 - len(val)), 2)    

if __name__ == '__main__':
    print(Solution().reverseBits(8))

    