#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:27:09 2018

@author: wangshanmin
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:
    def deleteDuplicates(self, head):
        cur = head 
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
if __name__=='__main__':
    head = ListNode(0)
    head.next = ListNode(1)
    next_ = head.next.next = ListNode(1)
    print(Solution().deleteDuplicates(head))
            
                
                