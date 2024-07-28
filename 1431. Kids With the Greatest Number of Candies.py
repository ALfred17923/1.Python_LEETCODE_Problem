# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 14:27:32 2024

@author: ALFRED
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies=max(candies)
        result=[]
        for i in candies:
            if i+extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result

