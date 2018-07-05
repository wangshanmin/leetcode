#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:03:24 2018

@author: wangshanmin
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def maxDepth(self, root):
        if root:
            return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
#            return  1+max(map(self.maxDepth, (root.left, root.right)))  ## run maxDepth function according to root.left and root.right
        else:
            return 0
                
                          
if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.left.right = TreeNode(3)
    print(Solution().maxDepth(a))