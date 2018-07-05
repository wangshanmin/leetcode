#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:51:47 2018

@author: wangshanmin
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
#                print(res)
                res[-(level+1)].append(root.val)
                print(res)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)


        
if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.right.left = TreeNode(6)
    a.right.right = TreeNode(7)
    print(Solution().levelOrderBottom(a))