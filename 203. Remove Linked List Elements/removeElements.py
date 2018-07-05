#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 21:37:16 2018

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
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(float('inf'))
        dummy.next = head
        pre, cur = dummy, dummy.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next
                
            
        

if __name__=='__main__':
    a = ListNode(1)
    b = a.next = ListNode(2)
    c = b.next = ListNode(3)
    d = c.next = ListNode(1)
    print(Solution().removeElements(a, 1))