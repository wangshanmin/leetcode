#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:53:47 2018

@author: wangshanmin
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i+1] - prices[i])
        return profit
#        return sum(map(lambda x: max(prices[x + 1] - prices[x], 0),
#            range(len(prices[:-1]))))
#       
if __name__ == '__main__':
    print(Solution().maxProfit([1,4,2,5,10]))