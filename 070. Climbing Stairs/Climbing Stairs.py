#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:48:48 2018

@author: wangshanmin
"""

class Solution:
    def climbStairs(self, n):
        dp = [1 for i in range(n+1)]
        print(dp)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
if __name__ == '__main__':
    print(Solution().climbStairs(5))