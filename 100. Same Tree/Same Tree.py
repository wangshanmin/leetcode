#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:50:36 2018

@author: wangshanmin
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
                
                
                
        
if __name__=='__main__':
    a = TreeNode([])
#    a.left = 2
#    a.right = 1
    b = TreeNode([])
#    b.left = 2
#    b.right = 1
    print(Solution().isSameTree(a,b))
        