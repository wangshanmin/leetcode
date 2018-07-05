#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 12:16:19 2018

@author: wangshanmin
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()
if __name__ =="__main__":
    print(Solution().merge([0],0,[1],1))