#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:04:53 2018

@author: wangshanmin
"""

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
                dict = {}
        dict[0] = ''
        dict[1] = 'One'
        dict[2] = 'Two'
        dict[3] = 'Three'
        dict[4] = 'Four'
        dict[5] = 'Five'
        dict[6] = 'Six'
        dict[7] = 'Seven'
        dict[8] = 'Eight'
        dict[9] = 'Nine'
        dict[10] = 'ten'
        dict[20] = 'twenty'
        dict[30] = 'thirty'
        dict[40] = 'fourty'
        dict[50] = ''
        dict[60] = 'LX'
        dict[70] = 'LXX'
        dict[80] = 'LXXX'
        dict[90] = 'XC'
        dict[100] = 'C'
        dict[200] = 'CC'
        dict[300] = 'CCC'
        dict[400] =  'CD'       
        dict[500] = 'D'
        dict[600] = 'DC'
        dict[700] = 'DCC'    
        dict[800] = 'DCCC'
        dict[900] = 'CM' 
        dict[1000] = 'M'        
        dict[2000] = 'MM'  
        dict[3000] = 'MMM' 
        
        
if __name__=='__main__':
    print(Solution().numberToWords(123))