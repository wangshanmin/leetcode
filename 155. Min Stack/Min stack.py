#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:59:25 2018

@author: wangshanmin
"""

class MinStack:
    def __init__(self):
        self.min = None
        self.stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
            print(self.min)
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x
                

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    # @return an integer
    def top(self):
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min

    # @return an integer
    def getMin(self):
        return self.min
        

if __name__ == "__main__":
    stack = MinStack()
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(-1)
    print(stack.top())