#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 20:05:37 2018

@author: wangshanmin
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            print(l1)
            print(l2)
            l1.next = self.mergeTwoLists(l1.next,l2)
            print(l1)
#        return l1 or l2
    


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l2 = ListNode (2)
    l2.next = ListNode(3)
    Solution().mergeTwoLists(l1, l2)