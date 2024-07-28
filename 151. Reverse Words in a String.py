# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:02:49 2024

@author: ALFRED
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word=s.strip()
        word=word.split()
        word=word[-1::-1]
        return ' '.join(word)