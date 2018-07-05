#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:07:30 2018

@author: wangshanmin
"""

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = 0 
        n = len(s) - 1
        s = s.upper()
        while m <= n:
            if (s[m].isdigit() or s[m].isalpha()) and (s[n].isdigit() or s[n].isalpha()):
                if s[m] != s[n]:
                    return False
                else:
                    m = m+1
                    n = n-1
            elif not (s[m].isdigit() or s[m].isalpha()):
                m = m+1
            elif not (s[n].isdigit() or s[n].isalpha()):
                n = n-1
        return True
    
if __name__ == '__main__':
    print(Solution().isPalindrome("race a car"))

                    