#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 20:17:16 2018

@author: wangshanmin
"""

class Solution:
    def even(self, s, m):
        i = 0
        while m - i >= 0 and m + i < len(s):
            if s[m-i] == s[m+i]:
                i += 1
            else:
                break
        return  max(0,i-1) 

    def old(self, s, m):
        i = 0
        while m - i >= 0 and m+1+i < len(s):
            if s[m-i] == s[m+1+i]:
                i += 1
            else:
                break
        return max(0,i-1)
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        leng = 0
        for i in range(len(s)):
            m = self.even(s, i)
            if leng < m*2+1:
                leng =m *2+1
                re = s[i-m: i +m+1]
            
            if i+1 < len(s) and s[i] == s[i+1]:
                m = self.old(s, i)
                if leng < m*2+2:
                    leng = m*2+2
                    re = s[i-m : i+m+1+1]
        return re
        
if __name__=='__main__':
    print(Solution().longestPalindrome('ccc'))