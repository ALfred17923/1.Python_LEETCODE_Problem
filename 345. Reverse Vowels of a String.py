# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:42:07 2024

@author: ALFRED
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        p=list(s)
        vowel=set('aeiouAEIOU')
        i,j=0,len(p)-1
        while i<j:
            if p[i] not in vowel:
                i+=1
            elif p[j] not in vowel:
                j-=1
            else:
                p[i],p[j]=p[j],p[i]
                i+=1
                j-=1
        return "".join(p)