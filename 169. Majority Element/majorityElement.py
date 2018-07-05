#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 14:57:32 2018

@author: wangshanmin
"""
import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#        idx, cnt = 0, 1

#        for i in range(1, len(nums)):
#            if nums[idx] == nums[i]:
#                cnt += 1
#            else:
#                cnt -= 1
#                if cnt == 0:
#                    idx = i
#                    cnt = 1
#
#        return nums[idx]
        return sorted(collections.Counter(nums).items(), key=lambda a: a[1], reverse=True)[0][0]
        
if __name__ == '__main__':
    print(Solution().majorityElement([1,2,2,2,1,2,1])) 