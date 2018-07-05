#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:03:38 2018

@author: wangshanmin
"""
import collections
class Solution(object):
    def hammingWeight(self, n):
#        return str(bin(n)).count('1')
        return collections.Counter(bin(n))['1']
if __name__=='__main__':
    print(Solution().hammingWeight(11))