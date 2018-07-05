#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:16:15 2018

@author: wangshanmin
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        a = int(a)
        b = int(b)
        item = 0
        while a or b:
            fir = a % 10
            sec = b % 10
            val = fir + sec + carry
            if val > 1:
                carry = 1
                val = val -2
            else:
                carry = 0
            result.append(val)
            a = a // 10
            b = b // 10
        if carry == 1:
            result.append(carry)
        List = list(reversed(result))
        for i in range(len(List)):
            item = item*10 + List[i]
        return str(item)

if __name__ == '__main__':
    a = '1010'
    b = '1011'
    print(Solution().addBinary(a,b))
        