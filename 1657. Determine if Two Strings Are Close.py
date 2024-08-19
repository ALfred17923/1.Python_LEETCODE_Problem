# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:05:11 2024

@author: ALFRED
"""

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        #check length of two string isequal
        if len(word1)!=len(word2):
            return False
        #Get the Frequency
        d1={}
        d2={}
        for i in word1:
            d1[i]=d1.get(i,0)+1
        for i in word2:
            d2[i]=d2.get(i,0)+1
        #check the key value using unordered element using set
        if set(d1.keys())!=set(d2.keys()):
            return False
        #check the character set
        a=list(d1.values())
        b=list(d1.values())
        a.sort()
        b.sort()
        return a==b