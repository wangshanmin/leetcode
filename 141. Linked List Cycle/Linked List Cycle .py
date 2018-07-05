#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:47:03 2018

@author: wangshanmin
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            slow , fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
       
if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = a.next
    print(Solution().hasCycle(a))