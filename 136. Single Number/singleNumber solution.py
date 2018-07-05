#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:59:54 2018

@author: wangshanmin
"""

import operator
from functools import reduce 
class Solution:

    def singleNumber(self, nums):
        return reduce(operator.xor, nums)
    
if __name__=='__main__':
#    print(Solution().singleNumber([1,2,3,4,3,2,1]))    
    a = [1,2,3,4,3,2,1]
    print(reduce(operator.xor,a))