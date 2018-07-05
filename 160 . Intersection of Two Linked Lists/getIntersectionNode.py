#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 20:15:46 2018

@author: wangshanmin
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        begin, tailA, tailB = None, None, None

        # a->c->b->c
        # b->c->a->c
        while curA and curB:
            if curA == curB:                                                                                                        
                begin = curA
                break

            if curA.next:
                curA = curA.next
            elif tailA is None:
                tailA = curA
                curA = headB
            else:
                break

            if curB.next:
                curB = curB.next
            elif tailB is None:
                tailB = curB
                curB = headA
            else:
                break

        return begin
    
if __name__=='__main__':
    a1 = ListNode(1)
    a2 = a1.next = ListNode(2)
    a3 = a2.next = ListNode(3)
    b1 = ListNode(4)
    b2 = b1.next = ListNode(5) 
    c1 = a3.next = b2.next = ListNode(6)
    c2 = c1.next = ListNode(7)
    c3 = c2.next = ListNode(8)
    print(Solution().getIntersectionNode(a1, b1))
            