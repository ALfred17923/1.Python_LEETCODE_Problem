# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 10:12:13 2024

@author: ALFRED
"""

class Solution(object):
    def longestSubarray(self, nums):
        start=0
        max_length=0
        zero_count=0
        for i in range (len(nums)):
            if nums[i]==0:
                zero_count+=1
            while zero_count>1:
                if nums[start]==0:
                    zero_count-=1
                start+=1
            max_length = max(max_length , i - start + 1)
        return max_length-1