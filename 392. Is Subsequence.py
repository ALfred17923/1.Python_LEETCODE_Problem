# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 18:58:15 2024

@author: ALFRED
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i=i+1
            j=j+1
        return True if i==len(s) else False