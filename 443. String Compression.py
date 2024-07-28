# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 18:19:09 2024

@author: ALFRED
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        r,i=0,0
        while (i<len(chars)):
            chars_occ=chars[i]
            chars_count=0
            while (i<len(chars) and chars_occ==chars[i]):
                chars_count+=1
                i+=1
            chars[r]=chars_occ
            r+=1
            if chars_count>1:
                chars_count_str=str(chars_count)
                for j in range(len(chars_count_str)):
                    chars[r]=chars_count_str[j]
                    r+=1
        return r
