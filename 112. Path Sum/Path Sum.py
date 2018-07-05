#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 19:25:11 2018

@author: wangshanmin
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:

    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
                        
                
        
if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.left.right = TreeNode(3)
    print(Solution().hasPathSum(a,4))