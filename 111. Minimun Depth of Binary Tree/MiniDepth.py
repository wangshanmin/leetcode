#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:00:35 2018

@author: wangshanmin
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1
        
        
        
        
        
if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.left = TreeNode(1)
    a.left.left.left = TreeNode(1)
    print(Solution().minDepth(a))