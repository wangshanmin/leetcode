#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:38:42 2018

@author: wangshanmin
"""

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
        while fast and slow:
            fast = fast.next
            if fast is slow:
                return True
            if fast:
                fast = fast.next
            slow = slow.next
        return False
       
if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = a.next
    print(Solution().hasCycle(a))