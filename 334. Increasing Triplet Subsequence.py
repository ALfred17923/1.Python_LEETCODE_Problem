# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:00:29 2024

@author: ALFRED
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f=float('inf')
        s=float('inf')
        for i in nums:
            if f>=i:
                f=i
            elif s>=i:
                s=i
            else:
                return True
        return False