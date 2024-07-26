# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 09:47:47 2024

@author: ALFRED
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        nums_value=sum(nums[:k])
        max_value=nums_value
        start_index=0
        end_index=k
        while end_index<len(nums):
            nums_value-=nums[start_index]
            start_index+=1
            nums_value+=nums[end_index]
            end_index+=1
            max_value=max(nums_value,max_value)
        return float(max_value)/k
nums=[1,12,-5,-6,50,3]
k=4
sol=Solution()
print(sol.findMaxAverage(nums,k))