#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:26:16 2018

@author: wangshanmin
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
            
        return self.KMP(haystack, needle)
    
    def KMP(self, text, pattern):
        prefix = self.getPrefix(pattern)
        j = -1
        for i in range(len(text)):
            while j > -1 and pattern[j + 1] != text[i]:
                j = prefix[j]
            if pattern[j + 1] == text[i]:
                j += 1
            if j == len(pattern) - 1:
                return i - j
        return -1
    
    def getPrefix(self, pattern):
        prefix = [-1] * len(pattern)
        j = -1
        for i in range(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]:
                j = prefix[j]
            if pattern[j + 1] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix

    
# Time:  O(n * k)
# Space: O(k)
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().strStr("a", ""))
    print(Solution().strStr("abababcdab", "ababcdx"))