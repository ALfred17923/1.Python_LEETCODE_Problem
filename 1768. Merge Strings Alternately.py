# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 08:48:43 2024

@author: ALFRED
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=[]
        i,j=0,0
        while i<len(word1) and j<len(word2):
                result.append(word1[i])
                result.append(word2[j])
                i+=1
                j+=1
        result.append(word1[i:])
        result.append(word2[j:])
        return "".join(result)
