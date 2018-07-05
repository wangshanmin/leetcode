#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:47:25 2018

@author: wangshanmin
"""

# Definition for a binary tree node.
class Solution:
    
    def isSymmetric(self, root):
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)
                
                
                 
                
                