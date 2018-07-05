#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 14:46:10 2018

@author: wangshanmin
"""

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = {}
        dict[0] = ''
        dict[1] = 'I'
        dict[2] = 'II'
        dict[3] = 'III'
        dict[4] = 'IV'
        dict[5] = 'V'
        dict[6] = 'VI'
        dict[7] = 'VII'
        dict[8] = 'VIII'
        dict[9] = 'IX'
        dict[10] = 'X'
        dict[20] = 'XX'
        dict[30] = 'XXX'
        dict[40] = 'XL'
        dict[50] = 'L'
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
        a = []
        b = ''
        i = 1000
        while len(a) < 4:
            a.append(num // i)
            num = num % i
            i = i // 10
        j = 0
        print(a)
        while j < len(a):
            b += dict[a[j] * 10 ** (len(a) - j-1)]
            j = j+1
        return b
                
            
        
        
if __name__=='__main__':
    print(Solution().intToRoman(58))