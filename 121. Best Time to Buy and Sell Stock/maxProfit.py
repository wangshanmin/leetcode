#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:25:29 2018

@author: wangshanmin
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#        res = []
#        for i in range(len(prices)-1):
#            for j in range(i+1, len(prices)):
#                if prices[j] - prices[i] > 0:
#                    res.append(prices[j] - prices[i])
#        if res:
#            return max(res)
#        else:
#            return 0
        
        max_profit = 0
        min_profit = float('inf')
        for price in prices:
            min_profit = min(min_profit, price)
            max_profit = max(max_profit, price-min_profit)
        return max_profit
    
if __name__ == '__main__':
    print(Solution().maxProfit([1,4,2,5,10]))