# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:17:29 2024

@author: ALFRED
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_index=0
        right_index=0
        sum1=sum(nums)

        for i in range (len(nums)):
            right_index=sum1-left_index-nums[i]
            if right_index==left_index:
                return i
            left_index+=nums[i]
        return -1
