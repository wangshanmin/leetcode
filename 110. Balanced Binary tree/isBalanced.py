#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 14:54:44 2018

@author: wangshanmin
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    
    def cal_depth(self, root):
        if not root:
            return 0
        else:
            return max( 1 + self.cal_depth(root.left), 1 + self.cal_depth(root.right))
      
                    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        
        return abs(self.cal_depth(root.left) - self.cal_depth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
            
if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.left = TreeNode(1)
    a.left.left.left = TreeNode(1)
    print(Solution().isBalanced(a))
    
        
    
            