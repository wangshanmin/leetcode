# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Given a 32-bit signed integer, reverse digits of an integer.
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2**32:
            sy = False
            result = 0
            if x < 0:
                sy = True
            x = abs(x)
            while x != 0:
                val = x % 10
                newresult = result * 10 + val
                result = newresult
                x = x // 10
            if result > 2**32:
                return 0
            else:
                if sy:
                    return -result
                else:
                    return result
        else:
            return 0


if __name__ == '__main__':
    a = 123
    print(Solution().reverse(a))